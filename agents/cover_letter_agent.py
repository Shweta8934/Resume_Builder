import os, requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:8502",
    "X-Title": "AI Resume Builder"
}

def call_openrouter(prompt: str):
    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 1024
    }
    try:
        res = requests.post(OPENROUTER_API_URL, headers=HEADERS, json=payload)
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return str(e)

def cover_letter_agent(jd_text, resume_data):
    prompt = f"""
    Write a concise cover letter for this job:
    {jd_text}

    Candidate Summary:
    
    {resume_data.get('summary') or resume_data.get('professional_summary', '')}

    Limit to 200 words. Personal, confident, relevant.
    """
    return call_openrouter(prompt)
