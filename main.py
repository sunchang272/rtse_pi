# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: rtse_pi
File Name: main.py.py
Author: sunch
Create Date: 2021/11/18 14:49 
-------------------------------------------------
"""
import argparse
import webrtcns
import time
import hw


ns = webrtcns.Ns()
ns.set_mode(3)


player = hw.player()


def record_in():
    recorder = hw.recorder()
    while True:
        data = recorder.read(160, exception_on_overflow=False)
        data = ns.process(data)
        player.write(data)
        time.sleep(.001)


def file_in():
    wf = open(args.file, 'rb')
    wf.read(44)
    while True:
        data = wf.read(160)
        data = ns.process(data)
        player.write(data)
        time.sleep(0.1)


if __name__ == '__main__':
    argParser = argparse.ArgumentParser()
    argParser.add_argument('-m', '--mode', type=str, default='r')
    argParser.add_argument('-f', '--file', type=str, default='./-10db_s1_car.wav')
    args = argParser.parse_args()

    if args.mode == 'r':
        record_in()

    if args.mode == 'f':
        file_in()

