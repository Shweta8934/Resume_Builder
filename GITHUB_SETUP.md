# 🚀 GitHub Setup Guide

## ⚡ Quick Setup (After Git Installation)

Git has been installed! Please follow these steps to push your code to GitHub:

### 1. 🔄 **Restart Your Terminal**
- Close this PowerShell window
- Open a new PowerShell/Command Prompt window
- Navigate back to your project: `cd "C:\Users\sharm\Downloads\AIResumeBuilder-main"`

### 2. ✅ **Verify Git Installation**
```bash
git --version
```

### 3. 🔧 **Configure Git (First Time Setup)**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 4. 📁 **Initialize Repository**
```bash
git init
```

### 5. 📋 **Add All Files**
```bash
git add .
```

### 6. 💾 **Make First Commit**
```bash
git commit -m "Initial commit: AI Resume Builder with OpenRouter GPT-4o-mini"
```

### 7. 🌐 **Create GitHub Repository**
1. Go to [github.com](https://github.com)
2. Click "New" repository
3. Name it: `AIResumeBuilder` or `ai-resume-builder`
4. Don't initialize with README (we already have one)
5. Click "Create repository"

### 8. 🔗 **Link Local Repository to GitHub**
Replace `YOUR_USERNAME` with your GitHub username:
```bash
git remote add origin https://github.com/YOUR_USERNAME/AIResumeBuilder.git
git branch -M main
```

### 9. 🚀 **Push to GitHub**
```bash
git push -u origin main
```

## 🔐 **Authentication Options**

### Option A: Personal Access Token (Recommended)
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` permissions
3. Use token as password when prompted

### Option B: GitHub CLI
```bash
# Install GitHub CLI first
winget install --id GitHub.cli
# Then authenticate
gh auth login
```

## 📝 **Complete Command Sequence**
Once you restart your terminal, run these commands:

```bash
cd "C:\Users\sharm\Downloads\AIResumeBuilder-main"
git init
git add .
git commit -m "Initial commit: AI Resume Builder with OpenRouter GPT-4o-mini"
git remote add origin https://github.com/YOUR_USERNAME/AIResumeBuilder.git
git branch -M main
git push -u origin main
```

## 🎯 **Repository Structure**
Your GitHub repository will contain:
- ✅ Clean, organized codebase
- ✅ OpenRouter GPT-4o-mini integration
- ✅ Professional documentation
- ✅ .gitignore for security
- ✅ Setup instructions

## 🔒 **Security Notes**
- ✅ .env file is excluded from Git (contains API keys)
- ✅ Cache files are ignored
- ✅ Only essential files are tracked

## 🆘 **Troubleshooting**

### Git Not Found Error
- Restart terminal after installation
- Or use full path: `"C:\Program Files\Git\bin\git.exe"`

### Authentication Issues
- Use Personal Access Token instead of password
- Or install GitHub CLI for easier authentication

### Permission Errors
- Make sure you have write access to the repository
- Check if repository name already exists

## 🎉 **After Success**
Once pushed, your repository will be available at:
`https://github.com/YOUR_USERNAME/AIResumeBuilder`

You can then:
- Share your project with others
- Deploy to cloud platforms
- Collaborate with team members
- Track changes and versions
