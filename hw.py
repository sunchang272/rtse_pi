# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: version_1.0
File Name: recorder.py
Author: sunch
Create Date: 2021/11/24 14:53 
-------------------------------------------------
"""

import pyaudio


def recorder():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    return stream


def player():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    output=True)
    return stream

