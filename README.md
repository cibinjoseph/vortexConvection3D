# vortexConvection3D
A simple 3d simulation for vortex filament convection

## Working
`vortexSim.py` is the program that simulates motion of vortex filaments in 3-dimensional space.  
The vortex filament coordinates are read from the file `vortexFilaments.dat` 
in CSV format in the following form:
```
P1(x) P1(y) P1(z) P2(x) P2(y) P2(z)  gamma  vortexCoreRadius
```
where `P1(x,y,z)` and `P2(x,y,z)` are endpoints of the filament and gamma is the strength.

`vtx.py` contains the class definition for the Vortex class.  
`tools/` contains a few scripts for generating common geometries.

