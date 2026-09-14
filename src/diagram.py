import pandas as pd
import matplotlib.pyplot as plt 

def logarithmic_analysis():
    
    df = pd.read_csv("data/population.csv")
    
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(df["generation"], df["population"])
    ax.set_title(("Population over time"))
    ax.set_xlabel("Generations")
    ax.set_ylabel("Population")
    ax.set_yscale("log")
    ax.grid(True, alpha=0.3)
    
    fig.canvas.manager.set_window_title("Analysis")
    fig.tight_layout()
    
    
    plt.show()
    
    
    
def linear_analysis():
    
    df = pd.read_csv("data/population.csv")
    
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(df["generation"], df["population"])
    ax.set_title(("Population over time"))
    ax.set_xlabel("Generations")
    ax.set_ylabel("Population")
    ax.grid(True, alpha=0.3)
    
    fig.canvas.manager.set_window_title("Analysis")
    fig.tight_layout()
    
    
    plt.show()