import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_plot(name:str, guild_id:str):
    df = pd.read_csv(f"./src/csv/{guild_id}_{name}.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hours"] = df["timestamp"].dt.hour
    name_count = pd.value_counts(df["hours"])
    get_x = dict(name_count).keys()
    get_y = dict(name_count).values()
    x = [*get_x]
    y = [*get_y]
    plt.bar(np.array(x), np.array(y))
    plt.yticks(np.arange(min(y), max(y)+1, 2.0))
    plt.xticks(np.arange(min(x), max(x)+1, 1.0))
    plt.xlabel("Hours")
    plt.ylabel(f"{name}-Count")
    plt.title(f"{name} ~ Plot")

    plt.savefig(f"./src/img/{guild_id}_{name}.png")
    plt.close()