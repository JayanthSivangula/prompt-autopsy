# 🩺 Prompt Autopsy Tool

> **Diagnose why your AI prompt failed — and get a smarter version instantly.**

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-F55036?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-48cfad?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

---

```
  ██████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ████████╗
  ██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝
  ██████╔╝██████╔╝██║   ██║██╔████╔██║██████╔╝   ██║   
  ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝    ██║   
  ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║        ██║   
  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝   
                    A U T O P S Y
```

---

## 🔍 What Is This?

**Prompt Autopsy** is an AI-powered web app that acts like a doctor for your broken AI prompts.

You paste a bad prompt + the bad output you got → It diagnoses what went wrong, rewrites the prompt, scores it, and explains exactly what to fix. Built with **Streamlit + Groq (LLaMA 3.3)**, deployed live on the internet.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔬 **AI Diagnosis** | Analyzes why your prompt failed and what went wrong |
| ✅ **Auto-Fix** | Rewrites your prompt into a high-quality improved version |
| 📊 **Score Dashboard** | Rates Clarity, Specificity, Structure & Overall out of 10 |
| 🎯 **8 Prompt Categories** | Tailored tips for Coding, Writing, Business, Marketing & more |
| 🌐 **9 Languages** | Get diagnosis in English, Hindi, Telugu, Spanish, French & more |
| 💬 **Chat Mode** | Have a back-and-forth conversation to refine your prompt further |
| 📦 **Prompt Library** | Save your best fixed prompts for future reference |
| 💾 **History** | Every diagnosis is saved in your session history |
| 📄 **Download Report** | Export your full diagnosis as a `.txt` file |

---

## 🚀 Live Demo

🌍 **Try it here →** [prompt-autopsy.streamlit.app](https://prompt-autopsy-h4jaauftrpccws8bjcvg6u.streamlit.app/)

---

## 🛠️ Tech Stack

```
Frontend      →  Streamlit (Python)
AI Model      →  LLaMA 3.3 70B via Groq API (Free)
Auth/Secrets  →  python-dotenv
Deployment    →  Streamlit Cloud
Version Ctrl  →  GitHub
```

---

## ⚡ Quick Start (Run Locally)

### 1. Clone the repo
```bash
git clone https://github.com/JayanthSivangula/prompt-autopsy.git
cd prompt-autopsy
```

### 2. Install dependencies
```bash
pip install streamlit groq python-dotenv
```

### 3. Set up your API key
Create a `.env` file in the project folder:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get a free Groq API key at → [console.groq.com](https://console.groq.com)

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📁 Project Structure

```
prompt-autopsy/
│
├── app.py              ← Main application file
├── .env                ← Your secret API key (never commit this!)
├── .gitignore          ← Tells Git to ignore .env
├── requirements.txt    ← Python dependencies
└── README.md           ← You are here!
```

---

## 🎮 How to Use

```
Step 1 → Select your prompt category (Coding, Writing, etc.)
Step 2 → Choose your output language
Step 3 → Paste your bad prompt
Step 4 → Paste the bad output you received
Step 5 → Click 🔬 Diagnose My Prompt
Step 6 → Read the diagnosis, check your scores
Step 7 → Use Chat Mode to refine further
Step 8 → Save to library or download report
```

---

## 📸 App Preview

```
┌─────────────────────────────────────────────────┐
│  🩺 Prompt Autopsy Tool                         │
│  ─────────────────────────────────────────────  │
│  🔬 Diagnose  💬 Chat  📦 Library  💾 History   │
│  ─────────────────────────────────────────────  │
│  🎯 Category: [General ▼]                       │
│  🌐 Language: [English ▼]                       │
│                                                 │
│  📝 Bad Prompt    │   📤 Bad Output             │
│  ───────────────  │   ─────────────────         │
│  Write about AI   │   AI is technology...       │
│                                                 │
│       [ 🔬 Diagnose My Prompt ]                 │
│                                                 │
│  📊 Score Dashboard                             │
│  ┌────────┬──────────────┬──────────┬────────┐  │
│  │ 9/10   │    9/10      │  8/10    │  9/10  │  │
│  │Clarity │ Specificity  │Structure │Overall │  │
│  └────────┴──────────────┴──────────┴────────┘  │
└─────────────────────────────────────────────────┘
```

---

## 🌐 Supported Languages

`English` `Hindi` `Telugu` `Spanish` `French` `German` `Japanese` `Chinese` `Arabic`

---

## 🎯 Prompt Categories

`General` `Creative Writing` `Coding` `Business / Email` `Data Analysis` `Marketing / Copywriting` `Research / Summary` `Customer Support`

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Built By

**Jayanth Sivangula**

Built from scratch in a single session — Python, Streamlit, Groq API, GitHub, and Streamlit Cloud.

[![GitHub](https://img.shields.io/badge/GitHub-JayanthSivangula-181717?style=for-the-badge&logo=github)](https://github.com/JayanthSivangula)

---

## 📜 License

This project is licensed under the MIT License — feel free to use, modify , and share!

---

<div align="center">

**If this helped you, give it a ⭐ on GitHub!**

*Built with 🩺 and a lot of bad prompts*

</div>
