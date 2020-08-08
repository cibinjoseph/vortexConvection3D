#!/usr/bin/python3

""" Creates vortex coordinates for a vortex ring """
import numpy as np

radius = 1.1
zCoordinate = 0.0
nFilaments = 25
filename = 'vortexFilaments.dat'

# Create coordinates of a circle
thetas = np.linspace(0.0, 2.0*np.pi, nFilaments)
vRingStart = []
for theta in thetas:
    xyz = [radius*np.cos(theta), radius*np.sin(theta), zCoordinate]
    vRingStart.append(xyz)

# Create start and end points for 
# each filament in the vortex ring
vRingStart = np.array(vRingStart)
vRingEnd = vRingStart[1:, :]
vRingStart = vRingStart[0:-1, :]

vortices = np.append(vRingStart, vRingEnd, axis=1)

np.savetxt(filename, vortices)
