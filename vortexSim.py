#!/usr/bin/python3

""" Simulates motion of vortices """
import vtx
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.animation as animation
from mpl_toolkits.mplot3d import axes3d
from celluloid import Camera

def getCoords(vts):
    """ Get coordinates of vortices in x, y, z form """
    coords = [[], [], []]
    for vt in vts:
        coords = vt.appCoords(coords)
    return coords

vtxFilamentsFilename = 'vortexFilaments.dat'
animationFilename = 'output.gif'
dt = 0.01
nt = 10

# Read coordinates of vortices 
vts = np.loadtxt(vtxFilamentsFilename)
shape = np.shape(vts)
nVortices = shape[0]
print('Total vortices found: ' + str(nVortices))

# Initialize vortices
vortx = []
if shape[1] == 6:
    for vt in vts:
        vortx.append(vtx.Vtx([vt[0], vt[1], vt[2]], \
                             [vt[3], vt[4], vt[5]], \
                             1.0, 0.0))
elif shape[1] == 8:
    for vt in vts:
        vortx.append(vtx.Vtx([vt[0], vt[1], vt[2]], \
                             [vt[3], vt[4], vt[5]], \
                             vt[6], vt[7]))
else:
    raise ValueError('Wrong number of columns in vortex coordinate file')

fig = plt.figure()
ax = plt.axes(projection='3d')
camera = Camera(fig)
for i in range(nt):
    print(str(i+1) + '/' + str(nt))
    coords = getCoords(vortx)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    ax.plot(coords[0],coords[1],coords[2],'b')
    camera.snap()

    for vt in vortx:
        for vtOther in vortx:
            vt.addInfluenceBy(vtOther)

    for vt in vortx:
        vt.update(dt)

animation = camera.animate()
animation.save('output.gif', writer='imagemagick')
