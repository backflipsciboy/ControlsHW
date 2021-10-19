import matplotlib.pyplot as plt
import sys

import numpy as np

sys.path.append('..')  # add parent directory
import VTOLParam as P
from hw2.signalGenerator import signalGenerator
from hw2.VTOLAnimation import VTOLAnimation
from hw2.dataPlotter import dataPlotter
from hw3.vtolDynamics import vtolDynamics
from vtolController import vtolController

# instantiate satellite, controller, and reference classes
satellite = vtolDynamics()
referenceH = signalGenerator(amplitude=0.0, frequency=0.01, y_offset=5)
referenceZ = signalGenerator(amplitude=2.5, frequency=.08, y_offset=3.0)
disturbance = signalGenerator(amplitude=0.0)
noise = signalGenerator(amplitude=1.0)

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = VTOLAnimation()
controller = vtolController()

t = P.t_start  # time starts at t_start
while t < P.t_end:  # main simulation loop

    # Propagate dynamics in between plot samples
    t_next_plot = t + P.t_plot

    # updates control and dynamics at faster simulation rate
    while t < t_next_plot:  
        rH = referenceH.step(t)
        rZ = referenceZ.step(t)
        n = 0.0 #noise.random(t)
        x = satellite.state + n
        d = disturbance.step(t)
        u = np.array(controller.update(rH,rZ,x))
        y = satellite.update(u)  # Propagate the dynamics
        t = t + P.Ts  # advance time by Ts

    # update animation and data plots
    animation.update(satellite.state, rZ)
    dataPlot.update(t, satellite.state, rZ, rH, u.item(0), u.item(1))

    # the pause causes the figure to be displayed during the
    # simulation
    plt.pause(0.0001)  

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
