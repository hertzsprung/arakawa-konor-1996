#!/usr/bin/env python3
import math
import numpy as np

p0 = 1000e2 # Pa
p_top = 1e2
T0 = 250 # K
g0 = 9.81 # ms^-2
R = 287 #Jkg^-1K^-1
a = 6.3712e6 # m
H = R * T0 / g0
cp = 1000 # Jkg^-1K^-1

# from http://www.staff.science.uu.nl/~delde102/BruntVaisalaFrequencyIsothermalAtmosphere.pdf
def brunt_vaisala():
    return math.sqrt(g0*g0/(cp*T0))

def isothermal_hydrostatic_pressure(Z):
    return p0 * math.exp(-Z/(R * T0/g0))

def geopotential_height(p):
    return -H * math.log(p/p0)

def to_geopotential(z):
    return a * z / (a + z)

def to_geometric(Z):
    return a * Z / (a - Z)

#for z in np.linspace(0, to_geopotential(50.927e3), num=40):
#    p = isothermal_hydrostatic_pressure(z)
#    print(z, p, math.log(p))

log_p0 = math.log(p0)
log_p_top = math.log(p_top)

p = [math.exp(log_p) for log_p in np.linspace(log_p0, log_p_top, num=40)]
theta = [T0 * math.pow(p0/p_k, R/cp) for p_k in p]
z = [to_geometric(geopotential_height(p_k)) for p_k in p]

dz = [top - bottom for bottom, top in zip(z[:-1], z[1:])]
#print(dz)
#print(list(zip(z, p, theta)))
print(brunt_vaisala())
