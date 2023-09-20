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

    data0_raw = quadrant0.readline();
    data0 = tuple(map(int, data0_raw.split()))
    quadrant0.reset_input_buffer()

    data1_raw = quadrant1.readline();
    data1 = tuple(map(int, data1_raw.split()))
    quadrant1.reset_input_buffer()

    if (len(data0) == 4) and (len(data1) == 4):
        data = struct.unpack('BBBBBBBB', data0[:4] + data1[:4])
        print('%d %d %d %d %d %d %d %d;' % data)
    else:
        print('wtf!')
        continue
