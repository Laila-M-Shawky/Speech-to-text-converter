# 🎙️ Speech to Text Converter

![Demo](speech_to_text.gif)

- This desktop app converts speech into text, summarizes the content, and speaks it back to the user.
- You can either record your voice using a microphone or upload a `.wav` audio file.

---

## 📌 Description

Speech to Text Converter is a simple desktop program built with Python that helps users transform spoken language into summarized, readable text.  
It supports both live audio recording through a microphone and file-based input using `.wav` files.  
After converting speech to text using Google’s Speech Recognition API, the application applies LSA (Latent Semantic Analysis) to summarize the text.  
Finally, it uses a text-to-speech engine to read the summary aloud for accessibility and convenience.

---

## 📁 Dataset

This project does not require any external dataset.  
It is designed to work with real-time voice input or pre-recorded `.wav` files.  
Users can test the tool with any clear, English audio sample in `.wav` format.

---

## ⚙️ Installation

### 1. Requirements

To get started, make sure you have Python 3.8 or later installed on your system.  
Then install the following Python libraries using pip:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install sumy
pip install pyaudio

### 2. Setup

- Ensure the following before running:
  - Python 3.8+ is installed.
  - Microphone is connected (if recording).
  - A `.wav` file is ready (if uploading).
- Launch the app with:

```bash
python main.py


## 🎬 Inference Demo

To use the application:

- Click **Record Audio**:
  - Speak into the microphone.
  - Wait for transcription and summary.
  - The summary is saved to `output.txt` and read aloud.

- Click **Upload Audio File**:
  - Select a `.wav` file from your computer.
  - The app transcribes, summarizes, saves, and speaks the result.

**Outcome:**  
Fast and accessible conversion of voice to summarized text.

---

## 👥 Contributors

Developed by **Team 4 – ICAIL 2025**:

- Ibrahim Abdelwahab  
- Mariam Youssef  
- Marina Soliman  
- Laila Mohamed  
- Mostafa Mahmoud

---

## 📝 License

- Open source under the **MIT License**.  
- Free to use, modify, and distribute with attribution.
