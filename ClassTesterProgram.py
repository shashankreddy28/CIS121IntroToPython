"""
Shashank Reddy
4/07/23

This code will test your created classes
"""

from lab12 import Tetrahedron
from lab12 import Cube
from lab12 import Octahedron
from lab12 import Icosahedron
def ComparegetSaToVolRatio(commonSideLength):
	tetrahedron = Tetrahedron(commonSideLength)
	print("The SA:V of a tetrahedron is " +str(tetrahedron.getSaToVolRatio()))
	
	cube = Cube(commonSideLength)
	print("The SA:V of a cube is " +str(cube.getSaToVolRatio()))

	octahedron = Octahedron(commonSideLength)
	print("The SA:V of a octahedron is " +str(octahedron.getSaToVolRatio()))

	icosahedron = Icosahedron(commonSideLength)
	print("The SA:V of a icosahedron is " +str(icosahedron.getSaToVolRatio()))


ComparegetSaToVolRatio(1)
ComparegetSaToVolRatio(10)
ComparegetSaToVolRatio(25.6)
