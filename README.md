# 🗣️ Voice Assistant - Echo  

**Echo** is an AI-powered voice assistant that recognizes voice commands, responds with text-to-speech, and performs system automation tasks.  

## 🛠️ Technologies Used

### 🎙️ Voice Interaction
- **Speech Recognition (`speech_recognition`)** - Converts voice commands into text.
- **Text-to-Speech (`pyttsx3`)** - Converts text responses into speech.

### 🌐 Web & Search
- **Wikipedia API (`wikipedia`)** - Fetches summaries for user queries.
- **Web Automation (`webbrowser`)** - Opens and navigates web pages.
- **YouTube & Music (`pywhatkit`)** - Searches and plays music on YouTube, Spotify, or Apple Music.

### 🎵 Media & System Control
- **System Control (`os`, `pyautogui`)** - Opens applications, controls volume, manages system shutdown/restart, and automates keyboard/mouse tasks.
- **Screen Capture (`pyautogui`)** - Takes and saves screenshots based on voice input.

### 🖥️ GUI Interface
- **Custom GUI (`customtkinter`)** - Provides an interactive graphical interface.

### 🖱️ Miscellaneous
- **IP Lookup (`requests`)** - Retrieves the user's public IP address.

## 🚀 Features  

### 🎙️ Voice Interaction  
- Uses `speech_recognition` for voice input and `pyttsx3` for text-to-speech.  
- Greets users based on the time of day.  

### 🌐 Web & Search  
- Searches Wikipedia and reads summaries.  
- Opens YouTube, Google, and other websites.  
- Plays YouTube videos directly via voice command.  
- Supports playing music on **Spotify** and **Apple Music**.  

### 🎵 Media & System Control  
- Plays local music and video files.  
- Adjusts system volume.  
- Takes screenshots with user-defined names.  
- Opens/closes applications like Notepad, VLC, Command Prompt, and Google.  
- Controls system functions (shutdown, restart, lock).  

### 🖥️ GUI Interface  
- Built with `customtkinter` for an interactive experience.  
- Includes buttons for manual control of the assistant.  

### 🖱️ Automation & Miscellaneous  
- Uses `pyautogui` for keyboard and mouse automation.  
- Opens and interacts with applications using automation.  
- Retrieves public IP address information.  
- Recognizes and processes multiple commands continuously.  

## 🛠️ Installation & Usage  

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
2. Run the assistant:  
   ```bash
   python Assistant.py
   ```  
3. Use voice commands to interact with Echo.  

## 📝 Example Commands  
- **"Search Python programming on Wikipedia"**  
- **"Open YouTube and play a song"**  
- **"Take a screenshot"**  
- **"Shut down the system"**  
- **"What is my IP address?"**  

🔹 **Echo is a powerful and interactive AI assistant designed for automation and ease of access!**  
