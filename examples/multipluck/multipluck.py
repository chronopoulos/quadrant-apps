#!/usr/bin/python3 -u

import serial
import struct
import sys

THRESH1 = 180
THRESH2 = 70

if len(sys.argv) > 1:
    deviceFile = sys.argv[1]
else:
    deviceFile = '/dev/ttyACM0'

quadrant = serial.Serial(deviceFile, 115200)

engaged = [False, False, False, False, False, False, False, False]

while True:
    data_raw = quadrant.readline();
    data = tuple(map(int, data_raw.split()))
    if len(data) == 4:
        for i in range(4):
            if (not engaged[i]) and (THRESH2 <= data[i] < THRESH1):
                engaged[i] = True
                print('%d %d;' % (i, data[i] - THRESH2))
            if engaged[i] and (data[i] >= THRESH1) or (data[i] < THRESH2):
                engaged[i] = False
            if (not engaged[i+4]) and (data[i] < THRESH2):
                engaged[i+4] = True
                print('%d %d;' % (i+4, data[i]))
            if engaged[i+4] and (data[i] >= THRESH2):
                engaged[i+4] = False
    else:
        print('wtf!')
