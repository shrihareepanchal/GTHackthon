# InsightFusion: Multi-Source Automated Insight Engine (Gemini-Powered)
Tagline: A real-time, multi-source analytics engine that merges Clickstream, Weather, and Foot-Traffic data to auto-generate executive-ready PPTX reports enriched with Gemini-based insights — in under 20 seconds.

## 1. The Problem (Real-World Scenario)
Context — How AdTech Reporting Really Happens  
During my exploration of GroundTruth-style AdTech workflows, I discovered a major operational inefficiency: Account Managers spend 5–8 hours every week manually downloading CSVs, merging them in Excel, generating screenshots, and preparing “Weekly Performance Reports” for clients.

The Pain Point  
This manual process is slow, error-prone, highly repetitive, and not scalable. If CTR drops or traffic collapses due to weather, the client learns days later.

My Solution — InsightFusion  
I built InsightFusion, an automated system that ingests multiple data sources (Clickstream, Weather, Foot Traffic), merges them, runs automated EDA, extracts insights, and uses Google Gemini 1.5 Flash to generate a natural-language executive summary exported into a professional PPTX report.

## 2. Expected End Result
Input: Any CSV/JSON logs (clickstream, weather, traffic).  
Action: Run one command.  
Output: A professionally generated PPTX with:
- Daily impressions & revenue charts  
- Traffic-temperature correlation analysis  
- CTR trends  
- Gemini-written executive insights  
- Actionable recommendations  

## 3. Technical Approach
InsightFusion uses a true multi-source ETL architecture.

### Components:
- **Ingestion:** Load Clickstream CSV, Weather JSON, Foot Traffic CSV  
- **Merging:** Timestamp-based harmonization  
- **EDA:** Matplotlib visualizations  
- **AI Summary:** Gemini 1.5 Flash with PII masking & fallback  
- **Reporting:** python-pptx executive slide deck  

## 4. Tech Stack
- Python 3.10+  
- Pandas, NumPy  
- Matplotlib  
- Google Gemini 1.5 Flash  
- python-pptx  

## 5. Challenges & Learnings
**Challenge: Multimodal alignment**  
Solution: Timestamp normalization + stable merging.

**Challenge: AI Hallucination**  
Solution: Strict context instructions + PII masking.

## 6. Visual Proof
See `/screenshots` folder for:
- Dashboard preview  
- Charts  
- PPTX summary slide  

## 7. How to Run
```bash
pip install -r requirements.txt
export GEMINI_API_KEY="your_key"
python src/run_pipeline.py
```

Output:
```
reports/final_gemini_report.pptx
```

## 8. Folder Structure
src/  
data/  
reports/  
screenshots/  
requirements.txt  
README.md  

## 9. Conclusion
InsightFusion automates and accelerates AdTech analytics. It is scalable, fast, and engineered for the GroundTruth AI Hackathon.
