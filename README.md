# AIResumeBuilder - Powered by OpenRouter GPT-4o-mini

🧠 **Intelligent Resume & Cover Letter Generator**

AIResumeBuilder is an AI-powered Streamlit application that creates tailored resumes and cover letters based on job descriptions. Now powered by OpenRouter's GPT-4o-mini for cost-effective, high-quality AI generation.

## ✨ Features

- 🤖 **AI-Powered Content Generation** using OpenRouter GPT-4o-mini
- 📁 **Project Portfolio Management** with ratings and technology tags
- 🎯 **Smart Project Matching** based on job requirements
- 📄 **Professional Document Export** in DOCX format
- 🔍 **Technology Filtering** for project selection
- 💼 **Cover Letter Generation** tailored to job descriptions

## 🚀 Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure OpenRouter API**:
   - Get your API key from [openrouter.ai](https://openrouter.ai)
   - Update `.env` file with your key:
     ```
     OPENROUTER_API_KEY="your-api-key-here"
     ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

4. **Access**: Open your browser to `http://localhost:8502`

## 📖 Usage

1. **Add Projects**: Use the sidebar to manage your project portfolio
2. **Enter Details**: Fill in your personal information and skills
3. **Paste Job Description**: Add the target job posting
4. **Select Projects**: Choose relevant projects to highlight
5. **Generate**: Let AI create tailored resume and cover letter
6. **Download**: Get professional DOCX documents

## 💰 Cost-Effective AI

Now using OpenRouter GPT-4o-mini:
- ⚡ **Fast Generation**: Quick response times
- 💸 **Affordable**: ~$0.15/$0.60 per 1M input/output tokens
- 🎯 **High Quality**: GPT-4 level performance
- 🔄 **Reliable**: Stable API with good uptime

## 📋 Requirements

- Python 3.11+
- Streamlit
- OpenRouter API key
- See `requirements.txt` for full dependencies

## 🔧 Technical Stack

- **Frontend**: Streamlit
- **AI Engine**: OpenRouter GPT-4o-mini
- **Document Processing**: python-docx
- **Data Storage**: JSON files
- **Project Matching**: Custom keyword-based algorithm

For detailed setup instructions, see `SETUP_OPENROUTER.md`.
