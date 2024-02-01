import os
import time
import pywhisper
import json

model = pywhisper.load_model("base")


def transcribe_directory(audio_directory):
    # Dictionary to hold all transcriptions
    transcriptions = {}

    # Put all the audio files in the directory into a list
    audio_files = [
        file
        for file in os.listdir(audio_directory)
        if file.endswith(".mp3") or file.endswith(".wav")
    ]

    # Process each audio file
    for audio_file in audio_files:
        file_path = os.path.join(audio_directory, audio_file)
        file_title = os.path.splitext(audio_file)[
            0
        ]  # Remove the extension from the title

        print(
            f"Processing {audio_file}..."
        )  # Print the file being processed to track progress
        start_time = time.time()  # Start timing
        result = model.transcribe(file_path)
        processing_time = time.time() - start_time  # Stop timing

        transcription = result["text"]  # Extract the transcription text only
        transcriptions[file_title] = transcription

        print(
            f"Finished {audio_file} in {processing_time:.2f} seconds."
        )  # Print the time taken to process the file

    # Write all transcriptions to a JSON file
    with open("transcriptions.json", "w", encoding="utf-8") as f:
        json.dump(transcriptions, f, ensure_ascii=False, indent=4)

    return transcriptions


# Path to the directory containing audio files (this is hardcoded for simplicity right now)
audio_directory = "audios"

# Transcribe all audio files in the directory and save to JSON
all_transcriptions = transcribe_directory(audio_directory)
