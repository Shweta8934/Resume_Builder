# import streamlit as st
# from agents.resume_agent import resume_agent
# from agents.project_agent import project_agent
# from agents.cover_letter_agent import cover_letter_agent
# from utils.docx_builder import build_resume_docx, build_cover_letter_docx
# from utils.document_generator import fill_docx_template
# import json
# import os

# st.set_page_config(page_title="AveryBit Smart Resume Builder", layout="wide")

# st.markdown("""
#     <style>
#     .stApp {
#         max-width: 1200px;
#         margin: 0 auto;
#     }
#     .main .block-container {
#         padding-top: 2rem;
#         padding-bottom: 2rem;
#     }
#     h1 {
#         color: #1E88E5;
#         margin-bottom: 2rem;
#     }
#     h2 {
#         color: #424242;
#         margin-bottom: 1.5rem;
#     }
#     .stButton>button {
#         background-color: #1E88E5;
#         color: white;
#         border-radius: 4px;
#         padding: 0.5rem 1rem;
#     }
#     </style>
#     """, unsafe_allow_html=True)


# st.title("🧠 ResumeGenie by AveryBit")
# st.subheader("Powered by OpenRouter GPT-4o-mini - Craft the Perfect Resume & Cover Letter")



# # Load projects
# project_file = "data/projects.json"
# stored_projects = []
# if os.path.exists(project_file):
#     with open(project_file) as f:
#         try:
#             stored_projects = json.load(f)
#         except json.JSONDecodeError:
#             stored_projects = []

# if "edit_index" not in st.session_state:
#     st.session_state.edit_index = None

# # Sidebar project manager
# st.sidebar.header("📁 Project Viewer")
# if stored_projects:
#     for idx, p in enumerate(stored_projects):
#         with st.sidebar.expander(p['title']):
#             st.markdown(f"**Client:** {p.get('client', '-')}")
#             st.markdown(f"**Duration:** {p.get('duration', '-')}")
#             st.markdown(f"**URL:** [{p.get('url', '')}]({p.get('url', '')})")
#             st.markdown(f"**Description:** {p.get('description', '-')}")
#             if p.get("responsibilities"):
#                 st.markdown("**Responsibilities:**")
#                 for r in p["responsibilities"]:
#                     st.markdown(f"- {r}")
#             st.markdown(f"**Rating:** {'⭐' * int(p.get('rating', 0))}")
#             if p.get("technologies"):
#                 st.markdown(f"**Technologies Used:** {', '.join(p['technologies'])}")
#             col1, col2 = st.columns(2)
#             if col1.button("✏️ Edit", key=f"edit_{idx}"):
#                 st.session_state.edit_index = idx
#             if col2.button("🗑️ Delete", key=f"delete_{idx}"):
#                 del stored_projects[idx]
#                 with open(project_file, "w") as f:
#                     json.dump(stored_projects, f, indent=2)
#                 st.success("🗑️ Project deleted!")
#                 st.rerun()
# else:
#     st.sidebar.warning("No projects found.")

# # Sidebar: Add/Edit project
# with st.sidebar.form("Add or Edit Project"):
#     default = lambda key: stored_projects[st.session_state.edit_index].get(key, "") if st.session_state.edit_index is not None else ""

#     st.subheader("➕ Add/Edit Project")
#     new_title = st.text_input("Project Name", value=default("title"))
#     new_description = st.text_area("Project Description", value=default("description"))
#     new_client = st.text_input("Client Name", value=default("client"))
#     new_duration = st.text_input("Project Duration", value=default("duration"))
#     new_url = st.text_input("Project URL", value=default("url"))
#     new_responsibilities = st.text_area(
#         "Project Responsibilities (One per line)",
#         value="\n".join(default("responsibilities")) if default("responsibilities") else ""
#     )
#     rating = st.selectbox("⭐ Project Rating", list(range(1, 6)),
#                           format_func=lambda x: "⭐" * x,
#                           index=default("rating") - 1 if default("rating") else 0)
#     technologies = st.multiselect(
#         "🛠️ Technologies Used",
#         ["React Native", "Reactjs", "Nodejs", "Express js", "Mongodb", "Firebase", "Laravel", "Redux", "JavaScript", "TypeScript", "Sahha Health SDK", "React Navigation", "Axios", "Background Fetch API", "Mobile Health Tracking", "RESTful APIs", "Redux-Saga", "React Native Gesture Handler", "Custom UI Components", "WordPress", "ReactJS", "Node.js", "Express.js", "MongoDB",  "Scikit-learn",
#   "TensorFlow",
#   "PyTorch",
#   "XGBoost",
#   "Spark",
#   "Delta Lake",
#   "BigQuery",
#   "MLflow",
#   "AWS SageMaker",
#   "AWS EC2",
#   "AWS Lambda",
#   "AWS S3",
#   "Docker",
#   "Kubernetes",
#   "n8n",
#   "LangChain",
#   "Hugging Face Transformers",
#   "OpenAI API",
#   "AI Workflow Automation"],
#         default=default("technologies") if default("technologies") else []
#     )

