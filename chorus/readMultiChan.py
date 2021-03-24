#!/usr/bin/python -u

import serial
import struct
import sys

if len(sys.argv) > 1:
    deviceFile = sys.argv[1]
else:
    deviceFile = '/dev/ttyACM0'

quadrant = serial.Serial(deviceFile, 115200)
while True:
    result = quadrant.read(5);
    if result[4] == chr(10):
        data = struct.unpack('BBBB', result[:4])
        print '%d %d %d %d;' % data
    else:
        print 'wtf!'
