# Import necessary modules for GUI and audio processing
import tkinter as tk
from tkinter import filedialog, messagebox
from audio_utils import record_audio, transcribe_from_file
from summary_utils import do_summary, save_output
from speech_utils import speak

# Function to handle recording audio from microphone,
# transcribing it, summarizing it, saving it, and speaking it aloud
def do_record():
    spoken = record_audio()  # Capture audio input from mic and convert to text
    if spoken.strip():       # Check if transcription is not empty
        summary = do_summary(spoken)   # Summarize the transcribed text
        save_output(summary)          # Save summary to output.txt
        speak("Done summarizing.")    # Read the summary aloud

# Function to handle file input (WAV file),
# transcribing it, summarizing it, saving it, and speaking it aloud
def do_file():
    f_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])  # Open file dialog
    if f_path:                                 # If a file is selected
        spoken = transcribe_from_file(f_path)  # Transcribe audio from file
        if spoken.strip():                     # Check if transcription is not empty
            summary = do_summary(spoken)       # Summarize the transcribed text
            save_output(summary)               # Save summary to output.txt
            speak("Summary is saved.")         # Read the summary aloud

# === GUI SETUP ===

# Create the main window
root = tk.Tk()
root.title("Voice Summary Tool")      # Set window title
root.geometry("400x220")              # Set window size

# Add a label to guide the user
main_lbl = tk.Label(root, text="Choose how you wanna input audio", font=("Arial", 14))
main_lbl.pack(pady=15)

# Add a button to start recording audio
record_btn = tk.Button(root, text="Record Audio", font=("Arial", 13), command=do_record)
record_btn.pack(pady=8)

# Add a button to upload an audio file
file_btn = tk.Button(root, text="Upload Audio File", font=("Arial", 13), command=do_file)
file_btn.pack(pady=8)

# Start the GUI event loop
root.mainloop()