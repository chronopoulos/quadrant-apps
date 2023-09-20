#!/usr/bin/python3 -u

import serial
import struct
import sys

if len(sys.argv) > 1:
    deviceFile = sys.argv[1]
else:
    deviceFile = '/dev/ttyACM0'

quadrant = serial.Serial(deviceFile, 115200)
while True:
    data_raw = quadrant.readline();
    data = tuple(map(int, data_raw.split()))
    if len(data) == 4:
        print('%d %d %d %d;' % data)
    else:
        print('wtf!')
