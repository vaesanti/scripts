#!/bin/bash
echo " $(df -H / | awk '/dev/ {print $4"/"$2}')"
