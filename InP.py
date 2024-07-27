#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:44 2024

@author: paul

"""

import matplotlib.pyplot as plt
from calcs import get_nk_data_yml

class InP:

    # Values taken from Coldren Table 1.1 and Appendix 11

    # **** Strain Parameters ****

    # Lattice constant 
    a = 5.8688  # [Å]

    # Deformation Potentials
    a_dp = -6.16    # [eV]
    b_dp = -2.0     # [eV]
    d_dp = -5.0    # [eV]

    # Elastic Moduli
    C11 = 10.22 # [10^11 dyn/cm^2]
    C12 = 5.76  # [10^11 dyn/cm^2]
    C44 = 4.60  # [10^11 dyn/cm^2]

    # Pressure coefficient of Eg
    dE_dP = 8.5    # [10^-6 eV/bar]

    Delta = 0.10   # [eV]

    #******************************

    # Bandgap energy, Eg, at 300 K
    Eg = 1.351	# [eV]

    # Effective Masses
    me = 0.077  # Electron effective mass
    mhh = 0.61  # Heavy hole effective mass
    mlh = 0.12	# Light hole effective mass
    msh = 0.20  # Split-off effective mass



if __name__ == "__main__":
    InP = InP()
    print('The lattice constant of InP is: ' + str(InP.a))
