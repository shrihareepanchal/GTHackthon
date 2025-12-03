import pandas as pd
import json

def load_clickstream(path):
    return pd.read_csv(path, parse_dates=["timestamp"])

def load_foot_traffic(path):
    return pd.read_csv(path, parse_dates=["timestamp"])

def load_weather(path):
    with open(path) as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df
