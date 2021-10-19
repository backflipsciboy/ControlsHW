import numpy as np

import sys

sys.path.append('..')  # add parent directory
import VTOLParam as P


class vtolController:
    def __init__(self):
        # Instantiates the PD object
        self.kptheta = P.kptheta
        self.kdtheta = P.kdtheta
        self.kpz = P.kpz
        self.kdz = P.kdz
        self.kph = P.kph
        self.kdh = P.kdh
        self.limit = P.Fmax

    def update(self, h_r, z_r, x):
        z = x.item(0)
        h = x.item(1)
        theta = x.item(2)
        zdot = x.item(3)
        hdot = x.item(4)
        thetadot = x.item(5)

        theta_e = 0.0
        F_e = ((P.mc + 2 * P.mr) * P.g)/np.cos(theta_e)

        F_tilde = self.kph * (h_r - h) - self.kdh * hdot

        theta_r = self.kpz * (z_r - z) - self.kdz * zdot

        tau = self.kptheta * (theta_r - theta) - self.kdtheta * thetadot

        F = F_tilde #F_e + F_tilde

        F = self.saturate(F)

        return F, tau

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit * np.sign(u)
        return u
