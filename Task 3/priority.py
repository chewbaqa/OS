import pandas as pd
import numpy as np


def priority_scheduling(processes, priorities, burst_times):
    # Create a DataFrame from processes, priorities and burst times
    df = pd.DataFrame(
        {"Process": processes, "Priority": priorities, "Burst Time": burst_times}
    )

    # Sort the DataFrame by priority
    df = df.sort_values("Priority")

    # Calculate waiting times
    df["Waiting Time"] = df["Burst Time"].cumsum() - df["Burst Time"]

    # Calculate turnaround times (waiting time + burst time)
    df["Turnaround Time"] = df["Waiting Time"] + df["Burst Time"]

    # Calculate completion times (cumulative sum of burst times)
    df["Completion Time"] = df["Burst Time"].cumsum()

    print(df)
    print(f'Average Waiting Time: {np.mean(df["Waiting Time"])}')
    print(f'Average Turnaround Time: {np.mean(df["Turnaround Time"])}')


processes = ["P1", "P2", "P3", "P4", "P5"]
priorities = [3, 1, 4, 5, 2]
burst_times = [10, 5, 8, 6, 9]
priority_scheduling(processes, priorities, burst_times)
