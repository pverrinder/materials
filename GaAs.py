#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:44 2024

@author: paul

"""

import matplotlib.pyplot as plt
from calcs import get_nk_data_yml
from calcs import epsilon_adachi

def get_gaas_nk_data(model: None = None,
                    wl_span: None = None,
                    n_points = 200):

    filePath = 'data-nk/GaAs/'
    if model == 'adachi':
        nk = get_nk_data_yml(filePath + 'Adachi.yml', wl_span=wl_span, n_points=n_points)
    elif model == 'aspnes':
        nk = get_nk_data_yml(filePath + 'Aspnes.yml', wl_span=wl_span, n_points=n_points)
    elif model == 'papatryfonos':
        nk = get_nk_data_yml(filePath + 'Papatryfonos.yml', wl_span=wl_span, n_points=n_points)
    # Default to Adachi model
    else:
        nk = get_nk_data_yml(filePath + 'Adachi.yml', wl_span=wl_span, n_points=n_points)
        if model == None:
            print('No refractive index model specified. Default to Adachi.')
        else:
            print('Invalid model name. Choose one of: ' + str(self.valid_models))

    return nk 


class GaAs:

    name = 'GaAs'

    #******* Material Constants ******** 
    # Most values taken from Coldren Table 1.1 and Appendix 11

    # Lattice constant 
    a = 5.6533  # [Å]

    # Bandgap energy, Eg, at 300 K
    Eg = 1.424	# [eV]

    # Effective Masses
    me = 0.067	# Electron effective mass
    mhh = 0.38  # Heavy hole effective mass
    mlh = 0.09	# Light hole effective mass
    msh = 0.15  # Split-off effective mass

    # Deformation Potentials
    a_dp = -8.68    # [eV]
    b_dp = -1.7     # [eV]
    d_dp = -4.55    # [eV]

    # Elastic Moduli
    C11 = 11.88 # [10^11 dyn/cm^2]
    C12 = 5.38  # [10^11 dyn/cm^2]
    C44 = 5.94  # [10^11 dyn/cm^2]

    # Pressure coefficient of Eg
    dE_dP = 11.5    # [10^-6 eV/bar]

    Delta = 0.34    # [eV]

    #******************************


    #*** Model Parameters for Optical Dispersion Calculations According to Adachi 1989 *** 

    
    class adachi_consts:
        E0   = 1.42    #eV
        Δ0   = 1.77-E0 #eV
        E1   = 2.90    #eV
        Δ1   = 3.13-E1 #eV
        E2   = 4.7     #eV
        Eg   = 1.73    #eV
        A    = 3.45    #eV**1.5
        B1   = 6.37
        B11  = 13.08   #eV**-0.5
        Γ    = 0.10    #eV
        C    = 2.39
        γ    = 0.146
        D    = 24.2
        εinf = 1.6


    valid_models = ['adachi',
                    'aspnes',
                    'papatryfonos']

    # Get data for nk versus wavelength and return in a pandas dataframe
    def get_nk_data(self,
                    model: None = None,
                    wl_span: None = None,
                    n_points = 200):
        nk = get_gaas_nk_data(model=model, wl_span=wl_span, n_points=n_points)

        return nk
    
    #*** Calculate Optical Dispersion eps(hw) Using Adachi Model *** 
    def calculate_eps(self,
                      Eph = (0.1, 6),
                      n_points = 200):
        eps = epsilon_adachi.epsilon(self, Eph=Eph, n_points=n_points)
        return eps




if __name__ == "__main__":
    GaAs = GaAs()
    print('The lattice constant of GaAs is: ' + str(GaAs.a))


