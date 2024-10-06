import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv(".env")

# Set Google Generative AI API key as an environment variable
API_KEY = "AIzaSyB-j27MWcc1BIzIGFNwAT9GSgK-qZhOVSE"

# Initialize Google Generative AI client
genai.configure(api_key=API_KEY)

st.title("Gemini 1.5 Pro ChatBot")

API_KEY_INPUT = st.text_input("Enter your Google Generative AI API key:")

if "genai_model" not in st.session_state:
  st.session_state["genai_model"] = "gemini-1.5-pro"

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""
    model = genai.GenerativeModel(st.session_state["genai_model"])
    response = model.generate_content(prompt)
    full_response += response.parts[0].text
    message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
  st.session_state.messages.append({"role": "assistant", "content": full_response})