#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:44 2024

@author: paul

"""

import matplotlib.pyplot as plt
from calcs import get_nk_data_yml
from calcs import epsilon_adachi

class InAs:

    name = 'InAs'
    # Values taken from Coldren Table 1.1 and Appendix 11

    # **** Strain Parameters ****

    # Lattice constant 
    a = 6.0583  # [Å]

    # Bandgap energy, Eg, at 300 K
    Eg = 0.359	# [eV]

    # Effective Masses
    me = 0.027	# Electron effective mass
    mhh = 0.34  # Heavy hole effective mass
    mlh = 0.027 # Light hole effective mass
    msh = 0.05  # Split-off effective mass

    # Deformation Potentials
    a_dp = -5.79    # [eV]
    b_dp = -1.8     # [eV]
    d_dp = -3.6    # [eV]

    # Elastic Moduli
    C11 = 8.329 # [10^11 dyn/cm^2]
    C12 = 4.526  # [10^11 dyn/cm^2]
    C44 = 3.959  # [10^11 dyn/cm^2]

    # Pressure coefficient of Eg
    dE_dP = 10.0    # [10^-6 eV/bar]

    Delta = 0.371    # [eV]

    #******************************

    """ Model Parameters for Optical Dispersion Calculations According to Adachi 1989 """
    class adachi_consts:
        E0   = 0.36    #eV
        Δ0   = 0.76-E0 #eV
        E1   = 2.50    #eV
        Δ1   = 2.78-E1 #eV
        E2   = 4.45     #eV
        Eg   = 1.07    #eV
        A    = 0.61    #eV**1.5
        B1   = 6.59
        B11  = 13.76   #eV**-0.5
        Γ    = 0.21    #eV
        C    = 1.78
        γ    = 0.108
        D    = 20.8
        εinf = 2.8


    valid_models = ['adachi',
                    'aspnes',
                    'lorimor']

    """ Calculate Optical Dispersion eps(hw) Using Adachi Model """
    def calculate_eps(self,
                      Eph = (0.1, 6),
                      n_points = 200):
        eps = epsilon_adachi.epsilon(self, Eph=Eph, n_points=n_points)
        return eps

    # Get data for nk versus wavelength and return in a pandas dataframe
    def get_nk_data(self,
                    model: None = None,
                    wl_span: None = None,
                    n_points = 200):

        filePath = 'data-nk/InAs/'
        if model == 'adachi':
            nk = get_nk_data_yml(filePath + 'Adachi.yml', wl_span=wl_span, n_points=n_points)
        elif model == 'aspnes':
            nk = get_nk_data_yml(filePath + 'Aspnes.yml', wl_span=wl_span, n_points=n_points)
        elif model == 'lorimor':
            nk = get_nk_data_yml(filePath + 'Lorimor.yml', wl_span=wl_span, n_points=n_points)
        # Default to Adachi model
        else:
            nk = get_nk_data_yml(filePath + 'Adachi.yml', wl_span=wl_span, n_points=n_points)
            if model == None:
                print('No refractive index model specified. Default to Adachi.')
            elif model != self.valid_models[0] and model != self.valid_models[1] and model != self.valid_models[2]:
                print('Invalid model name. Choose one of: ' + str(self.valid_models))

        return nk



if __name__ == "__main__":
    InAs = InAs()
    print('The lattice constant of InAs is: ' + str(InAs.a))

    eps = InAs.calculate_eps()
    print(eps)
    nk_aspnes = InAs.get_nk_data(model='aspnes')
    nk_adachi = InAs.get_nk_data(model='adachi', wl_span=[0.25,1.0])
    #nk = GaAs.get_nk_data(model='adachi')

    wl_aspnes = nk_aspnes['wl']
    n_aspnes = nk_aspnes['n']

    wl_adachi = nk_adachi['wl']
    n_adachi = nk_adachi['n']

    plt.plot(wl_aspnes, n_aspnes)
    plt.show()

    plt.plot(wl_adachi, n_adachi)
    plt.show()

