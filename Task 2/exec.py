import os

os.execl('/bin/ls','ls','-l')

# replaces the current process with the ls command