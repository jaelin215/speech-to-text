import pandas as pd
import os
import torch
from TTS.api import TTS
import streamlit as st
import numpy as np

# Define available TTS models
available_models = {
    "Model A": TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC"),  # Update with actual model paths
    "Model B": TTS(model_name="tts_models/en/ljspeech/glow-tts"),
    # Add more models as needed
}

# Streamlit app
def main():
    st.title("Text-to-Speech Demo")

    # Model selection dropdown
    selected_model = st.selectbox("Select TTS Model", list(available_models.keys()))

    # Initialize the selected TTS model
    tts_model = available_models[selected_model]

    # User input for text
    text_input = st.text_area("Enter text:", "Hi there! How do you feel today?")

    # Button to generate speech
    if st.button("Generate Speech"):
        # Generate speech using the selected TTS model
        try:
            # speech, sample_rate = tts_model.tts(text_input)

            # Ensure the audio data is in WAV format
            wav_data = tts_model.tts_to_file(text=text_input)

            # Specify the sample rate in st.audio
            st.audio(wav_data, format="audio/wav")
        except Exception as e:
            st.error(f"Error generating speech: {str(e)}")

if __name__ == "__main__":
    main()