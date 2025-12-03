import pandas as pd
import json

def load_clickstream(path):
    df = pd.read_csv(path, low_memory=False)
    if "timestamp" in df:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df = df.dropna(subset=["timestamp"])
    return df

def load_foot_traffic(path):
    df = pd.read_csv(path, low_memory=False)
    if "timestamp" in df:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df = df.dropna(subset=["timestamp"])
    return df

def load_weather(path):
    with open(path, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    if "timestamp" in df:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df = df.dropna(subset=["timestamp"])

    return df
