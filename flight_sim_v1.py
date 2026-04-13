import math
import matplotlib.pyplot as plt
import numpy as np

pitch = 10 #pitch in degrees
speed = 100 
altitude = 1000
dt = 0.1
time = 0

time_list = []
altitude_list = []
vertical_speed_list = []

while time < 10:
    time += dt  # Increment time by dt
    time = round(time, 2) # Round time to 2 decimal places for better readability
    
    pitch_rad = math.radians(pitch)  # Convert pitch to radians

    turbulence = np.random.normal(0,0.5) # Simulate turbulence as a random value from a normal distribution with mean 0 and standard deviation 0.5

    vertical_speed = speed * math.sin(pitch_rad) + turbulence # Calculate vertical speed based on pitch and add turbulence effect
    

    altitude += vertical_speed * dt # Update altitude based on vertical speed and time step
    

    time_list.append(time)  # Append current time to the list
    altitude_list.append(altitude)  # Append current altitude to the list
    vertical_speed_list.append(vertical_speed)  # Append current vertical speed to the list

plt.figure()

plt.plot(time_list, altitude_list)
plt.title("Altitude vs Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Altitude (meters)")

plt.figure()

plt.plot(time_list, vertical_speed_list)
plt.title("Vertical Speed vs Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Vertical Speed")

plt.show()

