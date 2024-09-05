#from gtts import gTTS
import pyttsx3
import os

'''
this did not sound as good in my opinion
def ttsgtts(text,lang,accent):
	mp3 = gTTS(text = text, lang = lang, tld = accent)
	filename = 'temp.mp3'
	mp3.save(os.path.dirname(os.path.realpath(__file__)) + '/aud.mp3')
'''

#can change voice module i think in pyttsx3 if you download more voices
def tts(text, voice):
    eng = pyttsx3.init()
    eng.setProperty('rate', 125)
    voices = eng.getProperty('voices')
    eng.setProperty('voice',voices[voice].id)
    eng.save_to_file(text, os.path.dirname(os.path.realpath(__file__)) + '/aud.mp3')
    eng.runAndWait()
	

tts("ahh why am i gay", 0)

