#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root."
   exit 1
fi

chmod +x watchout.py
cp watchout.py /usr/local/bin/
ln -s /usr/local/bin/watchout.py /usr/local/bin/watchout
echo "WatchOut CLI tool has been installed."
echo "To run the tool, type 'watchout' in the terminal."
# this is for linux users only, for windows users, you can create a batch file to run the python script
