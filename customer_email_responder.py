import streamlit as st
import subprocess
import time
from datetime import datetime
import csv
from pathlib import Path
import pandas as pd

# --- App Config ---
st.set_page_config(
    page_title="AI Customer Email Responder",
    page_icon="📨",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        .main {background-color: #f9f9f9;}
        h1 {color: #4CAF50;}
        .stTextArea textarea {background-color: #fff5e6;}
        .footer {font-size: 12px; color: #888; margin-top: 50px;}
    </style>
""", unsafe_allow_html=True)

# --- Title and Intro ---
st.title("📨 AI Customer Email Responder")
st.markdown("""
This app helps you craft thoughtful, tone-appropriate responses to customer emails using a locally hosted AI model.

🧠 Powered by TinyLLaMA running locally via [Ollama](https://ollama.com)
""")

# --- Sidebar ---
st.sidebar.header("Customization")
tone = st.sidebar.radio("Select the tone of your response:", ["Friendly", "Formal", "Concise"])
date = datetime.now().strftime("%A, %B %d, %Y")
st.sidebar.markdown(f"_Today's date: {date}_")

# --- Email Input ---
st.subheader("Step 1: Paste Customer Email")
email_input = st.text_area("Customer Email:", height=200, placeholder="Paste the email from the customer here...")

# --- Generate Button ---
submit = st.button("✉️ Generate AI Response")

# --- File for saving responses ---
log_file = Path("email_response_log.csv")
if not log_file.exists():
    with open(log_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Tone", "Customer Email", "AI Response"])

# --- Response Generation ---
if submit and email_input:
    with st.spinner("Thinking..."):
        time.sleep(0.5)  # slight pause for effect
        prompt = f"""
        You are a helpful customer support agent. Respond to the following email in a {tone.lower()} tone.

        Customer email:
        {email_input}

        Your reply:
        """
        result = subprocess.run(
            ["ollama", "run", "tinyllama", prompt],
            capture_output=True,
            text=True
        )

        ai_reply = result.stdout.strip()

        st.subheader("✅ Suggested Reply")
        st.markdown(f"""
        <div style='background-color: #e8f5e9; padding: 15px; border-radius: 8px; border: 1px solid #c8e6c9;'>
            <pre style='white-space: pre-wrap; word-wrap: break-word;'>{ai_reply}</pre>
        </div>
        """, unsafe_allow_html=True)

        # --- Save to CSV ---
        with open(log_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().isoformat(), tone, email_input, ai_reply])

# --- Log Viewer ---
st.subheader("📂 View Past Responses")
if log_file.exists():
    df = pd.read_csv(log_file)
    if not df.empty:
        st.dataframe(df)
        st.download_button(
            label="Download Response Log",
            data=log_file.read_bytes(),
            file_name="email_response_log.csv",
            mime="text/csv"
        )
    else:
        st.info("No past responses saved yet.")
else:
    st.warning("Response log file not found.")

# --- Footer ---
st.markdown("""
<div class='footer'>
    Using TinyLLaMA via Ollama · Interface: Streamlit · 100% Local & Free
</div>
""", unsafe_allow_html=True)
