import numpy as np


def fcfs(processes, bt):
    n = len(processes)
    wt = np.insert(np.cumsum(bt[:-1]), 0, 0)
    ct = np.cumsum(bt)  # Completion Time

    print("Process\tBurst Time\tWaiting Time\tCompletion Time")
    for i in range(n):
        print(f"{i + 1}\t{bt[i]}\t\t{wt[i]}\t\t{ct[i]}")

    print(f"Average Waiting Time: {np.mean(wt)}")


processes = [1, 2, 3]
burst_time = [10, 6, 8]
fcfs(processes, burst_time)
