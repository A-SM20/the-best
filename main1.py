import speech_recognition as sr
from pydub import AudioSegment
from transformers import pipeline

def transcribe_audio(file_path, output_file="transcription.txt"):
    recognizer = sr.Recognizer()

    # Convert to WAV if needed
    if not file_path.endswith(".wav"):
        audio = AudioSegment.from_file(file_path)
        converted_file = file_path.rsplit(".", 1)[0] + ".wav"  # Change extension to .wav
        audio.export(converted_file, format="wav")
    else:
        converted_file = file_path

    # Load the audio file
    with sr.AudioFile(converted_file) as source:
        audio_data = recognizer.record(source)

    # Transcribe the audio
    try:
        text = recognizer.recognize_google(audio_data)
        print("🎙 Transcription:", text)

        # Save transcription to a file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"✅ Transcription saved to {output_file}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return None
    except sr.RequestError:
        print("❌ Could not request results. Check your internet connection.")
        return None

def summarize_text(input_file="transcription.txt", output_file="summary.txt"):
    # Load the pre-trained summarization model
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Read the meeting transcript from the input file
    with open(input_file, "r", encoding="utf-8") as file:
        conversation = file.read().strip()

    # Handle empty file case
    if not conversation:
        print("❌ Error: The input file is empty.")
        return None

    # Generate summary
    summary = summarizer(conversation, max_length=150, min_length=50, do_sample=False)

    # Write the summary to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(summary[0]['summary_text'])

    print(f"✅ Meeting summary saved to {output_file}")
    return summary[0]['summary_text']

# Example usage
file_path = r"OSR_us_000_0015_8k.wav"

# Step 1: Transcribe audio
transcription = transcribe_audio(file_path)

# Step 2: Summarize text if transcription is successful
if transcription:
    summarize_text()