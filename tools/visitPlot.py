# Run this using visit -s
OpenDatabase("Results/vortices*.plt database")
AddPlot("Mesh", "mesh", 1, 1)

# Line colour
MeshAtts = MeshAttributes()
MeshAtts.lineWidth = 4
MeshAtts.meshColor = (51, 102, 255, 255)
MeshAtts.meshColorSource = MeshAtts.MeshCustom
SetPlotOptions(MeshAtts)

# 3D Axis
# aatts = AnnotationAttributes()
# aatts.axes3D.visible = 1
# SetAnnotationAttributes(aatts)
DrawPlots()
