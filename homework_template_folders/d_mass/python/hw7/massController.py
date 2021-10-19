import numpy as np

import sys

sys.path.append('..')  # add parent directory
import massParam as P


class massController:
    def __init__(self):
        # Instantiates the PD object
        self.kp = P.kp
        self.kd = P.kd
        self.ki = 0.1
        self.limit = P.f_max
        self.integral = 0.0

    def update(self, z_r, x):
        z = x.item(0)
        zdot = x.item(1)

        z_e = z_r
        F_e = P.k * z_e

        self.integral = self.integral + (z_r - z)
        if zdot >= .4 or zdot <= -.4:
            self.integral = 0

        F_tilde = self.kp * (z_r - z) - self.kd * zdot + self.ki * self.integral

        F = F_e + F_tilde

        F = self.saturate(F)

        return F

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit * np.sign(u)
        return u
