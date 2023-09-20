#!/bin/bash

pasuspender -- pd main.pd &
sleep 2
python3 ./serial2stdout_twoBoards.py | pdsend 8000
