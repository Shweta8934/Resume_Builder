# # agents/resume_agent.py

# import os
# import json
# import requests
# from app import candidate_api  # Import the API key from app.py

# # 

# OPENROUTER_API_KEY = candidate_api
# print(f"Using API Key: {OPENROUTER_API_KEY}")
# OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# HEADERS = {
#     "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#     "Content-Type": "application/json",
#     "HTTP-Referer": "http://localhost:8502",
#     "X-Title": "AI Resume Builder"
# }


# def resume_agent(name, experience_level, job_description, projects_list, required_skills):
#     prompt = f"""
# You are a resume generation expert. Based on the candidate's details, required skills, job description, and selected projects, return a complete and clean JSON object. Do not include any explanation or markdown — only the raw JSON.

# Make sure to:
# - Categorize technologies under frontend, backend, databases, cloud, and tools
# - If a category is missing in the input, intelligently infer based on context
# - Fill all categories; no category should be empty if it's implied from required skills or job description

# Candidate Information:
# - Name: {name}
# - Experience: {experience_level} years
# - Required Skills: {', '.join(required_skills)}
# - Job Description: {job_description}

# Selected Projects (use in project_experience section):
# {json.dumps(projects_list)}

# Expected Output Format:
# {{
#   "name": "{name}",
#   "position_title": "Determine from job description, avoid 'Senior'/'Junior'",
#   "professional_summary": "Write 7-8 line summary of candidate's expertise based on the JD and skills.",
#   "professional_experience": {{
#     "years": "{experience_level}",
#     "description": "Generate 20-25 detailed bullet points with action verbs about candidate's responsibilities and technical knowledge."
#   }},
#   "technical_skills": {{
#     "frontend": ["React", "HTML", "CSS"],
#     "backend": ["Python", "Django", "Node.js"],
#     "databases": ["MongoDB", "PostgreSQL"],
#     "cloud": ["AWS", "Azure"],
#     "tools": ["Git", "Docker", "Jira"]
#   }},
#   "employment_history": [
#     {{
#       "company": "AveryBit Solutions Pvt. Ltd.",
#       "location": "Indore",
#       "positions": [
#         {{
#           "title": "Detect appropriate role title",
#           "duration": "Jan 2021 - Present",
#           "responsibilities": [
#             "List key contributions based on required skills and job role"
#           ]
#         }}
#       ]
#     }}
#   ],
#   "project_experience": {json.dumps(projects_list)}
# }}
# """


#     body = {
#         "model": "openai/gpt-4o-mini",
#         "messages": [
#             {"role": "user", "content": prompt}
#         ],
#         "temperature": 0.3,
#         "top_p": 0.9
#     }

#     try:
#         response = requests.post(OPENROUTER_API_URL, headers=HEADERS, json=body)
#         response.raise_for_status()
#         content = response.json()['choices'][0]['message']['content']
#         data = json.loads(content)
#         return data

#     except json.JSONDecodeError:
#         print("❌ AI response was not valid JSON:")
#         print(content)
#         return {"error": "Invalid JSON returned by AI"}

#     except Exception as e:
#         print(f"❌ API error: {str(e)}")
#         return {"error": str(e)}
import os
import json
import requests

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

def resume_agent(name, experience_level, job_description, projects_list, required_skills, api_key=None):
    """
    Generates structured resume data from job description, skills, and projects.
    """
    OPENROUTER_API_KEY = api_key or os.getenv("OPENROUTER_API_KEY")

    if not OPENROUTER_API_KEY:
        return {"error": "❌ Missing OpenRouter API key. Please provide it."}

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8502",
        "X-Title": "AI Resume Builder"
    }

    prompt = f"""
You are a resume generation expert. Based on the candidate's details, required skills, job description, and selected projects, return a complete and clean JSON object. Do not include any explanation or markdown — only the raw JSON.

Make sure to:
- Categorize technologies under frontend, backend, databases, cloud, and tools
- If a category is missing in the input, intelligently infer based on context
- Fill all categories; no category should be empty if it's implied from required skills or job description

Candidate Information:
- Name: {name}
- Experience: {experience_level} years
- Required Skills: {', '.join(required_skills)}
- Job Description: {job_description}

Selected Projects (use in project_experience section):
{json.dumps(projects_list)}

Expected Output Format:
{{
  "name": "{name}",
  "position_title": "Determine from job description, avoid 'Senior'/'Junior'",
  "professional_summary": "Write 7-8 line summary of candidate's expertise based on the JD and skills.",
  "professional_experience": {{
    "years": "{experience_level}",
    "description": "Generate 20-25 detailed bullet points with action verbs about candidate's responsibilities and technical knowledge."
  }},
  "technical_skills": {{
    "frontend": ["React", "HTML", "CSS"],
    "backend": ["Python", "Django", "Node.js"],
    "databases": ["MongoDB", "PostgreSQL"],
    "cloud": ["AWS", "Azure"],
    "tools": ["Git", "Docker", "Jira"]
  }},
  "employment_history": [
    {{
      "company": "AveryBit Solutions Pvt. Ltd.",
      "location": "Indore",
      "positions": [
        {{
          "title": "Detect appropriate role title",
          "duration": "Jan 2021 - Present",
          "responsibilities": [
            "List key contributions based on required skills and job role"
          ]
        }}
      ]
    }}
  ],
  "project_experience": {json.dumps(projects_list)}
}}
"""

    body = {
        "model": "openai/gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "top_p": 0.9
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=body)
        response.raise_for_status()
        content = response.json()['choices'][0]['message']['content']
        return json.loads(content)

    except json.JSONDecodeError:
        return {"error": "Invalid JSON returned by AI"}
    except Exception as e:
        return {"error": str(e)}
