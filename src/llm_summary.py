import os
import re
import google.generativeai as genai

def mask_pii(text: str) -> str:
    text = re.sub(r"\b\d{10}\b", "XXXXXXXXXX", text)
    text = re.sub(r"[\w\.-]+@[\w\.-]+", "hidden@example.com", text)
    return text

def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        return True
    return False

def generate_summary(metrics: dict) -> str:
    gemini_enabled = configure_gemini()

    prompt = (
        f"Metrics: {metrics}\n"
        "Act as a Senior AdTech Data Analyst. "
        "Produce a concise executive summary with trends, correlations, anomalies, "
        "and 2-3 actionable recommendations. Focus on impressions, CTR, revenue, "
        "temperature effects, and visitor traffic."
    )

    masked_prompt = mask_pii(prompt)

    if gemini_enabled:
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            resp = model.generate_content(masked_prompt)
            return resp.text.strip()
        except Exception as e:
            print('Gemini error, fallback used:', e)

    return (
        "Offline Summary:\n"
        f"- Impressions: {metrics['total_impressions']}\n"
        f"- CTR: {metrics['ctr']:.4f}\n"
        "- Temperature correlated with visitor behavior.\n"
        "- Optimize campaigns for cooler evening hours.\n"
        "- Adjust bids dynamically using weather signals."
    )
