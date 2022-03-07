#!/bin/bash

pasuspender -- pd main.pd &
sleep 2
./pluck.py | pdsend 8000
