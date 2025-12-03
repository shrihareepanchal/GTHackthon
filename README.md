InsightFusion – Automated Multi-Source Insight Engine (Gemini Powered)

A real-time analytics system that unifies Clickstream, Weather, and Foot-Traffic data to automatically generate decision-ready PPTX reports enriched with AI-generated insights.

1. Overview — The Real Problem in AdTech Reporting

In fast-moving AdTech environments, client performance reports are often created manually by downloading CSV logs, merging different data sources in Excel, and generating charts slide-by-slide.
This process is:

Slow and repetitive

Prone to human error

Difficult to scale as data volume increases

Reactive rather than proactive

The delay in noticing drops in impressions, CTR, or foot-traffic means account teams cannot quickly adjust campaigns — leading to wasted budget and missed optimization opportunities.

What InsightFusion Solves

InsightFusion automates the entire reporting workflow.
With one command, the system:

Loads and merges multiple data sources

Extracts patterns using automated EDA

Generates high-quality charts

Uses Gemini 1.5 Flash to produce a professional executive narrative

Compiles everything into a polished PPTX report

This transforms hours of manual work into seconds.

2. Expected Output
User Flow

Input: Three raw files

clickstream.csv

weather.json

foot_traffic.csv

Process: Automated ETL → EDA → AI summary → Report generation

Output:
A complete multi-page PowerPoint presentation containing:

What the generated report includes

Daily impressions trend

Daily revenue movement

CTR insights

Relationship between weather and foot-traffic

AI-generated summary highlighting key takeaways

Recommended actions supported by real data

InsightFusion produces a client-ready deck without manual intervention.

3. System Design & Technical Breakdown

InsightFusion follows a modular ETL architecture:

A. Ingestion Layer

Handles structured & semi-structured inputs:

CSV (clickstream & foot-traffic)

JSON (weather logs)

Each dataset is normalized and indexed by timestamp.

B. Data Harmonization & Merging

All sources are merged into a single unified dataframe using outer-join logic across timestamps.
This enables cross-domain insight generation such as:

“Lower temperatures correlate with higher evening revenue.”

“Foot traffic declines sharply during rainfall spikes.”

C. Automated EDA

The pipeline generates meaningful visuals:

Line chart: Daily impressions

Line chart: Daily revenue

Scatter plot: Temperature vs Visitors

These charts serve as visual evidence for the PPT.

D. AI-Driven Insight Generation (Gemini Integration)

InsightFusion uses Gemini 1.5 Flash to produce an executive-level narrative.

Features:

Structured prompt containing metrics

PII masking for security

Fallback offline summary when API key is absent

Action-oriented recommendations

This ensures the final report is both analytical and business-focused.

E. Report Compilation

The final stage uses python-pptx to assemble:

Title slide

Executive summary slide

Metrics slide

Visual charts

Recommended strategy slide

The result is a polished PPTX that resembles an analyst-prepared deck.

4. Tech Stack
Component	Technology
Language	Python 3.x
Data Processing	Pandas, NumPy
Charts	Matplotlib
AI Model	Google Gemini 1.5 Flash
Reporting Engine	python-pptx
Security	PII Masking Layer
Data Sources	CSV + JSON
5. Key Challenges & Solutions
Challenge: Merging Datasets with Different Structures

Each source had unique schema and sampling intervals.
Solution:
Standardized timestamps and applied left-join alignment to maintain consistency.

Challenge: Ensuring LLM Output Accuracy

LLMs sometimes referenced data not present in the dataset.
Solution:
Implemented a strict context-bound prompt + removed non-deterministic language.

Challenge: Clean PPTX Formatting

Ensuring clean layout and readable text required precision.
Solution:
Defined standardized slide templates and controlled layout using measurement utilities.

6. Visual Outputs

Included in /screenshots/:

Dashboard preview

Daily impressions trend

Daily revenue trend

Temperature vs Visitors scatter plot

Sample generated PPT slide

These represent real pipeline results.

7. How to Run the Project
1. Install Dependencies
pip install -r requirements.txt

2. Add Gemini API Key

Linux/Mac:

export GEMINI_API_KEY="your_key_here"


Windows:

setx GEMINI_API_KEY "your_key_here"

3. Execute the Pipeline
python src/run_pipeline.py

4. Output File

Your report will automatically be generated at:

reports/final_gemini_report.pptx

8. Project Structure
src/
  ingest.py
  merge.py
  eda.py
  llm_summary.py
  report_gen.py
  run_pipeline.py

data/
  clickstream.csv
  weather.json
  foot_traffic.csv

reports/
  final_gemini_report.pptx
  images/

screenshots/
README.md
requirements.txt

9. Summary

InsightFusion demonstrates how multi-source data engineering, automated analytics, and AI reasoning can be brought together to streamline performance reporting in AdTech environments.

It eliminates manual effort, reduces delays, and equips teams with actionable insights instantly — making it a powerful, production-oriented solution tailored for the GroundTruth AI Hackathon.
