# Import the text-to-speech library
import pyttsx3

# Initialize the text-to-speech engine
tts = pyttsx3.init()

# Function to speak out the given text aloud
def speak(text):
    tts.say(text)        # Queue the text to be spoken
    tts.runAndWait()     # Process and speak the queued text
