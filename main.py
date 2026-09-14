from src.graphical_interface import show_menu
from src.simulation import game_of_life_simulation
from src.diagram import linear_analysis
from src.diagram import logarithmic_analysis

config = show_menu()



if config:
    game_of_life_simulation(generations=config["generations"], delay=config["delay"], pattern=config["pattern"])
    logarithmic_analysis()
 