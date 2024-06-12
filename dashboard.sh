#!/bin/bash
# Launches dashboard

echo "Where would you like to go?"
echo
echo
echo

sleep 1

read -rp "Target website:" destination
echo -e "DESTINATION='$destination'" > ~/dashtop/.env
echo
echo

sleep 3
echo "Launching dashboard"
echo
echo
echo

sleep 3

DISPLAY=:0 ~/.py/bin/python ~/dashtop/scripts/dashtopLoad.py
