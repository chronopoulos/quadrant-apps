#!/usr/bin/python3 -u

import serial
import struct
import sys

if len(sys.argv) > 1:
    deviceFile = sys.argv[1]
else:
    deviceFile = '/dev/ttyACM0'

quadrant = serial.Serial(deviceFile, 115200)

engaged = [False, False, False, False]

while True:
    result = quadrant.read(5);
    if result[4] == 10:
        data = struct.unpack('BBBB', result[:4])
        for i in range(4):
            if (not engaged[i]) and (data[i] < 180):
                engaged[i] = True
                print('%d %d;' % (i, data[i]))
            if engaged[i] and (data[i] >= 180):
                engaged[i] = False
    else:
        print('wtf!')
