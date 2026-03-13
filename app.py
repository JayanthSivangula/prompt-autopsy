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

# Custom CSS
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
    }
    .result-box {
        background-color: #1e2130;
        border-radius: 12px;
        padding: 20px;
        border-left: 4px solid #6c63ff;
        margin-top: 20px;
    }
    .score-card {
        background-color: #1e2130;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border: 1px solid #3d4466;
    }
    h1 { color: #6c63ff !important; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "library" not in st.session_state:
    st.session_state.library = []
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
if "last_result" not in st.session_state:
    st.session_state.last_result = None
if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = None

# Header
st.title("🩺 Prompt Autopsy Tool")
st.markdown("##### Diagnose why your AI prompt failed — and get a smarter version instantly")
st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔬 Diagnose", "💬 Chat Mode", "📦 Prompt Library", "💾 History"])

# ──────────────────────────────────────────────
# TAB 1 — DIAGNOSE
# ──────────────────────────────────────────────
with tab1:

    # Category selector
    st.markdown("### 🎯 Select Prompt Category")
    category = st.selectbox("", [
        "General",
        "Creative Writing",
        "Coding",
        "Business / Email",
        "Data Analysis",
        "Marketing / Copywriting",
        "Research / Summary",
        "Customer Support"
    ])

    category_tips = {
        "General": "Be clear, specific, and provide context.",
        "Creative Writing": "Specify tone, style, length, and audience.",
        "Coding": "Mention language, expected input/output, and any constraints.",
        "Business / Email": "Specify recipient, purpose, tone, and desired outcome.",
        "Data Analysis": "Mention data format, what insights you need, and output format.",
        "Marketing / Copywriting": "Include target audience, product benefits, and call to action.",
        "Research / Summary": "Specify source type, depth of summary, and key focus areas.",
        "Customer Support": "Include product context, customer issue, and desired resolution tone."
    }

    st.info(f"💡 **Tip for {category}:** {category_tips[category]}")

    # Language selector
    st.markdown("### 🌐 Output Language")
    language = st.selectbox("", [
        "English", "Hindi", "Spanish", "French",
        "German", "Japanese", "Chinese", "Arabic", "Telugu"
    ])

    st.markdown("---")

    # Input boxes
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("### 📝 Your Bad Prompt")
        bad_prompt = st.text_area("", height=180,
                                   placeholder="Paste your prompt here...",
                                   key="prompt")
    with col_right:
        st.markdown("### 📤 The Bad Output You Got")
        bad_output = st.text_area("", height=180,
                                   placeholder="Paste the bad output here...",
                                   key="output")

    diagnose_clicked = st.button("🔬 Diagnose My Prompt")

    # AI diagnosis function
    def diagnose_prompt(prompt, output, cat, lang):
        system_prompt = f"""
You are Prompt Autopsy AI — an expert at analyzing why AI prompts fail.
The user's prompt is in the category: {cat}
Please respond in: {lang}

User's Bad Prompt:
{prompt}

Bad Output Received:
{output}

Respond in this exact format:

## 🔍 Diagnosis
[What went wrong with the prompt]

## ❌ Why It Failed
[Explain why the output was bad]

## ✅ Fixed Prompt
[Write the improved prompt here]

## 💡 Improvements Made
[Explain what you changed and why]

## 🎯 Category-Specific Tips
[Give 2-3 tips specific to the {cat} category]

## 📊 Scores
Score the FIXED prompt you wrote above, not the original bad one.
Clarity: X/10
Specificity: X/10
Structure: X/10
Overall: X/10
"""
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You analyze prompts like a doctor. Be concise and helpful."},
                {"role": "user", "content": system_prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content

    # Score parser
    def parse_scores(result):
        scores = {"Clarity": 0, "Specificity": 0, "Structure": 0, "Overall": 0}
        for line in result.split("\n"):
            for key in scores:
                if key.lower() in line.lower():
                    try:
                        numbers = [int(s) for s in line.replace("/", " ").split() if s.isdigit()]
                        if numbers:
                            scores[key] = min(numbers[0], 10)
                    except:
                        pass
        return scores

    if diagnose_clicked:
        if bad_prompt and bad_output:
            with st.spinner("🔬 Analyzing your prompt DNA..."):
                result = diagnose_prompt(bad_prompt, bad_output, category, language)

            st.session_state.last_result = result
            st.session_state.last_prompt = bad_prompt
            st.session_state.chat_messages = []

            st.session_state.history.append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "prompt": bad_prompt,
                "category": category,
                "language": language,
                "result": result
            })

            st.success("✅ Diagnosis Complete!")
            st.markdown("---")

            # Result box
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(result)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("---")

            # Score dashboard
            st.markdown("## 📊 Score Dashboard")
            scores = parse_scores(result)
            c1, c2, c3, c4 = st.columns(4)
            for col, (label, score) in zip([c1, c2, c3, c4], scores.items()):
                color = "#48cfad" if score >= 7 else "#f7b731" if score >= 4 else "#fc5c65"
                col.markdown(f"""
                <div class="score-card">
                    <h2 style="color:{color}">{score}/10</h2>
                    <p style="color:#aaa">{label}</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("---")

            # Side by side
            st.markdown("## 📋 Side by Side Comparison")
            c1, c2 = st.columns(2)
            with c1:
                st.error("❌ Original Prompt")
                st.code(bad_prompt)
            with c2:
                st.success("✅ Fixed Prompt")
                st.info("See the Fixed Prompt section in the diagnosis above!")

            st.markdown("---")

            # Save to library button
            if st.button("📦 Save to Prompt Library"):
                st.session_state.library.append({
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "category": category,
                    "prompt": bad_prompt,
                    "result": result
                })
                st.success("✅ Saved to Prompt Library!")

            # Download report
            report = f"""PROMPT AUTOPSY REPORT
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Category: {category}
Language: {language}

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

# ──────────────────────────────────────────────
# TAB 2 — CHAT MODE
# ──────────────────────────────────────────────
with tab2:
    st.markdown("### 💬 Chat Mode — Refine Your Prompt Further")

    if st.session_state.last_result:
        st.info(f"💡 Chatting about: **{st.session_state.last_prompt[:60]}...**")

        for msg in st.session_state.chat_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        user_input = st.chat_input("Ask anything about your prompt diagnosis...")

        if user_input:
            st.session_state.chat_messages.append({"role": "user", "content": user_input})

            with st.chat_message("user"):
                st.markdown(user_input)

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    messages = [
                        {"role": "system", "content": f"You are Prompt Autopsy AI. The user's original prompt was: '{st.session_state.last_prompt}'. The diagnosis was: {st.session_state.last_result}. Help them refine and improve further."},
                    ] + st.session_state.chat_messages

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=messages,
                        temperature=0.3
                    )
                    reply = response.choices[0].message.content
                    st.markdown(reply)
                    st.session_state.chat_messages.append({"role": "assistant", "content": reply})
    else:
        st.warning("⚠️ Run a diagnosis first in the 🔬 Diagnose tab, then come back here to chat!")

# ──────────────────────────────────────────────
# TAB 3 — PROMPT LIBRARY
# ──────────────────────────────────────────────
with tab3:
    st.markdown("### 📦 Your Saved Prompt Library")

    if st.session_state.library:
        for i, item in enumerate(reversed(st.session_state.library)):
            with st.expander(f"📁 {item['time']} | {item['category']} | {item['prompt'][:50]}..."):
                st.markdown(item["result"])
                if st.button(f"🗑️ Delete", key=f"del_{i}"):
                    st.session_state.library.pop(len(st.session_state.library) - 1 - i)
                    st.rerun()
    else:
        st.info("No saved prompts yet! Run a diagnosis and click 'Save to Prompt Library'.")

# ──────────────────────────────────────────────
# TAB 4 — HISTORY
# ──────────────────────────────────────────────
with tab4:
    st.markdown("### 💾 Diagnosis History")

    if st.session_state.history:
        for i, item in enumerate(reversed(st.session_state.history)):
            with st.expander(f"🕐 {item['time']} | {item['category']} | {item['prompt'][:50]}..."):
                st.markdown(item["result"])
    else:
        st.info("No history yet! Run your first diagnosis in the 🔬 Diagnose tab.")

