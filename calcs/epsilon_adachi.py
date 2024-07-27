#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:47:23 2024

@author: paul
"""

"""
This file contains the functions for calculating epsilon for III-V compounds
according to Adachi 1989.
Reference: Adachi, S. (1989). Optical dispersion relations for GaP, GaAs, GaSb,
InP, InAs, InSb, Al xGa1-xAs, and In1-xGaxAs yP1-y. Journal of Applied Physics,
66(12), 6030–6040. https://doi.org/10.1063/1.343580
"""

import numpy as np

# Heviside function
def H(x):
    return 0.5 * (np.sign(x) + 1)


def Epsilon_A(eV,
              mat): #E0
    """
    Arguments:
        E: photon energy [eV]
        mat: material object containing relevant constants
    """
    χ0 = eV/mat.E0
    χso = eV / (mat.E0+mat.Δ0)
    H0 = H(1-χ0)
    Hso = H(1-χso)
    fχ0 = χ0**-2 * ( 2 -(1+χ0)**0.5 - ((1-χ0)*H0)**0.5 )
    fχso = χso**-2 * ( 2 - (1+χso)**0.5 - ((1-χso)*Hso)**0.5 )
    H0 = H(χ0-1)
    Hso = H(χso-1)
    ε2 = mat.A/(eV)**2 * ( ((eV-mat.E0)*H0)**0.5 + 0.5*((eV-mat.E0-mat.Δ0)*Hso)**0.5)
    ε1 = mat.A*mat.E0**-1.5 * (fχ0+0.5*(mat.E0/(mat.E0+mat.Δ0))**1.5*fχso)
    return ε1 + 1j*ε2


def Epsilon_B(eV,
              mat): #E1
    # ignoring E1+Δ1 contribution - no data on B2 & B21 in the paper
    # result seems to reproduce graphical data from the paper
    χ1 = eV/mat.E1
    H1 = H(1-χ1)
    ε2 = np.pi*χ1**-2*(mat.B1-mat.B11*((mat.E1-eV)*H1)**0.5)
    ε2 *= H(ε2) #undocumented trick: ignore negative ε2
    χ1 = (eV+1j*mat.Γ)/mat.E1
    ε1 = -mat.B1*χ1**-2*np.log(1-χ1**2)
    return ε1.real + 1j*ε2.real

def Epsilon_C(eV,
              mat): #E2
    χ2 = eV/mat.E2
    ε2 = mat.C*χ2*mat.γ / ((1-χ2**2)**2+(χ2*mat.γ)**2)
    ε1 = mat.C*(1-χ2**2) / ((1-χ2**2)**2+(χ2*mat.γ)**2)
    return ε1 + 1j*ε2

def Epsilon_D(eV,
              mat): #Eg
    # ignoring ħωq - no data in the paper
    # result seems to reproduce graphical data from the paper
    Ech = mat.E1
    χg = mat.Eg/eV
    χch = eV/Ech
    Hg = H(1-χg)
    Hch = H(1-χch)
    ε2 = mat.D/eV**2 * (eV-mat.Eg)**2 * Hg * Hch
    return 1j*ε2




def epsilon(obj,
            Eph = (0.1, 6),
            n_points = 200):

    # Get the Adachi material constants from the obj class passed as an argument 
    mat = obj.adachi_consts()

    if np.size(Eph) == 2:
        ev_min=Eph[0]
        ev_max=Eph[1]
        eV = np.linspace(ev_min, ev_max, n_points)
    elif np.size(Eph) == 1:
        eV = Eph
    else:
        print('Eph must be a tuple (Emin, Emax) or single value.')

    #μm = 4.13566733e-1*2.99792458/eV
    εA  = Epsilon_A(eV, mat)
    εB  = Epsilon_B(eV, mat)
    εC  = Epsilon_C(eV, mat)
    εD  = Epsilon_D(eV, mat)
    ε = εA + εB + εC + εD + mat.εinf
    n = (ε**.5).real
    k = (ε**.5).imag
    #α = 4*π*k/μm*1e4 #1/cm

    a = obj.a
    eps = 1.2

    return ε

