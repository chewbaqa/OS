import pandas as pd

def priority_scheduling(processes, priorities):
    # Create a DataFrame from processes and priorities
    df = pd.DataFrame({'Process': processes, 'Priority': priorities})

    # Sort the DataFrame by priority
    df = df.sort_values('Priority')

    print(df)


processes = ['P1', 'P2', 'P3', 'P4', 'P5']
priorities = [3, 1, 4, 5, 2]
# ! 
priority_scheduling(processes, priorities) 