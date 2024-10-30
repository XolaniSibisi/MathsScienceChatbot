import os
import pygame
from gtts import gTTS
from pathlib import Path
import time

def text_to_speech(text):
    # Define the path to save the speech file
    speech_file_path = Path(__file__).parent / "speech.mp3"

    # Delete the existing file if it exists
    if os.path.exists(speech_file_path):
        os.remove(speech_file_path)

    # Use gTTS to convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save(speech_file_path)  # Save the audio file

    # Initialize pygame mixer to play the audio
    pygame.mixer.init()
    pygame.mixer.music.load(speech_file_path)
    pygame.mixer.music.play()

    # Keep the program running long enough for the audio to play
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    pygame.mixer.quit()

