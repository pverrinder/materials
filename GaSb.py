#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:44 2024

@author: paul

"""

import matplotlib.pyplot as plt
from calcs import get_nk_data_yml

class GaSb:

    # Values taken from Coldren Table 1.1 and Appendix 11

    # **** Strain Parameters ****

    # Lattice constant 
    a = 6.0959  # [Å]

    # Deformation Potentials
    a_dp = -8.28    # [eV]
    b_dp = -1.8    # [eV]
    d_dp = -4.6    # [eV]

    # Elastic Moduli
    C11 = 8.842 # [10^11 dyn/cm^2]
    C12 = 4.026 # [10^11 dyn/cm^2]
    C44 = 4.322  # [10^11 dyn/cm^2]

    # Pressure coefficient of Eg
    dE_dP = 14.7    # [10^-6 eV/bar]

    Delta = 0.8   # [eV]

    #******************************

    # Bandgap energy, Eg, at 300 K
    Eg = 0.70	# [eV]

    # Effective Masses
    me = 0.041	# Electron effective mass
    mhh = 0.27  # Heavy hole effective mass
    mlh = 0.05	# Light hole effective mass
    msh = 0.08  # Split-off effective mass




if __name__ == "__main__":
    GaSb = GaSb()
    print('The lattice constant of GaSb is: ' + str(GaSb.a))
