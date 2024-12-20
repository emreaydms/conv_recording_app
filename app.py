import streamlit as st
import transformers
from transformers import pipeline

# ------------------------------
# Load Whisper Model
# ------------------------------
def load_whisper_model():
    """
    Load the Whisper model for audio transcription.
    """
    asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")
    return asr_pipeline


# ------------------------------
# Load NER Model
# ------------------------------
def load_ner_model():
    """
    Load the Named Entity Recognition (NER) model pipeline.
    """
    ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
    return ner_pipeline


# ------------------------------
# Transcription Logic
# ------------------------------
def transcribe_audio(uploaded_file):
    """
    Transcribe audio into text using the Whisper model.
    Args:
        uploaded_file: Audio file uploaded by the user.
    Returns:
        str: Transcribed text from the audio file.
    """
    model = load_whisper_model()
    transcription = model(uploaded_file)
    return transcription["text"]


# ------------------------------
# Entity Extraction
# ------------------------------
def extract_entities(text, ner_pipeline):
    """
    Extract entities from transcribed text using the NER model.
    Args:
        text (str): Transcribed text.
        ner_pipeline: NER pipeline loaded from Hugging Face.
    Returns:
        dict: Grouped entities (ORGs, LOCs, PERs).
    """
    entities = ner_pipeline(text)
    grouped_entities = {"ORGs": [], "LOCs": [], "PERs": []}

    for entity in entities:
        if entity["entity_group"] == "ORG":
            grouped_entities["ORGs"].append(entity["word"])
        elif entity["entity_group"] == "LOC":
            grouped_entities["LOCs"].append(entity["word"])
        elif entity["entity_group"] == "PER":
            grouped_entities["PERs"].append(entity["word"])

    for key in grouped_entities:
        grouped_entities[key] = list(set(grouped_entities[key]))

    return grouped_entities


# ------------------------------
# Main Streamlit Application
# ------------------------------
def main():
    st.title("Meeting Transcription and Entity Extraction")

    # Replace placeholders with your Name and Student ID
    STUDENT_NAME = "Emre Aydogmus"
    STUDENT_ID = "150220323"
    st.write(f"**{STUDENT_ID} - {STUDENT_NAME}**")

    # File upload section
    uploaded_file = st.file_uploader("Upload a business meeting audio file:", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.info("Transcribing the audio file... This may take a minute.")
        transcription = transcribe_audio(uploaded_file.getvalue())

        st.subheader("Transcription:")
        st.write(transcription)

        st.info("Extracting entities...")
        ner_pipeline = load_ner_model()
        grouped_entities = extract_entities(transcription, ner_pipeline)

        st.subheader("Extracted Entities:")
        st.markdown("### Organizations (ORGs):")
        st.write(grouped_entities["ORGs"])

        st.markdown("### Locations (LOCs):")
        st.write(grouped_entities["LOCs"])

        st.markdown("### Persons (PERs):")
        st.write(grouped_entities["PERs"])

if __name__ == "__main__":
    main()
