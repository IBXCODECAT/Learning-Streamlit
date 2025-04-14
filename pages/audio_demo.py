import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Persistent Audio with Volume Control",
    page_icon="🎚️",
    layout="centered"
)

st.title("🔊 Persistent Audio Player with Live Volume Control")

# Audio + JS slider (all in HTML so nothing re-renders)
audio_player_html = """
<div style="text-align: center;">
    <audio id="myAudio" controls autoplay style="width: 100%;">
        <source src="https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/refs/heads/master/sample.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    <br/>
    <label for="volumeSlider">Volume: </label>
    <input type="range" id="volumeSlider" min="0" max="100" value="50" />
    <span id="volumeValue">50</span>%
</div>

<script>
    const audio = document.getElementById("myAudio");
    const slider = document.getElementById("volumeSlider");
    const label = document.getElementById("volumeValue");

    // Set initial volume
    audio.volume = slider.value / 100;

    // Listen for slider changes
    slider.addEventListener("input", function() {
        audio.volume = this.value / 100;
        label.textContent = this.value;
    });
</script>
"""

st.components.v1.html(audio_player_html, height=160)

# Extra features
with st.expander("ℹ️ What’s going on here?"):
    st.markdown("""
    - The audio player and volume slider are rendered using **raw HTML and JavaScript**.
    - This avoids re-renders, so the audio keeps playing even when the slider changes.
    - We’re using the **browser’s native DOM** to control the volume.
    """)

# Footer
st.markdown("---")
st.caption(f"Rendered at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
