import streamlit as st
import google.generativeai as genai
import os

# Configure the API key (Streamlit Cloud will load it securely)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

st.title("🌍 Gemini Climate Chatbot")
prompt = st.text_input("Ask something about climate:")

if prompt:
    with st.spinner("Thinking..."):
        response = model.generate_content(prompt)

        st.write("🤖", response.text)