#     if st.form_submit_button("💾 Save Project") and new_title and new_description:
#         updated_project = {
#             "title": new_title,
#             "description": new_description,
#             "client": new_client,
#             "duration": new_duration,
#             "url": new_url,
#             "responsibilities": new_responsibilities.strip().splitlines(),
#             "rating": rating,
#             "technologies": technologies
#         }

#         if st.session_state.edit_index is not None:
#             stored_projects[st.session_state.edit_index] = updated_project
#             st.session_state.edit_index = None
#             st.success("✅ Project updated!")
#         else:
#             stored_projects.append(updated_project)
#             st.success("✅ Project added!")

#         with open(project_file, "w") as f:
#             json.dump(stored_projects, f, indent=2)
#         st.rerun()

# # 👤 User input
# candidate_api = st.text_input("👤 Enter Your api").strip()
# candidate_name = st.text_input("👤 Enter Your Name").strip()
# candidate_tech = st.text_input("💻 Your Technology/Role").strip()
# candidate_exp = st.text_input("📅 Years of Experience").strip()
# required_skills = st.text_area("🧠 Enter Required Skills (comma-separated)", placeholder="e.g. ReactJS, React Native, Angular, VueJS", height=68)
# required_skills_list = [skill.strip() for skill in required_skills.split(",") if skill.strip()]
# jd_text = st.text_area("📄 Paste the Job Description (JD) here:", height=68)

# # 📁 Project filter + multiselect
# all_techs = sorted({tech for p in stored_projects for tech in p.get("technologies", [])})
# filter_techs = st.multiselect("🔍 Filter Projects by Technology", all_techs)
# filtered_projects = [p for p in stored_projects if any(t in p.get("technologies", []) for t in filter_techs)] if filter_techs else stored_projects
# filtered_projects = sorted(filtered_projects, key=lambda p: int(p.get("rating", 0)), reverse=True)

# project_titles = [f"{p['title']} {'⭐' * int(p.get('rating', 0))}" for p in filtered_projects]
# selected_project_titles = st.multiselect("📁 Select Projects to Include in Resume", project_titles)
# selected_projects = [p for p in filtered_projects if f"{p['title']} {'⭐' * int(p.get('rating', 0))}" in selected_project_titles]

# # 🚀 Resume Build Block
# if jd_text and candidate_name and candidate_tech and candidate_exp and selected_projects:
#     if st.button("🚀 Generate Resume & Cover Letter"):
#         with st.spinner("Analyzing JD and building resume..."):
#             resume_data = resume_agent(
#                 candidate_name,
#                 experience_level=candidate_exp,
#                 job_description=jd_text,
#                 projects_list=selected_projects,
#                 required_skills=required_skills_list
#             )
            
#             resume_data["skills"] = ", ".join(required_skills_list)

#             base_path = os.path.dirname(os.path.abspath(__file__))
#             template_path = os.path.join(base_path, "templates", "Resume_Template.docx")

#             if not os.path.exists(template_path):
#                 st.error("❌ Resume template file not found.")
#             else:
#                 docx_file = fill_docx_template(resume_data, template_name=template_path)
#                 cover_letter = cover_letter_agent(jd_text, resume_data)
#                 resume_docx = build_resume_docx(resume_data, selected_projects, template_path)
#                 cover_letter_docx = build_cover_letter_docx(cover_letter)

#                 st.success("✅ Resume and Cover Letter generated!")
#                 filename_prefix = f"{candidate_name}_{candidate_tech}_{candidate_exp}".replace(" ", "_")

