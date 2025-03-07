# the-best
# Meeting Transcript and Summary Generator using Generative AI

This project uses Python, *Speech Recognition, **PyDub, and **Transformers* to transcribe meeting audio and generate a summary of the meeting using AI. The code leverages *Google's Speech-to-Text* for transcription and *Facebook's BART* model for summarization.

## Features
- *Transcribe Audio*: Convert audio files to text, supporting various audio formats (e.g., MP3, WAV).
- *Summarize Text*: Generate summaries of transcriptions using the BART model.
- *GUI with Tkinter*: The project also features a basic graphical user interface (GUI) built using Tkinter.

## Requirements

Before running the project, you need to install the following dependencies:

1. *SpeechRecognition*: For converting speech to text.
2. *pydub*: For audio file conversion (e.g., MP3 to WAV).
3. *transformers*: For generating summaries using a pre-trained model.
4. *tkinter*: For creating a GUI.

To install the dependencies, run the following command:

'''bash
pip install SpeechRecognition pydub transformers tkinter

/your_project_directory
│
├── final.py          # Main Python file with transcription and summarization functions
├── transcription.txt     # Transcription output file
├── summary.py        # Summary output file
├── summary.txt      # summary file generated after rendering
└── README.md             # Project description

*Usage*
--Transcribe Audio: The script will take an audio file (WAV or any supported format) and transcribe it into text.
--Summarize Transcription: After transcription, the script will summarize the transcribed text into a shorter version.

1.*Transcribe Audio:*

-The transcribe_audio() function will accept an audio file and transcribe the audio to a text file.

transcription = transcribe_audio("your_audio_file.wav")

-It will save the transcription into a file named transcription.txt.

2.*Summarize Transcription:*

-After transcription, the summarize_text() function will summarize the text from transcription.txt and save the summary in summary.txt.


summary = summarize_text()

-The generated summary will be saved in a file named summary.txt.

3. ** Sample File example**
file_path = "WhatsappAudio-2025.wav"

# Step 1: Transcribe audio
transcription = transcribe_audio(file_path)

# Step 2: Summarize text if transcription is successful
if transcription:
    summarize_text()

*How to Use the GUI*
1.Run the Python script that includes the Tkinter code.
2.Use the graphical interface to choose an audio file and click the "Transcribe" button.
3.After transcription, click the "Summarize" button to get a summary.

*Notes*
-File Formats: This project works best with WAV files, but the PyDub library is used to convert other formats (e.g., MP3) to WAV.
-Audio Quality: The transcription accuracy depends on the quality of the audio file.
-Summary Length: The generated summary will be between 50 and 150 characters, as specified in the summarizer function.

*Troubleshooting*
-No Audio Output: Ensure that the audio file is correctly loaded and that your microphone permissions are properly set (if using live audio capture).
-Error during Summarization: Check the input transcription file to ensure it contains valid text and isn't empty.
