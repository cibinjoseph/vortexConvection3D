# Run this using visit -s
OpenDatabase("Results/vortices*.plt database")
AddPlot("Mesh", "mesh", 1, 1)
aatts = AnnotationAttributes()
aatts.axes3D.visible = 1
SetAnnotationAttributes(aatts)
DrawPlots()
