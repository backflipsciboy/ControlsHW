import matplotlib.pyplot as plt
import sys

sys.path.append('..')  # add parent directory
import ballbeamParam as P
from hw2.signalGenerator import signalGenerator
from hw2.ballbeamAnimation import ballbeamAnimation
from hw2.dataPlotter import dataPlotter
from hw3.ballBeamDynamics import ballBeamDynamics
from ballController import ballController

# instantiate satellite, controller, and reference classes
ball = ballBeamDynamics()
controller = ballController()
reference = signalGenerator(amplitude=0.15, frequency=0.01, y_offset=.25)
disturbance = signalGenerator(amplitude=0.0)
noise = signalGenerator(amplitude=1)


# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = ballbeamAnimation()

t = P.t_start  # time starts at t_start
y = ball.h()
while t < P.t_end:  # main simulation loop

    # Propagate dynamics in between plot samples
    t_next_plot = t + P.t_plot

    # updates control and dynamics at faster simulation rate
    while t < t_next_plot:
        r = reference.square(t)
        d = disturbance.step(t)
        n = 0.0 #noise.random(t)
        x = ball.state
        u = controller.update(r,x)
        y = ball.update(u + d)  # Propagate the dynamics
        t = t + P.Ts  # advance time by Ts

    # update animation and data plots
    animation.update(ball.state)
    dataPlot.update(t, r, ball.state, u)

    # the pause causes the figure to be displayed during the
    # simulation
    plt.pause(0.0001)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
