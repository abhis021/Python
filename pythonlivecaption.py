# pip install SpeechRecognition PyAudio

# Make sure to update the device_index on line 34, to reflect the stero mixer on your computer

import concurrent.futures
import speech_recognition as sr
import time

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s: %(levelname)s - %(message)s"
)

def listen(mic, id):
    logging.debug(f"Listening... {id}")
    with mic as source:
        audio = r.listen(source, timeout=5, phrase_time_limit=3)
        return audio


def transcribe(audio):
    logging.debug(f"transcribing...")
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("\r...")


if __name__ == "__main__":
    r = sr.Recognizer()
    r.pause_threshold = 2

    mic = sr.Microphone(device_index=4)
    while True:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            listener = executor.submit(listen, mic, 1)
            subtitles = executor.submit(transcribe, listener.result())
            logging.info(subtitles.result())