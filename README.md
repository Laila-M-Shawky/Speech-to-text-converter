# 🎙️ Speech to Text Converter

<p align="center">
  <img src="speech_to_text.gif" width="600" />
</p>

- This desktop app converts speech into text, summarizes the content, and speaks it back to the user.
- You can either record your voice using a microphone or upload a `.wav` audio file.

---

## 📚 Table of Contents
- [Description](#-description)
- [Dataset](#-dataset)
- [Installation](#-installation)
- [Inference Demo](#-inference-demo)
- [Project Structure](#-project-structure)
- [Contributors](#-contributors)
- [License](#-license)

---

## 📌 Description

- Simple desktop app built with Python to convert speech into summarized, readable text.
- Supports two input methods:
  - Live microphone recording.
  - File-based input using `.wav` files.
- Uses Google Speech Recognition to convert speech to text.
- Applies LSA (Latent Semantic Analysis) via Sumy for automatic summarization.
- Outputs summary as:
  - Text saved to `output.txt`.
  - Spoken audio using `pyttsx3` for accessibility.

---

## 📁 Dataset

- No external dataset is required.
- Works with:
  - Real-time voice input.
  - Any clear `.wav` audio file in English.
- Ideal for demoing on personal recordings or public `.wav` samples.

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
```
### 2. Setup

- Ensure the following before running:
  - Python 3.8+ is installed.
  - Microphone is connected (if recording).
  - A `.wav` file is ready (if uploading).
- Launch the app with:

```bash
python main.py
```


## 🎬 Inference Demo

<p align="center">
  <img src="Demo.gif" width="800" />
</p>

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

## 📁 Project Structure

```bash
SpeechToTextConverter
├── main.py                    # Main GUI and application logic
├── audio_utils.py             # Audio recording and speech recognition functions
├── summary_utils.py           # Text summarization and file saving utilities
├── speech_utils.py            # Text-to-speech functionality
├── requirements.txt           # List of required Python libraries
├── README.md                  # Project documentation and usage guide
├── speech_to_text.gif         # Demo GIF showing application in action
├── Project_Proposal.pdf       # Initial project idea, objectives, and plan
├── Project_Presentation.pdf   # Final presentation delivered for ICAIL program
```

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
