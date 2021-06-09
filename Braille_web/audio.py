import pyttsx3
from gtts import gTTS
import os
from playsound import  playsound
from tempfile import TemporaryFile


def text_to_speech(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome1.mp3")
    playsound("welcome1.mp3")
    os.remove("welcome1.mp3")