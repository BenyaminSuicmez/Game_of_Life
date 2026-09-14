from src.graphical_interface import show_menu
from src.simulation import game_of_life_simulation


config = show_menu()

if config:
    game_of_life_simulation(generations=config["generations"], delay=config["delay"])



