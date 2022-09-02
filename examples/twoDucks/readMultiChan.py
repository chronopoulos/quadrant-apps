#!/usr/bin/python3 -u

import serial
import struct
import sys

if len(sys.argv) > 2:
    deviceFile0 = sys.argv[1]
    deviceFile1 = sys.argv[2]
else:
    deviceFile0 = '/dev/ttyACM0'
    deviceFile1 = '/dev/ttyACM1'

quadrant0 = serial.Serial(deviceFile0, 115200)
quadrant1 = serial.Serial(deviceFile1, 115200)

while True:
    result0 = quadrant0.read(5);
    quadrant0.reset_input_buffer()
    result1 = quadrant1.read(5);
    quadrant1.reset_input_buffer()
    if (result0[4] == 10) and (result1[4] == 10):
        data = struct.unpack('BBBBBBBB', result0[:4] + result1[:4])
        print('%d %d %d %d %d %d %d %d;' % data)
    else:
        print('wtf!')
        continue
