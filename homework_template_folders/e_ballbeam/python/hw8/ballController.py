import numpy as np

import sys

sys.path.append('..')  # add parent directory
import ballbeamParam as P


class ballController:
    def __init__(self):
        # Instantiates the PD object
        self.kptheta = P.kptheta
        self.kdtheta = P.kdtheta
        self.kpz = P.kpz
        self.kdz = P.kdz
        self.limit = P.Fmax

    def update(self, z_r, x):
        z = x.item(0)
        theta = x.item(1)
        zdot = x.item(2)
        thetadot = x.item(3)

        z_e = z
        F_e = (P.m1 * P.g) * z_e / P.length + P.m2 * P.g / 2

        theta_r = self.kpz * (z_r - z) - self.kdz * zdot

        F_tilde = self.kptheta * (theta_r - theta) - self.kdtheta * thetadot

        F = F_e + F_tilde

        F = self.saturate(F)

        return F

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit * np.sign(u)
        return u
