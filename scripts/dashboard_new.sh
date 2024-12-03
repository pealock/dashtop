#!/bin/bash

# Kills previous windows
sudo killall chromium-browser

# Launches dashboard
DISPLAY=:0 ../venv/bin/python ./dashtopLoad_new.py
