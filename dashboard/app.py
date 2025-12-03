import streamlit as st
import pandas as pd
import json
import io
from src.ingest import load_clickstream, load_weather, load_foot_traffic
from src.merge import merge_datasets
from src.eda import generate_all_charts
from src.llm_summary import generate_ai_summary
from src.report_gen import create_ppt_report
from src.anomaly_detector import AnomalyDetector
from src.recommendations import rule_based_recommendations, build_final_recommendations


st.title("InsightFusion – Automated Multi-Source Insight Engine")
st.write("Upload your files → Analyze → Generate Report → Download PPTX")

# Upload widgets
clickstream_file = st.file_uploader("Upload clickstream.csv", type=["csv"])
weather_file = st.file_uploader("Upload weather.json", type=["json"])
traffic_file = st.file_uploader("Upload foot_traffic.csv", type=["csv"])

if st.button("Run Analysis"):
    if not clickstream_file or not weather_file or not traffic_file:
        st.error("Please upload all 3 files.")
    else:
        with st.spinner("Processing data..."):

            # Load data
            df_click = load_clickstream(clickstream_file)
            df_weather = load_weather(json.load(weather_file))
            df_traffic = load_foot_traffic(traffic_file)

            # Merge datasets
            df = merge_datasets(df_click, df_weather, df_traffic)

            # Anomaly detection
            detector = AnomalyDetector()
            df = detector.detect_all(df)
            anomalies = detector.summarize_anomalies(df)

            # Rule-based recommendations
            rules = rule_based_recommendations(df)

            # LLM summary
            ai_summary = generate_ai_summary(df, anomalies)

            final_recs = build_final_recommendations(rules, ai_summary)

            # Generate charts
            chart_paths = generate_all_charts(df)

            # Generate ppt
            output_path = "reports/final_report_from_dashboard.pptx"
            create_ppt_report(df, chart_paths, ai_summary, final_recs, output_path)

            st.success("Report Generated Successfully!")
            st.download_button(
                label="Download PPTX",
                data=open(output_path, "rb").read(),
                file_name="InsightFusion_Report.pptx"
            )
