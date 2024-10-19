# Transcribes an audio file using Azure Speech Service and saves the recognized text to a file. It returns the recognized text as a string via the output_file variable and prints a completion message. It also prints a stream to the terminal as it recognizes the text during transcription.
 
import azure.cognitiveservices.speech as speechsdk
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the speech key from environment variables
speech_key = os.getenv("SPEECH_KEY")
service_region = "westeurope"
language = "de-DE"

# Set up the Azure Speech configuration
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language=language)

# Set the audio file path
audio_file = "./audio_samples/myfile.wav"

# Set up the audio configuration
audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

# Create a speech recognizer object
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Initialize an empty list to store recognized sentences
recognized_sentences = []

# Define an event handler for continuous recognition
def continuous_recognition_handler(evt):
  if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
    # Print the recognized sentence/phrase
    print(f"Recognized: {evt.result.text}")
    # Append the recognized text to the list
    recognized_sentences.append(evt.result.text)

# Start continuous recognition
speech_recognizer.recognized.connect(continuous_recognition_handler)
speech_recognizer.start_continuous_recognition()

# Wait for the recognition to complete
timeout_seconds = 6300# Set a timeout value (in seconds) based on your audio file length
timeout_expiration = time.time() + timeout_seconds

while time.time() < timeout_expiration:
  time.sleep(1)# Adjust the sleep duration as needed

# Stop continuous recognition
speech_recognizer.stop_continuous_recognition()

# Combine recognized sentences into a single string
transcription = '\n'.join(recognized_sentences)

# Open the output file in append mode
with open("transcription.txt", "a") as output_file:
  # Write the recognized text to the file
  output_file.write(transcription)
  output_file.write("\n")  # Add a newline for clarity

print("Recognition completed and results saved to transcription.txt")
