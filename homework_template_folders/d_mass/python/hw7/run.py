import matplotlib.pyplot as plt
import sys
sys.path.append('..')  # add parent directory
import massParam as P
from hw2.signalGenerator import signalGenerator
from hw2.massAnimation import massAnimation
from hw2.dataPlotter import dataPlotter
from hw3.massDynamics import massDynamics
from massController import massController

# instantiate satellite, controller, and reference classes
mass = massDynamics(alpha=0.0)
controller = massController()
reference = signalGenerator(amplitude=1, frequency=0.05)
disturbance = signalGenerator(amplitude=0.3)
noise = signalGenerator(amplitude=1.0)

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = massAnimation()

t = P.t_start  # time starts at t_start
z = mass.h()
while t < P.t_end:  # main simulation loop

    # Propagate dynamics in between plot samples
    t_next_plot = t + P.t_plot

    # updates control and dynamics at faster simulation rate
    while t < t_next_plot:
        r = reference.square(t)
        d = disturbance.step(t)
        n = 0.0 #noise.random(t)
        x = mass.state
        u = controller.update(r,x)
        z = mass.update(u + d)  # Propagate the dynamics
        t = t + P.Ts  # advance time by Ts

    # update animation and data plots
    animation.update(mass.state)
    dataPlot.update(t, r, mass.state, u)

    # the pause causes the figure to be displayed during the
    # simulation
    plt.pause(0.0001)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
