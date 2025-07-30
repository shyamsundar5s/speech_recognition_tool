import streamlit as st
from streamlit_speech_recognition import speech_to_text

# --- Page configuration ---
st.set_page_config(page_title="🎙️ Speech Recognition Tool", page_icon="🧠")

# --- Theme toggle ---
st.markdown("""
    <style>
    .stToggleSwitch label div[data-testid="stMarkdownContainer"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

theme = st.toggle("🌗 Toggle Dark Mode", key="theme_toggle")

# Apply light/dark background manually
if theme:
    st.markdown(
        """
        <style>
        body {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .stApp {
            background-color: #1e1e1e;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-color: #ffffff;
            color: #000000;
        }
        .stApp {
            background-color: #ffffff;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- App Title ---
st.title("🎙️ Speech Recognition Tool")
st.markdown("Try saying: **`hello`, `open`, `stop`, `exit`**")

# --- Speech Input Box ---
text_result = speech_to_text(
    placeholder="🎤 Click the mic and start speaking...",
    language="en-US",
    use_container_width=True
)

# --- Output ---
if text_result:
    st.success(f"You said: **{text_result.lower()}**")

