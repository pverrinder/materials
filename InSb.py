#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:44 2024

@author: paul

"""

import matplotlib.pyplot as plt
from calcs import get_nk_data_yml

class InSb:

    # Values taken from Coldren Table 1.1 and Appendix 11

    # **** Strain Parameters ****

    # Lattice constant 
    a = 6.4794  # [Å]

    # Deformation Potentials
    a_dp = -7.57    # [eV]
    b_dp = -2.0    # [eV]
    d_dp = -4.8    # [eV]

    # Elastic Moduli
    C11 = 6.47 # [10^11 dyn/cm^2]
    C12 = 3.65 # [10^11 dyn/cm^2]
    C44 = 3.02  # [10^11 dyn/cm^2]

    # Pressure coefficient of Eg
    dE_dP = 16.5    # [10^-6 eV/bar]

    Delta = 0.98   # [eV]

    #******************************

    # Bandgap energy, Eg, at 300 K
    Eg = 0.175	# [eV]

    # Effective Masses
    me = 0.014	# Electron effective mass
    mhh = 0.34  # Heavy hole effective mass
    mlh = 0.016	# Light hole effective mass
    msh = 0.03  # Split-off effective mass



if __name__ == "__main__":
    InSb = InSb()
    print('The lattice constant of InSb is: ' + str(InSb.a))
