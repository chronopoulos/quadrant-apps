#!/bin/bash

pasuspender -- pd main.pd &
sleep 2
python3 -u ./multipluck.py | pdsend 8000
