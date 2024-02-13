import numpy as np
import pandas as pd

def round_robin(pids, burst_times, quantum):
    rem_bursts, t, wait_times = np.copy(burst_times), 0, np.zeros(len(pids))

    while np.any(rem_bursts > 0):
        for i in range(len(rem_bursts)):
            if rem_bursts[i] > 0:
                time = min(quantum, rem_bursts[i])
                t += time
                rem_bursts[i] -= time
                if rem_bursts[i] == 0:
                    wait_times[i] = t - burst_times[i]

    df = pd.DataFrame({
        'Process': pids,
        'Burst Time': burst_times,
        'Waiting Time': wait_times
    })
    print(df)

# Driver code
round_robin([1, 2, 3], [10, 5, 8], 2) 