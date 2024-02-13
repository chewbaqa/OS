import pandas as pd

def sjf(processes, burst_time):
    df = pd.DataFrame({'Process': processes, 'Burst Time': burst_time})
    df = df.sort_values(by='Burst Time').reset_index(drop=True)

    df['Waiting Time'] = df['Burst Time'].shift(fill_value=0).cumsum()
    df['Turnaround Time'] = df['Burst Time'] + df['Waiting Time']

    print(df.to_string(index=False))

# Example usage
processes = [1, 2, 3]
burst_time = [10, 6, 8]
sjf(processes, burst_time) 