#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.download_button("⬇️ Download Resume", data=docx_file, file_name=f"{filename_prefix}_resume_template.docx", use_container_width=True)
#                 with col2:
#                     st.download_button("⬇️ Download Cover Letter", data=cover_letter_docx, file_name=f"{filename_prefix}_cover_letter.docx", use_container_width=True)


import streamlit as st
from agents.resume_agent import resume_agent
from agents.project_agent import project_agent
from agents.cover_letter_agent import cover_letter_agent
from utils.docx_builder import build_resume_docx, build_cover_letter_docx
from utils.document_generator import fill_docx_template
import json
import os

st.set_page_config(page_title="AveryBit Smart Resume Builder", layout="wide")

st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        color: #1E88E5;
        margin-bottom: 2rem;
    }
    h2 {
        color: #424242;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        border-radius: 4px;
        padding: 0.5rem 1rem;
    }
    </style>
    """, unsafe_allow_html=True)


st.title("🧠 ResumeGenie by AveryBit")
st.subheader("Powered by OpenRouter GPT-4o-mini - Craft the Perfect Resume & Cover Letter")

# Load projects
project_file = "data/projects.json"
stored_projects = []
if os.path.exists(project_file):
    with open(project_file) as f:
        try:
            stored_projects = json.load(f)
        except json.JSONDecodeError:
            stored_projects = []

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

# Sidebar project manager
st.sidebar.header("📁 Project Viewer")
if stored_projects:
    for idx, p in enumerate(stored_projects):
        with st.sidebar.expander(p['title']):
            st.markdown(f"**Client:** {p.get('client', '-')}")
            st.markdown(f"**Duration:** {p.get('duration', '-')}")
            st.markdown(f"**URL:** [{p.get('url', '')}]({p.get('url', '')})")
            st.markdown(f"**Description:** {p.get('description', '-')}")
            if p.get("responsibilities"):
                st.markdown("**Responsibilities:**")
                for r in p["responsibilities"]:
                    st.markdown(f"- {r}")
            st.markdown(f"**Rating:** {'⭐' * int(p.get('rating', 0))}")
            if p.get("technologies"):
                st.markdown(f"**Technologies Used:** {', '.join(p['technologies'])}")
            col1, col2 = st.columns(2)
            if col1.button("✏️ Edit", key=f"edit_{idx}"):
                st.session_state.edit_index = idx
            if col2.button("🗑️ Delete", key=f"delete_{idx}"):
                del stored_projects[idx]
                with open(project_file, "w") as f:
                    json.dump(stored_projects, f, indent=2)
                st.success("🗑️ Project deleted!")
                st.rerun()
else:
    st.sidebar.warning("No projects found.")

# Sidebar: Add/Edit project
with st.sidebar.form("Add or Edit Project"):
    default = lambda key: stored_projects[st.session_state.edit_index].get(key, "") if st.session_state.edit_index is not None else ""

    st.subheader("➕ Add/Edit Project")
    new_title = st.text_input("Project Name", value=default("title"))
    new_description = st.text_area("Project Description", value=default("description"))
    new_client = st.text_input("Client Name", value=default("client"))
    new_duration = st.text_input("Project Duration", value=default("duration"))
    new_url = st.text_input("Project URL", value=default("url"))
    new_responsibilities = st.text_area(
        "Project Responsibilities (One per line)",
        value="\n".join(default("responsibilities")) if default("responsibilities") else ""
    )
    rating = st.selectbox("⭐ Project Rating", list(range(1, 6)),
                          format_func=lambda x: "⭐" * x,
                          index=default("rating") - 1 if default("rating") else 0)
    technologies = st.multiselect(
        "🛠️ Technologies Used",
        [
            "React Native", "Reactjs", "Nodejs", "Express js", "Mongodb", "Firebase", "Laravel", "Redux",
            "JavaScript", "TypeScript", "Sahha Health SDK", "React Navigation", "Axios", "Background Fetch API",
            "Mobile Health Tracking", "RESTful APIs", "Redux-Saga", "React Native Gesture Handler", "Custom UI Components",
            "WordPress", "ReactJS", "Node.js", "Express.js", "MongoDB", "Scikit-learn", "TensorFlow", "PyTorch",
            "XGBoost", "Spark", "Delta Lake", "BigQuery", "MLflow", "AWS SageMaker", "AWS EC2", "AWS Lambda",
            "AWS S3", "Docker", "Kubernetes", "n8n", "LangChain", "Hugging Face Transformers", "OpenAI API",
            "AI Workflow Automation"
        ],
        default=default("technologies") if default("technologies") else []
    )

    if st.form_submit_button("💾 Save Project") and new_title and new_description:
        updated_project = {
            "title": new_title,
            "description": new_description,
            "client": new_client,
            "duration": new_duration,
            "url": new_url,
            "responsibilities": new_responsibilities.strip().splitlines(),
            "rating": rating,
            "technologies": technologies
        }

        if st.session_state.edit_index is not None:
            stored_projects[st.session_state.edit_index] = updated_project
            st.session_state.edit_index = None
            st.success("✅ Project updated!")
        else:
            stored_projects.append(updated_project)
            st.success("✅ Project added!")

        with open(project_file, "w") as f:
            json.dump(stored_projects, f, indent=2)
        st.rerun()

# 👤 User input
candidate_api = st.text_input("🔑 Enter Your OpenRouter API Key").strip()
candidate_name = st.text_input("👤 Enter Your Name").strip()
candidate_tech = st.text_input("💻 Your Technology/Role").strip()
candidate_exp = st.text_input("📅 Years of Experience").strip()
required_skills = st.text_area("🧠 Enter Required Skills (comma-separated)", placeholder="e.g. ReactJS, React Native, Angular, VueJS", height=68)
required_skills_list = [skill.strip() for skill in required_skills.split(",") if skill.strip()]
jd_text = st.text_area("📄 Paste the Job Description (JD) here:", height=68)

# 📁 Project filter + multiselect
all_techs = sorted({tech for p in stored_projects for tech in p.get("technologies", [])})
filter_techs = st.multiselect("🔍 Filter Projects by Technology", all_techs)
filtered_projects = [p for p in stored_projects if any(t in p.get("technologies", []) for t in filter_techs)] if filter_techs else stored_projects
filtered_projects = sorted(filtered_projects, key=lambda p: int(p.get("rating", 0)), reverse=True)

project_titles = [f"{p['title']} {'⭐' * int(p.get('rating', 0))}" for p in filtered_projects]
selected_project_titles = st.multiselect("📁 Select Projects to Include in Resume", project_titles)
selected_projects = [p for p in filtered_projects if f"{p['title']} {'⭐' * int(p.get('rating', 0))}" in selected_project_titles]

# 🚀 Resume Build Block
if jd_text and candidate_name and candidate_tech and candidate_exp and selected_projects:
    if st.button("🚀 Generate Resume & Cover Letter"):
        with st.spinner("Analyzing JD and building resume..."):
            resume_data = resume_agent(
                candidate_name,
                experience_level=candidate_exp,
                job_description=jd_text,
                projects_list=selected_projects,
                required_skills=required_skills_list,
                api_key=candidate_api   # 🔑 pass API key here
            )
            
            if "error" in resume_data:
                st.error(resume_data["error"])
            else:
                resume_data["skills"] = ", ".join(required_skills_list)

                base_path = os.path.dirname(os.path.abspath(__file__))
                template_path = os.path.join(base_path, "templates", "Resume_Template.docx")

                if not os.path.exists(template_path):
                    st.error("❌ Resume template file not found.")
                else:
                    docx_file = fill_docx_template(resume_data, template_name=template_path)
                    cover_letter = cover_letter_agent(jd_text, resume_data)
                    resume_docx = build_resume_docx(resume_data, selected_projects, template_path)
                    cover_letter_docx = build_cover_letter_docx(cover_letter)

                    st.success("✅ Resume and Cover Letter generated!")
                    filename_prefix = f"{candidate_name}_{candidate_tech}_{candidate_exp}".replace(" ", "_")

                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button("⬇️ Download Resume", data=docx_file, file_name=f"{filename_prefix}_resume_template.docx", use_container_width=True)
                    with col2:
                        st.download_button("⬇️ Download Cover Letter", data=cover_letter_docx, file_name=f"{filename_prefix}_cover_letter.docx", use_container_width=True)
