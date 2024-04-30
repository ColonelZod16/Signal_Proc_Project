import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt

def apply_lpf(df, cutoff_freq, order=5):
    # Create the filter coefficients
    b, a = butter(order, cutoff_freq, btype='low')
    
    # Apply the filter to each column
    filtered_data = {}
    for col in df.columns:
        filtered_data[col] = filtfilt(b, a, df[col])
    
    # Create a new DataFrame with the filtered data
    filtered_df = pd.DataFrame(filtered_data)
    
    return filtered_df

# Load CSV data into a Pandas DataFrame
in_df = pd.read_csv('360 low freq.csv')

df=apply_lpf(in_df,1000000/2000000)

# Calculate time intervals in seconds (assuming time is already in seconds)
time_diff = np.diff(df['time'])

# Calculate average acceleration (magnitude) using the Euclidean norm
acceleration = np.linalg.norm(df[['ax', 'ay', 'az']], axis=1)

vy = np.zeros(len(acceleration))  # Initialize velocity array with zeros
for i in range(len(vy) - 1):
    vy[i] = (df['ay'][i] + df['ay'][i + 1]) / 2 * time_diff[i]

dy=np.zeros(len(vy))
# dx=np.cumsum(vx*time_diff)
for i in range(len(vy)-1):
    dy[i]=abs(vy[i]+vy[i+1]/2*time_diff[i])
dist=np.sum(dy)
# dz=np.cumsum(vz*time_diff)

# n=len(dx)
# dist=math.sqrt((dx[n-1]*2)+(dy[n-1]2)+(dz[n-1]*2))
# Print the total distance traveled
print(f"Total distance traveled: {dist} meters")
