# Ball on Beam Parameter File
import numpy as np
# import control as cnt

# Physical parameters of the  ballbeam known to the controller
m1 = .35  # Mass of the ball, kg
m2 =  2 # mass of beam, kg
length = .5  # length of beam, m
g = 9.81  # gravity at sea level, m/s^2

# parameters for animation
radius = 0.05  # radius of ball

# Initial Conditions
z0 = length/2 # initial ball position,m
theta0 = 0 * np.pi/180  # initial beam angle,rads
zdot0 = 0  # initial speed of ball along beam, m/s
thetadot0 = 0 # initial angular speed of the beam,rads/s

# Simulation Parameters
t_start = 0  # Start time of simulation
t_end = 10  # End time of simulation
Ts = .001  # sample time for simulation
t_plot = .1  # the plotting and animation is updated at this rate

# Controller Coefficients
kptheta = 1.82508
kdtheta = 1.17303
kpz = -0.031743
kdz = -0.04939

# saturation limits
Fmax = 1000  # Max Force, N

# dirty derivative parameters
# sigma =   # cutoff freq for dirty derivative
# beta =  # dirty derivative gain

# equilibrium force when ball is in center of beam
# ze =
# Fe =
