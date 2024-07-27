#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:44 2024

@author: paul

"""

import matplotlib.pyplot as plt
from calcs import get_nk_data_yml

class AlAs:

    # Values taken from Coldren Table 1.1 and Appendix 11

    # **** Strain Parameters ****

    # Lattice constant 
    a = 5.6611  # [Å]

    # Bandgap energy, Eg, at 300 K
    Eg = 2.153	# [eV]

    # Effective Masses
    me = 0.19	# Electron effective mass
    mhh = 0.48  # Heavy hole effective mass
    mlh = 0.2	# Light hole effective mass
    msh = 0.29  # Split-off effective mass

    # Deformation Potentials
    a_dp = -7.96    # [eV]
    b_dp = -1.5     # [eV]
    d_dp = -3.4    # [eV]

    # Elastic Moduli
    C11 = 12.02 # [10^11 dyn/cm^2]
    C12 = 5.70  # [10^11 dyn/cm^2]
    C44 = 5.89  # [10^11 dyn/cm^2]

    # Pressure coefficient of Eg
    dE_dP = 10.2    # [10^-6 eV/bar]

    Delta = 0.3    # [eV]

    #******************************




    valid_models = ['fern',
                    'rakic']

    # Get data for nk versus wavelength and return in a pandas dataframe
    def get_nk_data(self, 
                    model: None = None, 
                    wl_span: None = None,
                    num_points = 200):

        filePath = 'data-nk/AlAs/'
        if model == 'fern':
            nk = get_nk_data_yml(filePath + 'Fern.yml', wl_span=wl_span, num_points=num_points)
        elif model == 'rakic':
            nk = get_nk_data_yml(filePath + 'Rakic.yml', wl_span=wl_span, num_points=num_points)
        # Default to Rakic model
        else:
            nk = get_nk_data_yml(filePath + 'Rakic.yml', wl_span=wl_span, num_points=num_points)
            if model == None:
                print('No refractive index model specified. Default to Rakic.')
            else:
                print('Invalid model name. Choose one of: ' + str(self.valid_models))

        return nk


if __name__ == "__main__":
    AlAs = AlAs()
    print('The lattice constant of AlAs is: ' + str(AlAs.a))
    
    nk = AlAs.get_nk_data(model='rakic')
    
    wl = nk['wl']
    n = nk['n']
    
    
    plt.plot(wl, n)

    
