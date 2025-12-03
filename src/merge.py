def merge_sources(click_df, foot_df, weather_df):
    df = click_df.merge(foot_df, on="timestamp", how="left")
    df = df.merge(weather_df, on="timestamp", how="left")
    df = df.sort_values("timestamp")
    return df
