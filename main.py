# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: rtse_pi
File Name: main.py.py
Author: sunch
Create Date: 2021/11/18 14:49 
-------------------------------------------------
"""

import hw
import webrtcns
import time

ns = webrtcns.Ns()
ns.set_mode(3)

recorder = hw.recorder()
player = hw.player()

while True:
    data = recorder.read(160, exception_on_overflow=False)
    data = ns.process(data)
    player.write(data)
    time.sleep(.001)

