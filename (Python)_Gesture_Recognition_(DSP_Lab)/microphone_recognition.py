#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pygame
import json
import time

# obtain audio from the microphone
r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

class Volume(object):
    def __init__(self):
        self.level = .5

    def increase(self, amount):
        self.level += amount
        print(f'New level is: {self.level}')

    def decrease(self, amount):
        self.level -= amount
        print(f'New level is: {self.level}')


vol = Volume()

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/adity/DSP/dsp3/Angel_Baby.mp3')
pygame.mixer.music.set_volume(vol.level)
pygame.mixer.music.play()
pygame.mixer.music.set_pos(50)
pygame.mixer.music.pause()

with sr.Microphone() as source:
    # print("Say something!")
        audio = r.listen(source)
    
voice = r.recognize_google(audio, language = 'en-US', show_all = True)
voice = json.dumps(voice, ensure_ascii=False)   

v2 = voice.get('alternative')
v3 = voice['alternative'][0]
print (v3)
v4 = v3['transcript']

# recognize speech using Sphinx
# while True:
#     # with sr.Microphone() as source:
#     # # print("Say something!")
#     #     audio = r.listen(source)
    
#     # voice = r.recognize_google(audio, language = 'en-US', show_all = True)
#     # voice = json.dumps(voice, ensure_ascii=False)   

#     # v2 = voice.get('alternative')
#     # v3 = voice['alternative'][0]
#     # print (v3)
#     # v4 = v3['transcript']
    

#     # v4 = voice.alternative.

#     # print(dir(voice))

#     if v4 == "music on":
#         pygame.mixer.music.unpause()

#     elif v4 == "music off":
#         pygame.mixer.music.pause()

#     elif v4 == "volume up":
#         vol.increase(0.2)
#         pygame.mixer.music.set_volume(vol.level)

#     elif v4 == "volume down":
#         vol.decrease(0.2)
#         pygame.mixer.music.set_volume(vol.level)



