#!/usr/bin/python3 -u

import serial
import struct
import sys
import rtmidi

def program_change(midi_out, channel, program):
    statusByte = (192 & 0xf0) | (channel - 1 & 0xf)
    msg = [statusByte] + [program & 0x7f]
    midi_out.send_message(msg)

if len(sys.argv) > 1:
    deviceFile = sys.argv[1]
else:
    deviceFile = '/dev/ttyACM0'

quadrant = serial.Serial(deviceFile, 115200)

engaged = [False, False, False, False]
primeRight = False
primeLeft = False
primeUp = False
primeDown = False

midiOut = rtmidi.MidiOut()
available_ports = midiOut.get_ports()
if available_ports:
    print('opening port 0')
    midiOut.open_port(0)
else:
    print('opening virtual port')
    midiOut.open_virtual_port("My virtual output")

currentProgram = 1

while True:
    result = quadrant.read(5);
    if result[4] == 10:
        data = struct.unpack('BBBB', result[:4])
        for i in range(4):
            if (not engaged[i]) and (data[i] < 180):
                engaged[i] = True
                if i==1 and engaged[3]:
                    primeRight = True
                if i==3 and engaged[1]:
                    primeLeft = True
            if engaged[i] and (data[i] >= 180):
                engaged[i] = False
                if i==1 and engaged[3]:
                    if primeLeft:
                        print('left swipe')
                        currentProgram -= 1
                        if currentProgram == 0:
                            currentProgram = 16
                        program_change(midiOut, 1, currentProgram)
                        primeLeft = False
                    elif primeRight:
                        print('right fakeout')
                        primeRight = False
                if i==3 and engaged[1]:
                    if primeRight:
                        print('right swipe')
                        currentProgram += 1
                        if currentProgram == 17:
                            currentProgram = 1
                        program_change(midiOut, 1, currentProgram)
                        primeRight = False
                    elif primeLeft:
                        print('left fakeout')
                        primeLeft = False
    else:
        print('wtf!')
