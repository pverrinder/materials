#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from GaAs import GaAs

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

def plot_nk_vs_wl(nk, title='', saveFig=False):
    
    # Create the figure and the first axis
    fig, ax1 = plt.subplots()

    # Plot the data for the left y-axis
    ax1.plot(nk['wl'], nk['n'], color=colors[0], label='n') 
    ax1.set_xlabel('Wavelength [µm]')
    ax1.set_ylabel('n', color=colors[0])
    ax1.tick_params(axis='y', labelcolor=colors[0])
    ax1.grid(True)

    # Create the second y-axis
    ax2 = ax1.twinx()  # This creates a second y-axis that shares the same x-axis

    # Plot the data for the right y-axis
    ax2.plot(nk['wl'], nk['k'], color=colors[1], label='k')
    ax2.set_ylabel('k', color=colors[1])
    ax2.tick_params(axis='y', labelcolor=colors[1])
    
    # Add legends for both plots
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

    # Display the plot
    plt.title(title)
    plt.show()


# Create GaAs material object
GaAs = GaAs()

# Print the valid model names
print('Valid models for nk data are: {}'.format(GaAs.valid_models))


# Plot dispersion relations
nk_adachi = GaAs.get_nk_data(model=GaAs.valid_models[0])
nk_aspnes = GaAs.get_nk_data(model=GaAs.valid_models[1])
nk_papa = GaAs.get_nk_data(model=GaAs.valid_models[2])



# Adachi
plot_nk_vs_wl(nk_adachi, title='GaAs nk: Adachi')

# Aspnes
plot_nk_vs_wl(nk_aspnes, title='GaAs nk: Aspnes')

# Papatryfonos
plot_nk_vs_wl(nk_aspnes, title='GaAs nk: Papatryfonos')