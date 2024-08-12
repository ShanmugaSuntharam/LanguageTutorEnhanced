import streamlit as st
import wave

from audio_recorder_streamlit import audio_recorder

#st.subheader("Base audio recorder")
#base_audio_bytes = audio_recorder(key="base")
#if base_audio_bytes:
#    st.audio(base_audio_bytes, format="audio/wav")

#st.subheader("Custom recorder")
#custom_audio_bytes = audio_recorder(
#    text="",
#    recording_color="#e8b62c",
#    neutral_color="#6aa36f",
#    icon_name="user",
#    icon_size="6x",
#    sample_rate=41_000,
#    key="custom",
#)
#st.text("Click to record")
#if custom_audio_bytes:
#    st.audio(custom_audio_bytes, format="audio/wav")

def app():
    st.subheader("Fixed length recorder")
    fixed_audio_bytes = audio_recorder(
        energy_threshold=(-1.0, 1.0),
        pause_threshold=10.0,
        key="fixed",
    )
    st.text("Click to record 10 seconds")
    if fixed_audio_bytes:
        #st.audio(fixed_audio_bytes, format="audio/wav")
    
        sample_rate = 44100  # Sample rate in Hz

        # Save as WAV file
        output_file = "output_from_new_lib.wav"
        with wave.open(output_file, 'w') as wf:
            wf.setnchannels(2)  # Stereo
            wf.setsampwidth(2)  # Sample width in bytes
            wf.setframerate(sample_rate)
            #wf.writeframes(audio_data.tobytes())
            wf.writeframes(fixed_audio_bytes)

    #print(f"Audio saved to {output_file}")