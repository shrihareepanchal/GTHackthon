import pandas as pd

def rule_based_recommendations(df):
    df = df.copy()
    df["ctr"] = df["clicks"] / df["impressions"].replace(0, 1)

    recs = []

    for i in range(1, len(df)):
        prev = df.iloc[i-1]
        today = df.iloc[i]

        if prev["ctr"] > today["ctr"] and abs(prev["impressions"] - today["impressions"]) < 0.05 * prev["impressions"]:
            recs.append("Creative fatigue detected due to CTR drop while impressions remain stable.")

        if today["revenue"] > prev["revenue"] and today["impressions"] < prev["impressions"]:
            recs.append("Conversion efficiency increased: revenue rising faster than impressions.")

        if today["temperature"] > prev["temperature"] and today["visitors"] < prev["visitors"]:
            recs.append("Foot traffic decrease associated with rising temperature.")

    return recs

def build_final_recommendations(rule_recs, llm_summary):
    final = []
    final.extend(rule_recs)
    final.append(llm_summary)
    return final
