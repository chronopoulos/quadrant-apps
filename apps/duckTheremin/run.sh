#!/bin/bash

pasuspender -- pd main.pd &
sleep 2
python3 -u ../../common/serial2stdout.py | pdsend 8000
