""" Class definition for vortex """
import numpy as np


eps = np.finfo(float).eps
tol = 1.0E-6
inv4pi = 0.25/np.pi

class Vtx:
    P1 = np.array([0,0,0])
    P2 = np.array([0,0,0])
    gam = 1.0
    rc = 0.0
    vel1 = 0.0
    vel2 = 0.0

    def __init__(self, P1, P2, gam=1.0, rc=0.0):
        self.P1 = np.array(P1)
        self.P2 = np.array(P2)
        self.gam = gam
        self.vel1 = 0.0
        self.vel2 = 0.0
        if rc < eps:
            self.rc = 1E-6
        else:
            self.rc = rc

    def vind(self, P):
        """ Induced velocity at P """
        r1 = P-self.P1
        r2 = P-self.P2

        r1Xr2 = np.cross(r1,r2)
        r1Xr2Abs2 = np.dot(r1Xr2, r1Xr2)

        vel = np.array([0.0, 0.0, 0.0])
        if r1Xr2Abs2 > tol:
            r0 = r1-r2
            r1Unit = r1/np.linalg.norm(r1)
            r2Unit = r2/np.linalg.norm(r2)
            vel = self.gam*r1Xr2*inv4pi*np.dot(r0, r1Unit-r2Unit) / \
                    np.sqrt((self.rc*np.linalg.norm(r0))**4.0 + r1Xr2Abs2**2.0)
        return vel

    def move(self, vec1, vec2):
        """ Move the vortex points by vec1 and vec2 """
        self.P1 = self.P1 + vec1
        self.P2 = self.P2 + vec2

    def addInfluenceBy(self, vtx2):
        vel1, vel2 = vtx2.vind(self.P1), vtx2.vind(self.P2)
        self.vel1 = self.vel1 + vel1
        self.vel2 = self.vel2 + vel1

    def update(self, dt):
        self.move(self.vel1*dt, self.vel2*dt)
        self.vel1 = 0.0
        self.vel2 = 0.0

    def appCoords(self, coords):
        if coords is not [[],[],[]]:
            coords[0].append(np.nan)
            coords[1].append(np.nan)
            coords[2].append(np.nan)
        coords[0].extend([self.P1[0], self.P2[0]])
        coords[1].extend([self.P1[1], self.P2[1]])
        coords[2].extend([self.P1[2], self.P2[2]])
        return coords

    def getStrXYZ(self):
        xyz1 = str(self.P1[0])+' '+str(self.P1[1])+' '+str(self.P1[2])
        xyz2 = str(self.P2[0])+' '+str(self.P2[1])+' '+str(self.P2[2])
        return xyz1, xyz2
