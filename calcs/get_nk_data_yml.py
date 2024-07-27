#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import yaml
import numpy as np
import pandas as pd

def get_nk_data_yml(fileName, 
          wl_span: None = None,
          n_points = 200):
    
    """
    Description:
    fileName: path to the .csv data file
    wl_span: wavelength range in, or single wavelength over which to interpolate the data
             Can be either tuple (wl1, wl2) or single valued list [wl].
             If None, use the span of the whole data set.
             Units of µm
    num_points: number of points for interpolation
    """
    
    # Conversion factor for photon wavelength to photon energy 
    eV_conv = 1.23985 # [µm * eV]
    
    
    # Load the YAML file
    with open(fileName, 'r') as file:
        contents = yaml.safe_load(file)


    nk_data_str = contents['DATA'][0]['data']

    # Process the data string into a list of lists
    data_lines = nk_data_str.strip().split('\n')
    data = [list(map(float, line.split())) for line in data_lines]

    nk_data = np.array(data)
    
    rows, columns = nk_data.shape
    
    wl_data = nk_data[:,0]
    n_data = nk_data[:,1]
    if columns == 3:
        k_data = nk_data[:,2]
    else:
        k_data = np.zeros(rows)
        
    # If no wavelength span is specified, just use the whole data set
    if wl_span == None:
        wl_span = [min(wl_data), max(wl_data)]
        wl = np.linspace(wl_span[0], wl_span[1], n_points)
        Eph = eV_conv/wl
        n = np.interp(wl, wl_data, n_data)
        k = np.interp(wl, wl_data, k_data)      
    elif np.size(wl_span) == 1:
        wl = wl_span
        Eph = eV_conv/np.array(wl)
        n = np.interp(wl, wl_data, n_data)
        k = np.interp(wl, wl_data, k_data)
        if min(wl_span) < min(wl_data) or max(wl_span) > max(wl_data):
            print('WARNING: Wavelength span is beyond the range of the data. Interpolation results may not be accurate.')
    elif np.size(wl_span) == 2:
        mask = (wl_data >= wl_span[0]) & (wl_data <= wl_span[1])
        wl = np.linspace(wl_span[0], wl_span[1], n_points)
        Eph = eV_conv/wl
        n = np.interp(wl, wl_data[mask], n_data[mask])
        k = np.interp(wl, wl_data[mask], k_data[mask])  
        if min(wl_span) < min(wl_data) or max(wl_span) > max(wl_data):
            print('WARNING: Wavelength span is beyond the range of the data. Interpolation results may not be accurate.')
    else:
        print('wl_span must be a tuple (wl_min, wl_max) or a single value.')    
    
    # Combine everything into a data frame
    # wl units: [µm]
    # Energy units: [eV]
    nk_df = pd.DataFrame({
    'wl': wl,
    'n': n,
    'k': k,
    'E': Eph
    })
    
    return nk_df



