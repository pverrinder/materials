#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:44 2024

@author: paul

"""

import matplotlib.pyplot as plt
from calcs import get_nk_data_yml

class AlP:

    # Values taken from Coldren Table 1.1 and Appendix 11

    # **** Strain Parameters ****

    # Lattice constant 
    a = 5.4635  # [Å]

    # Deformation Potentials
    a_dp = -8.38    # [eV]
    b_dp = -1.75    # [eV]
    d_dp = -4.8    # [eV]

    # Elastic Moduli
    C11 = 13.2 # [10^11 dyn/cm^2]
    C12 = 6.3  # [10^11 dyn/cm^2]
    C44 = 6.15  # [10^11 dyn/cm^2]

    # Pressure coefficient of Eg
    dE_dP = 9.75    # [10^-6 eV/bar]

    Delta = 0.10   # [eV]

    #******************************

    # Bandgap energy, Eg, at 300 K
    Eg = 2.41	# [eV]

    # Effective Masses
    me = 0.21	# Electron effective mass
    mhh = 0.51  # Heavy hole effective mass
    mlh = 0.21	# Light hole effective mass
    msh = 0.3   # Split-off effective mass


if __name__ == "__main__":
    AlP = AlP()
    print('The lattice constant of AlP is: ' + str(AlP.a))
