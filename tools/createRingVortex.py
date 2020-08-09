#!/usr/bin/python3

""" Creates vortex coordinates for a vortex ring """
import numpy as np
import io

radius = 1.0
zCoordinate = 0.5
nFilaments = 25
outputString = io.StringIO()

# Create coordinates of a circle
thetas = np.linspace(0.0, 2.0*np.pi, nFilaments+1)
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

# Print coordinates to stdout
np.savetxt(outputString, vortices)
print(outputString.getvalue())
outputString.close()
