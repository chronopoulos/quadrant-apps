#!/bin/bash

pasuspender -- pd main.pd &
sleep 2
./readMultiChan.py | pdsend 8000
