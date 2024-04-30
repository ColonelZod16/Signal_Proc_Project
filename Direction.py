import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
from matplotlib.animation import FuncAnimation
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

def calculate_yaw(mag_x, mag_y, gyro_z, dt):
    theta_yaw = np.arctan2(mag_y, mag_x)
    theta_yaw += gyro_z * dt
    return theta_yaw

input_file = 'high sampling 310.csv'
in_df = pd.read_csv(input_file)

normalized_cutoff = 1000000 / 2000000 

data_df=apply_lpf(in_df,normalized_cutoff)

# Calculate yaw angles
theta_yaw = calculate_yaw(data_df['Bx'], data_df['By'], data_df['wz'], data_df['time'].diff().mean())

# Convert yaw angles to degrees and handle negative angles
converted_yaw_angles = np.degrees(theta_yaw)
converted_yaw_angles[converted_yaw_angles < 0] += 360

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)  # Extend limits to accommodate the compass
ax.set_ylim(-1.5, 1.5)  # Extend limits to accommodate the compass
ax.set_axis_off()

# Draw the compass around the needle
circle = Circle((0, 0), 1, edgecolor='black', facecolor='none')
ax.add_patch(circle)

# Initial position and length of the arrow
x, y = 0, 0
dx, dy = 0, 0.8

compass_needle = FancyArrowPatch((x, y), (dx, dy), color='red', arrowstyle='->', linewidth=2)
ax.add_patch(compass_needle)

time_text = ax.text(0.5, -0.1, '', transform=ax.transAxes, ha='center', fontsize=12)
angle_text = ax.text(0.5, -0.15, '', transform=ax.transAxes, ha='center', fontsize=12)

def update_compass(frame):
    global compass_needle, time_text, angle_text
    current_time = data_df['time'].iloc[frame]
    current_yaw = converted_yaw_angles[frame]
    dx = np.cos(np.radians(current_yaw)) * 0.8  # Calculate new dx based on the current yaw angle
    dy = np.sin(np.radians(current_yaw)) * 0.8  # Calculate new dy based on the current yaw angle
    new_arrow = FancyArrowPatch((x, y), (dx, dy), color='red', arrowstyle='->', linewidth=2)
    compass_needle.remove()  # Remove the old arrow
    compass_needle = ax.add_patch(new_arrow)  # Add the new arrow
    time_text.set_text(f'Time: {current_time:.2f} s')
    angle_text.set_text(f'Yaw Angle: {current_yaw:.2f} degrees')
    return compass_needle, time_text, angle_text

# Calculate the time difference between data points in the CSV file
time_diff = data_df['time'].diff().mean()

# Calculate the number of frames per second based on the time difference
fps = int(1 / time_diff)

ani = FuncAnimation(fig, update_compass, frames=len(data_df['time']), interval=1, blit=True)
plt.show()
