#!/bin/bash
# Launches dashboard

echo "Launching dashboard"
echo
echo
echo

sleep 3

DISPLAY=:0 ~/.py/bin/python ~/dashtop/scripts/dashboardLoader.py
