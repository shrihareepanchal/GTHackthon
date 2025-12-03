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
images = create_plots(df, "reports/images")
summary = generate_summary(metrics)

export_ppt("Insights Report", summary, metrics, images, "reports/final_report.pptx")

print("Report generated at: reports/final_report.pptx")
