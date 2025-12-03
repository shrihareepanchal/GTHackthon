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

def generate_summary(metrics: dict, anomalies: list) -> str:
    gemini_enabled = configure_gemini()

    prompt = (
        "Act as a Senior AdTech Performance Analyst.\n"
        "Generate a concise, client-ready executive summary using only the provided data.\n\n"
        f"METRICS:\n{metrics}\n\n"
        f"ANOMALIES:\n{anomalies}\n\n"
        "Your summary must include:\n"
        "- 3–4 key insights\n"
        "- 1 correlation insight (e.g., temperature vs visitors)\n"
        "- 2 actionable recommendations\n"
    )

    masked_prompt = mask_pii(prompt)

    if gemini_enabled:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(masked_prompt)
            return response.text.strip()
        except Exception:
            pass

    return (
        "Offline Summary:\n"
        f"- Total Impressions: {metrics.get('total_impressions')}\n"
        f"- CTR: {metrics.get('ctr')}\n"
        "- Temperature shows correlation with foot-traffic.\n"
        "- Several anomalies detected in impressions/revenue.\n"
        "- Optimize timing and creatives based on visitor behavior.\n"
    )
