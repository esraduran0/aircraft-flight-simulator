import math
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# Simulation Constants
# ============================================================

# --- Aircraft Parameters ---
PITCH_DEG = 10
SPEED_MPS = 100
INITIAL_ALTITUDE_M = 1000

# --- Time Settings ---
INITIAL_TIME_S = 0
DT_S = 0.1
SIMULATION_DURATION_S = 10


# --- Turbulence Model ---
TURBULENCE_MEAN_MPS = 0
TURBULENCE_STD_MPS = 0.5

# --- State Initialization ---
altitude = INITIAL_ALTITUDE_M
time = INITIAL_TIME_S

time_list = []
altitude_list = []
vertical_speed_list = []

pitch_rad = math.radians(PITCH_DEG)  # Convert pitch to radians

while time < SIMULATION_DURATION_S:
    time += DT_S  # Increment time by dt
    time = round(time, 2) # Round time to 2 decimal places for better readability
    

    turbulence = np.random.normal(TURBULENCE_MEAN_MPS, TURBULENCE_STD_MPS) # Simulate turbulence as a random value from a normal distribution with mean and standard deviation

    vertical_speed = SPEED_MPS * math.sin(pitch_rad) + turbulence # Calculate vertical speed based on pitch and add turbulence effect
    

    altitude += vertical_speed * DT_S # Update altitude based on vertical speed and time step
    

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

