# The Game of Life

A NumPy implementation of Conway's Game of Life (1970), a cellular automaton
in which simple local rules produce surprisingly complex global behaviour.
The simulation runs in an OpenCV window and is configured through a small
Tkinter menu.

## The rules

Every cell on the grid is either alive or dead. In each generation, all cells
are updated simultaneously according to the following rules:

- A living cell with two or three living neighbours survives.
- A dead cell with exactly three living neighbours becomes alive.
- All other cells die or stay dead.

Each cell has eight neighbours, including the diagonal ones.

## Screenshots

**Configuration menu**

<img width="701" height="629" alt="Bildschirmfoto 2026-09-13 um 16 40 35" src="https://github.com/user-attachments/assets/2c7bddeb-3209-493d-9658-c4a26fa43cba" />

**Simulation running on an 800x800 grid**

<img width="795" height="828" alt="Bildschirmfoto 2026-09-13 um 16 41 00" src="https://github.com/user-attachments/assets/54bf6240-581f-4850-9ef2-53aa8cb6ef92" />

## How it works

The interesting part of this project is that no cell is ever visited
individually. There is no loop over the grid and no if-statement deciding the
fate of a single cell.

Counting neighbours is done by shifting the entire board eight times with
`np.roll`, once for every direction, and adding the results together. Since
living cells are stored as 1 and dead cells as 0, the sum at each position is
already the number of living neighbours at that position.

The rules are then applied as boolean masks over the whole array at once:

```python
survives = (board == 1) & ((neighbors == 2) | (neighbors == 3))
born = (board == 0) & (neighbors == 3)
board = (survives | born).astype(np.uint8)
```

Cells that appear in neither mask are dead in the next generation, so the
death conditions do not need to be written out explicitly.

Because `np.roll` wraps values around the edges, the grid behaves like a
torus: the top row is adjacent to the bottom row, and the left column to the
right one.

## Population analysis

The number of living cells is written to `data/population.csv` during the run,
one row per generation. After the simulation ends, the file is read back with
pandas and plotted with matplotlib.

Running a 800x800 grid with 30% initial density for 10,000 generations produces
a characteristic curve: the population collapses from roughly 220,000 to below
50,000 within the first few hundred generations, then settles at around 18,000
cells, about 3% of the grid.

<img width="999" height="662" alt="linear" src="https://github.com/user-attachments/assets/b98d264b-cc23-4204-a93e-7fb76aa789b1" />

Plotting the same run on a logarithmic scale makes the two phases visible. An
exponential decay would appear as a straight line; instead the curve bends
continuously and then flattens out entirely after roughly 5,000 generations.
The system does not die out, it settles into an equilibrium of still lifes and
small oscillators that no longer interfere with one another.

<img width="999" height="662" alt="log" src="https://github.com/user-attachments/assets/8d6b5d0c-82af-45dd-a6d3-1ae7c98ddd2f" />

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Usage

The menu lets you choose whether the simulation runs indefinitely or stops
after a given number of generations, and how long each generation is displayed
(20 to 2000 milliseconds).

While the simulation is running:

- `space` pauses and resumes
- `q` stops the simulation

Once the simulation ends, the population history is plotted automatically.

## Project structure

- `main.py` - entry point, connects menu, simulation and analysis
- `src/graphical_interface.py` - Tkinter configuration menu
- `src/simulation.py` — grid logic, OpenCV rendering, CSV logging
- `src/diagram.py` — reads the CSV and plots the population history
- `data/population.csv` — written on every run
