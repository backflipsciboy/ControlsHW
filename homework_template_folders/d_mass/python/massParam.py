# Inverted Pendulum Parameter File
import numpy as np
# import control as cnt

# Physical parameters of the arm known to the controller
m = 5 # mass kg
k = 3 # spring constant Kg/s^2
b = .5 # damping coefficient Kg/s

# parameters for animation
length = 5.0
width = 1.0

# Initial Conditions
z0 = 0  # initial position of mass, m
zdot0 = 0 # initial velocity of mass m/s

# Simulation Parameters
t_start = 0 # Start time of simulation
t_end = 30  # End time of simulation
Ts = .01  # sample time for simulation
t_plot = .2 # the plotting and animation is updated at this rate

f_max = 6 # the maximum force to be applied
kp = 3.04755
kd = 7.19844

# dirty derivative parameters
# sigma =  # cutoff freq for dirty derivative
# beta =   # dirty derivative gain

# saturation limits
#F_max = 10  # Max force, N

