import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def compute_metrics(df):
    impressions = df["impressions"].sum() if "impressions" in df else 0
    clicks = df["clicks"].sum() if "clicks" in df else 0
    temp = df["temperature"].mean() if "temperature" in df else 0
    visitors = df["visitors"].mean() if "visitors" in df else 0

    ctr = clicks / impressions if impressions > 0 else 0

    return {
        "total_impressions": int(impressions),
        "total_clicks": int(clicks),
        "ctr": float(ctr),
        "avg_temperature": float(temp),
        "avg_visitors": float(visitors),
    }

def ensure_timestamp(df):
    if "timestamp" not in df.columns:
        return df
    
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df = df.sort_values("timestamp")
    return df

def create_plots(df, outdir):
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)

    df = ensure_timestamp(df)

    f1 = out / "daily_impressions.png"
    f2 = out / "daily_revenue.png"
    f3 = out / "temp_vs_traffic.png"

    if "impressions" in df:
        plt.figure(figsize=(8, 3))
        try:
            df.set_index("timestamp")["impressions"].resample("D").sum().plot()
        except:
            df["impressions"].plot()
        plt.title("Daily Impressions")
        plt.savefig(f1)
        plt.close()

    if "revenue" in df:
        plt.figure(figsize=(8, 3))
        try:
            df.set_index("timestamp")["revenue"].resample("D").sum().plot()
        except:
            df["revenue"].plot()
        plt.title("Daily Revenue")
        plt.savefig(f2)
        plt.close()

    if "temperature" in df and "visitors" in df:
        plt.figure(figsize=(8, 3))
        df.plot.scatter("temperature", "visitors", alpha=0.25)
        plt.title("Temperature vs Foot Traffic")
        plt.savefig(f3)
        plt.close()

    return [str(f1), str(f2), str(f3)]
