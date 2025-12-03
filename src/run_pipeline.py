from anomaly_detector import AnomalyDetector
from recommendations import rule_based_recommendations, build_final_recommendations
from ingest import load_clickstream, load_foot_traffic, load_weather
from merge import merge_sources
from eda import compute_metrics, create_plots
from llm_summary import generate_summary
from report_gen import export_ppt

click = load_clickstream("data/clickstream.csv")
foot = load_foot_traffic("data/foot_traffic.csv")
weather = load_weather("data/weather.json")

df = merge_sources(click, foot, weather)
metrics = compute_metrics(df)

detector = AnomalyDetector()
df = detector.detect_all(df)
anomalies = detector.summarize_anomalies(df)

rule_recs = rule_based_recommendations(df)
llm_summary = generate_summary(metrics, anomalies)
final_recommendations = build_final_recommendations(rule_recs, llm_summary)

images = create_plots(df, "reports/images")

export_ppt(
    title="InsightFusion – Automated Multi-Source Report",
    summary=llm_summary,
    metrics=metrics,
    images=images,
    anomalies=anomalies,
    recommendations=final_recommendations,
    outpath="reports/final_report.pptx"
)

print("Report generated at: reports/final_report.pptx")
