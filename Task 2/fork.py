import os

pid = os.fork()

if (pid == 0) : # child process
    print("Child Process")
else:
    print("Parent Process")