import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from datetime import datetime

# Load your secret API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page setup
st.set_page_config(page_title="Prompt Autopsy", page_icon="🩺", layout="wide")

# Custom CSS for beautiful UI
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stTextArea textarea {
        background-color: #1e2130;
        color: #ffffff;
        border-radius: 10px;
        border: 1px solid #3d4466;
        font-size: 15px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6c63ff, #48cfad);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 40px;
        border: none;
        width: 100%;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #48cfad, #6c63ff);
        transform: scale(1.02);
    }
    .result-box {
        background-color: #1e2130;
        border-radius: 12px;
        padding: 20px;
        border-left: 4px solid #6c63ff;
        margin-top: 20px;
    }
    .score-box {
        background-color: #1e2130;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        border: 1px solid #3d4466;
    }
    h1 { color: #6c63ff !important; }
    .template-btn>button {
        background-color: #1e2130 !important;
        color: #6c63ff !important;
        border: 1px solid #6c63ff !important;
        border-radius: 8px !important;
        font-size: 13px !important;
        padding: 5px 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🩺 Prompt Autopsy Tool")
st.markdown("##### Diagnose why your AI prompt failed — and get a smarter version instantly")
st.markdown("---")

# Prompt Templates
st.markdown("### 📋 Quick Templates — Click to Auto-Fill")
col1, col2, col3, col4 = st.columns(4)

templates = {
    "✍️ Essay": ("Write an essay", "Here is an essay about the topic."),
    "💻 Code": ("Write code", "Here is some code."),
    "📧 Email": ("Write an email", "Hi, I am writing to you about this matter."),
    "📱 Social": ("Write a social media post", "Check this out!")
}

selected_template = None
with col1:
    if st.button("✍️ Essay"):
        selected_template = "✍️ Essay"
with col2:
    if st.button("💻 Code"):
        selected_template = "💻 Code"
with col3:
    if st.button("📧 Email"):
        selected_template = "📧 Email"
with col4:
    if st.button("📱 Social"):
        selected_template = "📱 Social"

# Set default values
default_prompt = templates[selected_template][0] if selected_template else ""
default_output = templates[selected_template][1] if selected_template else ""

st.markdown("---")

# Input section
col_left, col_right = st.columns(2)
with col_left:
    st.markdown("### 📝 Your Bad Prompt")
    bad_prompt = st.text_area("", height=180, placeholder="Paste your prompt here...", value=default_prompt, key="prompt")

with col_right:
    st.markdown("### 📤 The Bad Output You Got")
    bad_output = st.text_area("", height=180, placeholder="Paste the bad output here...", value=default_output, key="output")

# Diagnose button
st.markdown("###")
diagnose_clicked = st.button("🔬 Diagnose My Prompt")

# AI diagnosis function
def diagnose_prompt(prompt, output):
    system_prompt = f"""
You are Prompt Autopsy AI — an expert at analyzing why AI prompts fail.

User's Bad Prompt:
{prompt}

Bad Output Received:
{output}

Please respond in this exact format:

## 🔍 Diagnosis
[What went wrong with the prompt]

## ❌ Why It Failed
[Explain why the output was bad]

## ✅ Fixed Prompt
[Write the improved prompt here]

## 💡 Improvements Made
[Explain what you changed and why]

## 📊 Scores
- Clarity: X/10
- Specificity: X/10
- Structure: X/10
- Overall: X/10
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You analyze prompts like a doctor performs an autopsy. Be concise and helpful."},
            {"role": "user", "content": system_prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

# History storage
if "history" not in st.session_state:
    st.session_state.history = []

# Run diagnosis
if diagnose_clicked:
    if bad_prompt and bad_output:
        with st.spinner("🔬 Analyzing your prompt DNA..."):
            result = diagnose_prompt(bad_prompt, bad_output)

        # Save to history
        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "prompt": bad_prompt,
            "result": result
        })

        st.success("✅ Diagnosis Complete!")
        st.markdown("---")

        # Show result
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(result)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")

        # Side by side
        st.markdown("## 📊 Side by Side Comparison")
        c1, c2 = st.columns(2)
        with c1:
            st.error("❌ Original Prompt")
            st.code(bad_prompt)
        with c2:
            st.success("✅ Fixed Prompt")
            st.info("See the Fixed Prompt section in the diagnosis above!")

        # Download report
        st.markdown("---")
        report = f"""PROMPT AUTOPSY REPORT
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

ORIGINAL PROMPT:
{bad_prompt}

ORIGINAL OUTPUT:
{bad_output}

DIAGNOSIS:
{result}
"""
        st.download_button(
            label="📄 Download Report as TXT",
            data=report,
            file_name=f"prompt_autopsy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

    else:
        st.warning("⚠️ Please fill in both boxes first!")

# Prompt History
if st.session_state.history:
    st.markdown("---")
    st.markdown("## 💾 Prompt History")
    for i, item in enumerate(reversed(st.session_state.history)):
        with st.expander(f"🕐 {item['time']} — {item['prompt'][:50]}..."):
            st.markdown(item["result"])