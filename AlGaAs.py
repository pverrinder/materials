#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.constants import hbar, c, pi
from GaAs import GaAs

class AlGaAs:
    # Model based on Adachi 1985. Plans to add other options later

    """
    TODO:
        - Warn users if wavelength range goes past the bandgap energy.
        - Finish refractive index calculations
        - Review literature to see if there are other useful models/data
        besides Adachi and add options to use those values instead. This could
        be in a separate class, or just an option in this class (maybe
        thats's better...)
        -
    """
    def __init__(self, x, wlmin, wlmax, wlpnts):
        # Al fraction in AlxGaAs
        self.x = x
        self.a = GaAs.a + 0.0078*x

        # Bandgap Energy
        if x <= 0.45:
            self.Eg = GaAs.Eg + 1.247*x
        else:
            self.Eg = 1.900 + 0.125*x + 0.143*x**2

        # Critical point energy
        self.E0 = GaAs.E0 + 1.155*x + 0.37*x**2
        self.E0_D0 = GaAs.E0_D0 + 1.115*x + 0.37*x**2

        # Effective masses
        self.me = GaAs.me + 0.083*x
        self.mlh = GaAs.mlh + 0.063*x
        self.mhh = GaAs.mhh + 0.14*x
        self.mso = GaAs.mso + 0.09*x

        # Calculate refractive index as a function of composition

        # Wavelength (µm)
        wl = np.linspace(wlmin, wlmax, wlpnts)
        # Frequency (rad/s)
        w = 2*pi*c/wl


        A0 = 6.3 + 19.0*x
        B0 = 9.4 - 10.2*x

        # Real part of dielectric constant 
        #eps = ...

if __name__ == "__main__":
    AlGaAs = AlGaAs(x=0.3)

    print('The Bandgap of Al0.3GaAs is: ' + str(AlGaAs.Eg))
