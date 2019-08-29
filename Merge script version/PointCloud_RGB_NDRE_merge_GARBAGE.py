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



class ListOfPoints:

    listPoints = []
    minX = 0
    maxX = 0

    def __init__(self, minX, maxX):
        self.minX = minX
        self.maxX = maxX

    def addPoint(self, point):
        self.listPoints.append(point)
        return

    def getMin(self):
        return self.minX

    def getMax(self):
        return self.maxX

    def getList(self):
        return self.listPoints



def CreateListPoints(name):
    group = [None]
    index = 0
    
    with open(name, 'r') as file:
        baseX = float(file.read(10))
        baseX = math.floor(baseX)
        currentX = baseX
        file.seek(0)
        line = file.readline()
        while line != "":
            lineArray = line.split()
            if(currentX <= float(lineArray[0]) and currentX +0.1 > float(lineArray[0])):
                if(group[index] == None):
                    group[0] = ListOfPoints(currentX, currentX+0.1)
                    group[0].addPoint(Point(lineArray[0],lineArray[1],lineArray[2],lineArray[3],lineArray[4],lineArray[5]))
                    print("*")
                    
                elif (group[index].getMin() == currentX):
                    group[index].addPoint(Point(lineArray[0],lineArray[1],lineArray[2],lineArray[3],lineArray[4],lineArray[5]))
                    print("**")
                    
                elif(group[index].getMin() != currentX):
                    index += 1
                    group.append(ListOfPoints(currentX, currentX+0.1))
                    group[index].addPoint(Point(lineArray[0],lineArray[1],lineArray[2],lineArray[3],lineArray[4],lineArray[5]))
                    print("***")

                line = file.readline()
            else:
                currentX += 0.1
                print(currentX)
            


    return group



p1 = CreateListPoints("P:\PointCloud_RGB_NDRE_merge\RGB_NDRE_indexCaculator_group1_densified_point_cloud_NDRE.xyz")




    
