# VTOL Parameter File
import numpy as np

# Physical parameters of the  VTOL known to the controller
mc =  1# kg
mr =  .25 # kg
Jc =  0.0042 # kg m^2
d =  .3 # m
mu =  .1 # kg/s
g =  9.81 # m/s^2
F_wind = 0 # wind disturbance force

# parameters for animation
length = 10.0

# Initial Conditions
z0 =  0 # initial lateral position
h0 =  5.0 # initial altitude
theta0 = 0 # initial roll angle
zdot0 =  0 # initial lateral velocity
hdot0 =  0 # initial climb rate
thetadot0 = 0  # initial roll rate
target0 = 0

# Simulation Parameters
t_start = 0 # Start time of simulation
t_end =  10 # End time of simulation
Ts =  .1 # sample time for simulation
t_plot = .1 # the plotting and animation is updated at this rate

# saturation limits
Fmax =  10 # Max Force, N

#Controller Coefficients
kph = 0.114583
kdh = 0.5891671

kptheta = 0.372075
kdtheta = 0.191314

kpz = -0.007709
kdz = -0.03282


# dirty derivative parameters
# sigma =   # cutoff freq for dirty derivative
# beta =  # dirty derivative gain

# equilibrium force
# Fe =


