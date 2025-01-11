# Conversational Transcript Analysis using GenAI

This project, developed as part of the YZV 211E course, focuses on creating a Streamlit application for processing conversational transcripts. The application uses state-of-the-art machine learning models to transform audio recordings into structured, educational transcripts, extracting key entities such as Persons, Organizations, and Locations. This README provides an overview of the project, its features, and instructions for use.
App link: https://150220323yzv211hw3.streamlit.app/

## Features

1. **Audio Transcription**:
   - Utilizes the Hugging Face `openai/whisper-tiny` model to transcribe audio files into text.
   - Supports WAV file uploads for transcription.

2. **Named Entity Recognition (NER)**:
   - Implements the Hugging Face `dslim/bert-base-NER` model to extract named entities from the transcribed text.
   - Identifies and groups entities into:
     - **Persons (PERs)**
     - **Organizations (ORGs)**
     - **Locations (LOCs)**
   - Duplicates are removed for clarity.

3. **Streamlit Web App**:
   - An interactive interface for users to upload audio files and view the transcription and extracted entities.
   - Includes the developer’s name and student ID for proper attribution.

4. **Deployment**:
   - Hosted on Streamlit Cloud for easy access.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.9+ and pip installed. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application Locally**:
   ```bash
   streamlit run app.py
   ```

## How to Use

1. Upload an audio file in WAV format using the file uploader in the application.
2. View the transcription of the uploaded audio.
3. Review the extracted entities grouped by category (Persons, Organizations, Locations).

## Example Output

- **Transcription**:
  - "This is an example transcription of an audio meeting."

- **Extracted Entities**:
  - **Persons (PERs):** John Doe, Alice Smith
  - **Organizations (ORGs):** OpenAI, ITU
  - **Locations (LOCs):** Istanbul, San Francisco

## Notes

- This project was created for educational purposes as part of the YZV 211E course.
- Adheres to the ethical guidelines provided by ITU.

## Acknowledgments

- Course Instructor: Res. Asst. Yaren Yılmaz
- Models: Hugging Face (Whisper and NER)
- Framework: Streamlit

## License

This project is licensed under the MIT License. See the LICENSE file for details.
