#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:44 2024

@author: paul

"""

import matplotlib.pyplot as plt
from calcs import get_nk_data_yml

class GaP:
    
    # Values taken from Coldren Table 1.1 and Appendix 11

    # **** Strain Parameters ****

    # Lattice constant 
    a = 5.4512  # [Å]

    # Deformation Potentials
    a_dp = -9.76    # [eV]
    b_dp = -1.5     # [eV]
    d_dp = -4.6    # [eV]

    # Elastic Moduli
    C11 = 14.12 # [10^11 dyn/cm^2]
    C12 = 6.253 # [10^11 dyn/cm^2]
    C44 = 7.047 # [10^11 dyn/cm^2]

    # Pressure coefficient of Eg
    dE_dP = 11.0    # [10^-6 eV/bar]

    Delta = 0.10   # [eV]

    #******************************

    # Bandgap energy, Eg, at 300 K
    Eg = 2.272	# [eV]

    # Effective Masses
    me = 0.254	# Electron effective mass
    mhh = 0.67  # Heavy hole effective mass
    mlh = 0.17	# Light hole effective mass
    msh = 0.46  # Split-off effective mass




if __name__ == "__main__":
    GaP = GaP()
    print('The lattice constant of GaP is: ' + str(GaP.a))
