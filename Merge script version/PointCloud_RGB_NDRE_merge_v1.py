import math

# (2019-06-06) Created the class Point it is a class that can hold an X,Y,Z coordinate
#  and also 3 bands number. Created a class ListOfPoints witch can have multiple points
#  store for each object of it's kind
class Point:
    __X = 0
    __Y = 0
    __Z = 0
    __B1 = 0
    __B2 = 0
    __B3 = 0

    def __init__(self, X, Y, Z, B1, B2, B3):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.B1 = B1
        self.B2 = B2
        self.B3 = B3

    def __str__(self):
        p = "x: " + str(self.X) + " y: " + str(self.Y) + " z: "+ str(self.Z) + " B1: "+ str(self.B1)+ " B2: "+ str(self.B2)+ " B3: "+ str(self.B3)
        return p

    def __repr__(self):
        p = "x: " + str(self.X) 
        return p

    def getX(self):
        return self.X
    
    def getY(self):
        return self.Y
    
    def getZ(self):
        return self.Z

    def getB1(self):
        return self.X

    def getB2(self):
        return self.X

    def getB3(self):
        return self.X

class ListOfPoint:

    __baseX = 0
    __points = []
    __finalX = 0
    
    def __init__(self,name):
        with open(name, 'r') as file:
            index = 0
            self.points = [[]]
            self.baseX = float(file.read(10))
            self.baseX = math.floor(self.baseX)
            
            currentX = self.baseX
            file.seek(0)
            line = file.readline()
            while line != "":
                ## One line of a the txt file with all the numbers in an array
                lineS = line.split()
                if(float(lineS[0]) >= currentX ):
                    if(len(self.points[index]) != 0):
                        self.points.append([])
                        index += 1
                    currentX = round(currentX + 0.1,1) 
                print(currentX)
                if(float(lineS[0]) < currentX):
                    self.points[index].append(Point(lineS[0],lineS[1],lineS[2],lineS[3],lineS[4],lineS[5]))
                    line = file.readline()
            self.finalX = currentX

    def getPoints(self):
        return self.points
    def getBaseX(self):
        return self.baseX
    def getFianlX(self):
        return self.finalX


def run():
    ##p1 = ListOfPoint('P:\PointCloud_RGB_NDRE_merge\!RGB_NDRE_indexCaculator_group2_densified_point_cloud_RGB.xyz')
    p1 = ListOfPoint('P:\PointCloud_RGB_NDRE_merge\!RGB_NDRE_indexCaculator_group1_densified_point_cloud_NDRE.xyz')

    
    currentGroup = 0
    currentIndex = 0
    maxGroup = len(p1.getPoints())
    currentPoint = p1.getPoints()[currentGroup][currentIndex]
    
##    while currentGroup != maxGroup and currentIndex != maxIndex:
##        closest = math.inf



        
    return p1

p1 = run()
