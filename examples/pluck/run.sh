#!/bin/bash

pasuspender -- pd main.pd &
sleep 2
python3 -u ./pluck.py | pdsend 8000
