import numpy as np
from matplotlib import pyplot as plt
from scipy import special

def calc_channel_resistance(mu,Dp,porosity,radius, length,channel_radius,Qin, vw):
   #calculates resistance in a cylindrical tube with porous walls
   #assumptions constant wall permeability and constant wall veolcity

    #K = (Dp ** 2. / 180.) * ((porosity ** 3.) / (1. - porosity) ** 2.) #permeability
    #gamma = 1. / (1. + 2.5 * (1. - porosity))
    #area = np.pi * radius ** 2.

    resistance_channel=((8*mu*length)/(np.pi*channel_radius^4))*(1-((2*np.pi*channel_radius*length*vw)/2*Qin))

    return resistance_channel

