# Import the speech recognition library
import speech_recognition as sr

# Import messagebox from tkinter to show alerts to the user
from tkinter import messagebox

# Function to record audio from the microphone and transcribe it to text
def record_audio():
    r = sr.Recognizer()  # Create a Recognizer object
    with sr.Microphone() as src:  # Use the system microphone as the audio source
        messagebox.showinfo("Recording", "Say something...")  # Show a popup to inform the user
        r.adjust_for_ambient_noise(src)  # Adjust for background noise
        audio = r.listen(src)  # Listen and capture the audio
    try:
        # Try to recognize the captured audio using Google's API
        result = r.recognize_google(audio, language='en-US')
        return result
    except:
        # If recognition fails, show an error message and return an empty string
        messagebox.showerror("Error", "Couldn't get the voice correctly")
        return ""

# Function to transcribe an existing WAV audio file to text
def transcribe_from_file(file_path):
    r = sr.Recognizer()  # Create a Recognizer object
    try:
        with sr.AudioFile(file_path) as src:  # Load the audio file
            audio = r.record(src)  # Read the entire content of the file
        # Try to recognize the audio using Google's API
        result = r.recognize_google(audio, language='en-US')
        return result
    except:
        # If transcription fails, show an error message and return an empty string
        messagebox.showerror("Error", "Couldn't read from file.")
        return ""
