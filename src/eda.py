import matplotlib.pyplot as plt
from pathlib import Path

def compute_metrics(df):
    return {
        "total_impressions": int(df["impressions"].sum()),
        "total_clicks": int(df["clicks"].sum()),
        "ctr": float(df["clicks"].sum() / max(df["impressions"].sum(),1)),
        "avg_temperature": float(df["temperature"].mean()),
        "avg_visitors": float(df["visitors"].mean())
    }

def create_plots(df, outdir):
    out = Path(outdir); out.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8,3))
    df.set_index("timestamp")["impressions"].resample("D").sum().plot()
    plt.title("Daily Impressions")
    f1 = out/"daily_impressions.png"; plt.savefig(f1); plt.close()

    plt.figure(figsize=(8,3))
    df.set_index("timestamp")["revenue"].resample("D").sum().plot()
    plt.title("Daily Revenue")
    f2 = out/"daily_revenue.png"; plt.savefig(f2); plt.close()

    plt.figure(figsize=(8,3))
    df.plot.scatter("temperature","visitors",alpha=0.25)
    plt.title("Temperature vs Foot Traffic")
    f3 = out/"temp_vs_traffic.png"; plt.savefig(f3); plt.close()

    return [str(f1), str(f2), str(f3)]
