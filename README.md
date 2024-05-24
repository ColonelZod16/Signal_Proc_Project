
# Distance and Direction Estimation

Determining the distance and direction of person while running/walking using inertial sensors
of a Mobile Phone.

This project uses sensors like Magnetometer, Gyroscope to get the yaw angles which is used to deter-
mine the orientation of an object with respect to Z-axis.
To determine the distance travelled by the person while walking/running accelerometer data was used.
Low pass filter to filter out noise was also used.
The results were then compared with GPS to measure the accuracy.
## Direction Theory

Yaw, pitch, and roll angles are commonly used to describe the orientation of an object in three-
dimensional space. Here’s a brief explanation of each angle:
Yaw Angle (yaw): Yaw angle represents the rotation about the vertical axis (typically the z-axis).

It indicates the direction in which an object is facing relative to a reference direction. Yaw angles
change when the object rotates horizontally.
yaw = atan2(magy, magx), where magx and magy are the magnetic field components along the x and
y axes, respectively.

Pitch Angle (pitch): Pitch angle represents the rotation about the lateral axis (typically the y-axis).
It indicates the tilt of an object relative to the horizontal plane. Pitch angles change when the object
tilts up or down.

Roll Angle (roll): Roll angle represents the rotation about the longitudinal axis (typically the x-
axis). It indicates the tilt of an object relative to the vertical plane. Roll angles change when the
object tilts sideways.

While walking or running, the motion primarily involves changes in the yaw angle, as the direction of
movement changes. Pitch and roll angles may also change to some extent)
\horizontal



## Distance Theory

The code computes the time intervals between consecutive data points. It then determines the mag-
nitude of acceleration at each time point using the Euclidean norm. By approximating the area under
the acceleration-time curve using the trapezoidal rule, it estimates the velocity in the y-direction. Sub-
sequently, the code integrates velocity over time to calculate the change in position (displacement) in
the y-direction. Finally, it sums up the displacement values to estimate the total distance traveled.

The code only uses the y-direction because the phone is always in y-axis w.r.t the user , so whichever
direction the person turns , that direction becomes the y-axis w.r.t to the user hence it makes sense
to only use the accelerometer data in the y-direction.
## Results

According to the GPS data , the user walked a distance of 360 meters.

The code gives us a distance of 393.

The calculated distance is more due to the noise picked up by the inertial sensors. 100 Percent accuracy
cannot be achieved due to noise , even after the data was passed through a low pass filter.


## Run Locally

Use tools such as Physics Toolbox suite to collect data as you walk or run. Write the filename in either of the codes and check the result. Direction.py gives you an animation of real time direction changes. Distance will give a close estimation of the actual distance.



## Contributors

- [Sreyas Janamanchi](https://www.linkedin.com/in/sreyas-janamanchi-932569261/)
- [Anshul V Patil](https://www.linkedin.com/in/anshul-v-patil-44559221a/)
- [Nishal M](https://www.linkedin.com/in/nishal-m-221a44259/)

