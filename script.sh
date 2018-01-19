#!/bin/bash

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern. 
while true; do
    if pgrep -x "telegram2tweeter.py" > /dev/null
    then
        echo "Running"
    else
        echo "Run script and sleep"
        python teletweet.py
    fi
    sleep 300
done