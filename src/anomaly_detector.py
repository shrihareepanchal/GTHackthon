import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)

    def detect_all(self, df):
        if "impressions" in df.columns:
            df["impressions_z"] = (df["impressions"] - df["impressions"].mean()) / df["impressions"].std()
            df["impressions_anomaly"] = (np.abs(df["impressions_z"]) > 2).astype(int)

        if "revenue" in df.columns:
            df["revenue_z"] = (df["revenue"] - df["revenue"].mean()) / df["revenue"].std()
            df["revenue_anomaly"] = (np.abs(df["revenue_z"]) > 2).astype(int)

        if "visitors" in df.columns:
            df["visitors_z"] = (df["visitors"] - df["visitors"].mean()) / df["visitors"].std()
            df["visitors_anomaly"] = (np.abs(df["visitors_z"]) > 2).astype(int)

        return df

    def summarize_anomalies(self, df):
        summary = []

        if "timestamp" in df.columns:
            dt_col = "timestamp"
        elif "date" in df.columns:
            dt_col = "date"
        else:
            dt_col = None
            for c in df.columns:
                if df[c].dtype == "datetime64[ns]":
                    dt_col = c
                    break
            if dt_col is None:
                dt_col = df.columns[0]

        if "impressions_anomaly" in df.columns:
            rows = df[df["impressions_anomaly"] == 1]
            for _, row in rows.iterrows():
                summary.append(f"Impression anomaly detected on {row[dt_col]}: value={row['impressions']}.")

        if "revenue_anomaly" in df.columns:
            rows = df[df["revenue_anomaly"] == 1]
            for _, row in rows.iterrows():
                summary.append(f"Revenue anomaly detected on {row[dt_col]}: value={row['revenue']}.")

        if "visitors_anomaly" in df.columns:
            rows = df[df["visitors_anomaly"] == 1]
            for _, row in rows.iterrows():
                summary.append(f"Foot-traffic anomaly detected on {row[dt_col]}: value={row['visitors']}.")

        return summary
