import streamlit as st
from audio_utils import record_audio_to_file
from transcribe_utils import transcribe
from ai_utils import generate_answer

st.title("🎙️ Live Meeting AI Assistant")

if st.button("Start Listening"):
    st.info("Recording for 5 seconds...")
    audio_file = record_audio_to_file()

    st.success("Recording complete!")
    user_input = transcribe(audio_file)

    st.markdown(f"**Heard:** {user_input}")

    if user_input.strip():
        # Send any input to GPT-4, not just questions
        response = generate_answer(user_input)
        st.markdown(f"**💬 Response:** {response}")
    else:
        st.warning("Could not recognize any speech.")
