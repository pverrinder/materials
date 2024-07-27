#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:44 2024

@author: paul

"""

import matplotlib.pyplot as plt
from calcs import get_nk_data_yml

class AlSb:

    # Values taken from Coldren Table 1.1 and Appendix 11

    # **** Strain Parameters ****

    # Lattice constant 
    a = 6.1355  # [Å]

    # Deformation Potentials
    a_dp = 2.04    # [eV]
    b_dp = -1.35    # [eV]
    d_dp = -4.3    # [eV]

    # Elastic Moduli
    C11 = 8.769 # [10^11 dyn/cm^2]
    C12 = 4.341 # [10^11 dyn/cm^2]
    C44 = 4.076  # [10^11 dyn/cm^2]

    # Pressure coefficient of Eg
    dE_dP = -3.5    # [10^-6 eV/bar]

    Delta = 0.75   # [eV]

    #******************************

    # Bandgap energy, Eg, at 300 K
    Eg = 1.63	# [eV]

    # Effective Masses
    me = 0.33	# Electron effective mass
    mhh = 0.47  # Heavy hole effective mass
    mlh = 0.16	# Light hole effective mass
    msh = 0.24  # Split-off effective mass




if __name__ == "__main__":
    AlSb = AlSb()
    print('The lattice constant of AlSb is: ' + str(AlSb.a))
