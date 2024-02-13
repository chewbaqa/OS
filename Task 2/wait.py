import os

pid = os.fork()

if pid == 0:
    print("Child Process")
else:
    pid, status = os.wait()
    print("Child process with PID",pid,"terminated with status",status)
