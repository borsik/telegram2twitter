#!/bin/bash

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern.

check() {
  pgrep -lf ".[ /]$1( |\$)"
}

if check "telegram2twitter.py" >/dev/null
    then
        echo "Bot is running, nothing to do"
    else
        echo "Bot is dead, recover"
        python bot.py &
fi