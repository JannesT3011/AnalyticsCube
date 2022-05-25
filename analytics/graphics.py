import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from config import IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET
from imgurpython import ImgurClient
import os

client_id = IMGUR_CLIENT_ID
client_secret = IMGUR_CLIENT_SECRET

client = ImgurClient(client_id, client_secret)

def upload_to_imgur(path:str) -> str: # TODO async
    link = client.upload_from_path(path)["link"]
   
    return link

def plot_timestamp_hours(data:dict, guildid:str, name:str) -> str:
    df = pd.DataFrame(data)
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
    plt.title(f"{name} in which hours")
    path = f"{guildid}_timestamp_hours.png"
    plt.savefig(path)
    link = upload_to_imgur(path)
    plt.close()
    os.remove(path)
    
    return link
    
def plot_timestamp_weekdays(data:dict, guildid:str, name:str) -> str:
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["weekdays"] = df["timestamp"].dt.day_name()
    weekday_count = pd.value_counts(df["weekdays"])
    get_x = dict(weekday_count).keys()
    get_y = dict(weekday_count).values()
    x = [*get_x]
    y = [*get_y]
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    x = sorted(x, key=weekdays.index)
    plt.bar(np.array(x), np.array(y))
    plt.yticks(np.arange(min(y), max(y)+1, 2.0))
    plt.xlabel("Weekdays")
    plt.ylabel(f"{name}-Count")
    plt.title(f"{name} in which weekdays")
    path = f"{guildid}_timestamp_weekdays.png"
    plt.savefig(path)
    link = upload_to_imgur(path)
    plt.close()
    os.remove(path)

    return link

def plot_channels(data:dict, guildid, name:str, bot) -> str:
    df = pd.DataFrame(data)
    channels = [bot.get_channel(int(channel)).name for channel in df["channelid"]]
    channel_count = pd.value_counts(channels)
    get_x = dict(channel_count).keys()
    get_y = dict(channel_count).values()
    x = [*get_x]
    y = [*get_y]
    plt.bar(np.array(x), np.array(y))
    plt.yticks(np.arange(min(y), max(y)+1, 2.0))
    plt.xlabel("Hours")
    plt.ylabel(f"{name} in channel count")
    plt.title(f"{name} in which channels")
    path = f"{guildid}_channels.png"
    plt.savefig(path)
    link = upload_to_imgur(path)
    plt.close()
    os.remove(path)
    
    return link

def plot_users(data:dict, guildid) -> str:
    df = pd.DataFrame(data)
    x = df["timestamp"]
    y = df["count"]
    plt.plot(np.array(x), np.array(y))
    plt.xlabel("Time")
    plt.ylabel(f"Users-Count")
    plt.title(f"User counts")
    path = f"{guildid}_user_count.png"
    plt.savefig(path)
    link = upload_to_imgur(path)
    plt.close()
    os.remove(path)
   
    return link