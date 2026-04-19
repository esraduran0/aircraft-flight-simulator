# Aircraft Flight Simulator (V1)

This project implements a basic aircraft flight simulation using Python.

The goal of this version is to understand how pitch angle affects altitude over time and to simulate simple flight behavior with added turbulence.

## Features

- Simulates aircraft motion based on pitch angle
- Computes vertical speed using trigonometry
- Updates altitude over time using discrete time steps
- Adds random turbulence using a normal distribution
- Visualizes results using Matplotlib

## Model Description

The vertical motion of the aircraft is modeled using:

- Pitch angle (in degrees)
- Constant speed

Vertical speed is calculated as:

vertical_speed = speed * sin(pitch) + turbulence

Altitude is updated over time using:

altitude = altitude + vertical_speed * dt

Where:
- dt is the time step
- turbulence is modeled as Gaussian noise

## Results

Two plots are generated:

1. Altitude vs Time
   Shows smooth upward motion due to constant pitch

2. Vertical Speed vs Time
   Shows fluctuations caused by turbulence

## Key Insight

Although turbulence directly affects vertical speed, its effect on altitude appears smoother because altitude is the integrated result of vertical speed over time.

## Technologies Used

- Python
- NumPy
- Matplotlib

## Future Improvements

- Add gravity and lift forces
- Model more realistic flight dynamics
- Introduce time-varying pitch
- Implement control systems

This is the first version (V1) of the project. Future versions will include more realistic physics and control mechanisms.