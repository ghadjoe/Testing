import streamlit as st
from openai import OpenAI
import os

# Set your OpenAI API key securely
# You can also set this as an environment variable for better security
openai_api_key = os.getenv("OPENAI_API_KEY") or "sk-..."  # Replace with your actual key if not using env var

# Streamlit UI setup
st.set_page_config(page_title="Impact Artist GPT", layout="wide")
st.title("🎨 Impact Artist Program Assistant")
st.markdown("""
Ask a question or upload a meeting transcript and get AI-generated insights for your Ads Team.
""")

# User input
user_input = st.text_area("Enter your question or context")

# Submit button
if st.button("Generate Insights") and user_input:
    client = OpenAI(api_key=openai_api_key)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that analyzes internal communications and provides actionable insights to advertising teams."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.7,
        max_tokens=2048
    )

    # Output
    st.subheader("🧠 Insights for the Ads Team")
    st.write(response.choices[0].message.content)

# Optional: File upload (future extension)
# uploaded_file = st.file_uploader("Upload a meeting transcript", type=["txt", "pdf"])
# If uploaded_file:
#     ... (parse and analyze file content)
