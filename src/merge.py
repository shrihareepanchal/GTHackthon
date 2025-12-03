import pandas as pd

def merge_sources(click_df, foot_df, weather_df):
    def normalize_timestamp(df):
        for col in df.columns:
            if "time" in col.lower() or "date" in col.lower():
                df[col] = pd.to_datetime(df[col], errors="coerce")
                df = df.rename(columns={col: "timestamp"})
                return df
        df["timestamp"] = pd.to_datetime(df.index, errors="coerce")
        return df

    click_df = normalize_timestamp(click_df)
    foot_df = normalize_timestamp(foot_df)
    weather_df = normalize_timestamp(weather_df)

    df = click_df.merge(foot_df, on="timestamp", how="outer")
    df = df.merge(weather_df, on="timestamp", how="outer")

    df = df.sort_values("timestamp").reset_index(drop=True)

    return df
