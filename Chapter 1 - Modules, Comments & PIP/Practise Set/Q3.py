# Install an external module & use it to perform an operation of your interest

# pip install pyttsx3

# Text to Speech (TTS) library for Python

# Importing library
import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()