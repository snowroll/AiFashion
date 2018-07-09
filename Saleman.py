# -*- coding:utf-8 -*- 
'''
author: chaihj15
date: 2018/07/09
'''

import simpleaudio as sa

class Saleman:
    def __init__(self):
        self.wav = sa.WaveObject.from_wave_file("welcome.wav")
    
    def welcome(self):
        play_obj = self.wav.play()
        play_obj.wait_done()

saleman = Saleman()
saleman.welcome()