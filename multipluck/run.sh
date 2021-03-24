#!/bin/bash

pasuspender -- pd main.pd &
sleep 2
./multipluck.py | pdsend 8000
