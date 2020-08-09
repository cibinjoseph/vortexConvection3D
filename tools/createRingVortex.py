#!/usr/bin/python3

""" Creates vortex coordinates for a vortex ring """
import numpy as np
import io

nFilaments = 60
radius = 1.0
zCoordinate = 0.0
xShift = 0.0
yShift = 1.0
thetaX = 0.0  # Rotation about X-axis after shift
thetaY = 20.0  # Rotation about Y-axis after shift
outputString = io.StringIO()

rotX = np.array([[1, 0, 0], \
                 [0,np.cos(np.deg2rad(thetaX)),-np.sin(np.deg2rad(thetaX))], \
                 [0,np.sin(np.deg2rad(thetaX)), np.cos(np.deg2rad(thetaX))]])
rotY = np.array([[np.cos(np.deg2rad(thetaY)),0,-np.sin(np.deg2rad(thetaY))], \
                 [0,1,0], \
                 [np.sin(np.deg2rad(thetaY)),0, np.cos(np.deg2rad(thetaY))]])

def rotate(coords):
    rotMat = rotY.dot(rotX)
    rows = np.shape(coords)
    for i in range(rows[0]):
        coords[i] = rotMat.dot(coords[i])
    return coords

# Create coordinates of a circle
thetas = np.linspace(0.0, 2.0*np.pi, nFilaments+1)
vRingStart = []
for theta in thetas:
    xyz = [radius*np.cos(theta) + xShift, \
           radius*np.sin(theta) + yShift, \
           zCoordinate]
    vRingStart.append(xyz)

vRingStart = np.array(vRingStart)
vRingStart = rotate(vRingStart)

# Create start and end points for 
# each filament in the vortex ring
vRingEnd = vRingStart[1:, :]
vRingStart = vRingStart[0:-1, :]

vortices = np.append(vRingStart, vRingEnd, axis=1)

# Print coordinates to stdout
np.savetxt(outputString, vortices)
print(outputString.getvalue())
outputString.close()
