import math

class Geometric:
    def __init__(self):
        pass
    def __str__(self):
        pass
class TwoDimension(Geometric):
    def __init__(self):
        pass
    def getArea(self):
        pass
    def getPerimeter(self):
        pass
class Rectangle(TwoDimension):
    def __init__(self,sideLenght1,sideLength2):
        self.sideLength1=sideLenght1
        self.sideLength2=sideLength2
    def getArea(self):
        return self.sideLength1*self.sideLength2
    def getPerimeter(self):
        return 2*(self.sideLength1+self.sideLength2)
class square(Rectangle):
    def __init__(self,sideLenght):
        self.sideLength=sideLenght
    def getArea(self):
        return self.sideLength**2
    def getPerimeter(self):
        return 4 * self.sideLength
class circle(TwoDimension):
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        return math.pi*(self.radius)**2
    def getPerimeter(self):
        return 2*math.pi*self.radius
class Annulus(circle):
    def __init__(self,innerRadius,outerRadius):
        self.innerRadius=innerRadius
        self.outerRadius=outerRadius
    def getArea(self):
        return math.pi*((self.outerRadius**2)-(self.innerRadius**2))
    def getPerimeter(self):
        return 2* math.pi(self.outerRadius+self.innerRadius)
class EquilateralTriangle(TwoDimension):
    def __init__(self,sideLength):
        self.sideLength=sideLength
    def getArea(self):
        return (math.sqrt(3)/4)*(self.sideLength)**2
    def getPerimeter(self):
        return 3*self.sideLength

#three dimension

class threeDimension(Geometric):
    def getSurfaceArea(self):
        pass
    def getVolume(self):
        pass
    def getSaToVolRatio(self):
        return self.getSurfaceArea()/self.getVolume()
class Tetrahedron(threeDimension):
    def __init__(self,sideLength):
        self.sideLength=sideLength
    def getVolume(self):
        return (self.sideLength**3)/(6*math.sqrt(2))
    def getSurfaceArea(self):
        return math.sqrt(3)*((self.sideLength)**2)
class Icosahedron(threeDimension):
    def __init__(self,sideLength):
        self.sideLength=sideLength
    def getVolume(self):
        return 5*(3+math.sqrt(5))*(self.sideLength)**3/12
    def getSurfaceArea(self):
        return 5*math.sqrt(3)*self.sideLength**2
class Octahedron(threeDimension):
    def __init__(self,sideLength):
        self.sideLength=sideLength
    def getVolume(self):
        return (math.sqrt(2)/3)* self.sideLength**3
    def getSurfaceArea(self):
        return 2*math.sqrt(3)* self.sideLength**2
class Cube(threeDimension):
    def __init__(self,sideLength):
        self.sideLength=sideLength
    def getVolume(self):
        return self.sideLength**3
    def getSurfaceArea(self):
        return 6*(self.sideLength**2)










