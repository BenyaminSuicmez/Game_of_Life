from graphical_interface import show_menu
from simulation import game_of_life_simulation


config = show_menu()

if config:
    game_of_life_simulation(generations=config["generations"], delay=config["delay"])
