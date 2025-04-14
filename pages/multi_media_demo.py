import streamlit as st
from datetime import datetime

# Custom page config
st.set_page_config(
    page_title="Multimedia Showcase",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for a sleek look
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
            border-radius: 10px;
        }
        .header {
            color: #4B8BBE;
        }
        .footer {
            margin-top: 50px;
            font-size: 0.8em;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎧📺 Multimedia Experience")
st.subheader("A deeper dive into Streamlit's media capabilities")

with st.expander("ℹ️ About this app", expanded=False):
    st.markdown("""
    This Streamlit app demonstrates embedding and interacting with video and audio media. 
    It also includes layout management, state handling, and conditional UI rendering.
    """)

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎬 Video Component")
    show_video = st.checkbox("Show video", value=True)
    if show_video:
        st.video("https://youtu.be/rQVUytARSuY")
    else:
        st.info("Toggle the checkbox to reveal the video.")

with col2:
    st.markdown("### 🎵 Audio Component")
    audio_volume = st.slider("Set audio volume (visual only)", 0, 100, 50)
    st.audio("https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/refs/heads/master/sample.mp3")

# Upload feature (bonus interaction)
st.markdown("### 📁 Upload Your Own Audio File")
uploaded_audio = st.file_uploader("Choose an audio file", type=["mp3", "wav", "ogg"])
if uploaded_audio is not None:
    st.success("Audio uploaded successfully!")
    st.audio(uploaded_audio, format="audio/mp3")

# Use of session state (to simulate an interaction)
if "played_times" not in st.session_state:
    st.session_state.played_times = 0

if st.button("📈 Simulate Media Interaction"):
    st.session_state.played_times += 1
    st.success(f"Interaction recorded! You've 'interacted' {st.session_state.played_times} times.")

# Footer
st.markdown("---")
st.markdown(f'<div class="footer">Page rendered at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</div>', unsafe_allow_html=True)
