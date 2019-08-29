import math
import time
from tkinter import *
from multiprocessing import Process

## (2019-06-06) Created the class Point it is a class that can hold an X,Y,Z coordinate
#  and also 3 bands number. Created a class ListOfPoints witch can have multiple points
#  store for each object of it's kind
## (2019-06-07) Tested and fix some bugs that the class had. Add a method that make is so
#  you can find the index of the group a point is in. Ex: if you whant to fin the point 459325.056
#  you can enter it in the method getIndex and it will give you the index of the array the point is in.
#  I also added a method that will return true if a X coordinate is in the list and false otherwise.
## (2019-06-10) create the function findPoints witch take two ListOfPoint and try to associate the RGB
#  and the NDRE of the two file in one XYZ file. The final result is a XYZ file that as
#  X,Y,Z,R,G,B,RED_Edge,Nir,Garbage or X,Y,Z,RED_Edge,Nir,Garbage,R,G,B. For now the process is pretty slow.
#  Still got to make some test to make sure that the number in the file is somewhat accurate
## (2019-06-25) Created a new file that is the GUI of this application. By doing this I
#  dont need to go in the code cange the path file. The GUI id created using TKinter
#  wtich is the default GUI for python
## (2019-07-17) A real test has been process and it took 455230 secondes witch is
#   about 5 days. For the version 5 I am separating the task in two and computing them
#   in paralle so the computing time is almost cut in two. To do so I have use the multiprocessing
#   library. I have added the function stratProcessing and mergeAll. startProcessing is just a function that will
#   start the processing in two packages. mergeAll take the second file and append it to the first.
#   Version 6 is not so differant the only thing for now is that it split the task in 4.
#   Version 7 let you chose in how much slices you whant to split your programme.
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
        return self.B1

    def getB2(self):
        return self.B2

    def getB3(self):
        return self.B3

class ListOfPoint:

    baseX = 0
    points = []
    finalX = 0
    intervalSize = 0.1

    def __init__(self, name = None):
        if(name != None):
            self.createList(name)
        return None

    def createList(self,name):
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
                    currentX = round(currentX + self.intervalSize,1) 
                
                if(float(lineS[0]) < currentX):
                    self.points[index].append(Point(float(lineS[0]),float(lineS[1]),float(lineS[2]),float(lineS[3]),float(lineS[4]),float(lineS[5])))
                    line = file.readline()
            self.finalX = currentX
            

    def getList(self):
        return self.points
    def getBaseX(self):
        return self.baseX
    def getFianlX(self):
        return self.finalX
    
    def getIndex(self, num):

        first = float(self.points[0][0].getX())
        index = math.floor((num - self.baseX)*10) - math.floor((first-self.baseX)*10)
        maxIndex = len(self.points) - 1
        if(maxIndex < index):
            print("The number is to big")
            return False
        else:
            return index

    def isInList(self, num):
        index = self.getIndex(num)
        print(index)
        pointsList = self.points
        if(index == False):
            return False
        else:
            for i in range(len(pointsList[index])):
                if(num == pointsList[index][i].getX()):
                    return True
            return False


def findPoints(point1,point2,fileLocation,fileName,numOfProcessing, index):
    #Check witch file as the bigger minimum and set this one as the main file
    if(point1.getList()[0][0].getX() >= point2.getList()[0][0].getX()):
        firstList = point1
        secondList = point2
        master = "NDRE"
    else:
        firstList = point2
        secondList = point1
        master = "RGB"
    print("The main image is the " + master)

    distanceLimit = 0.001
    #These index is use to follow the main list and make sure it
    #dosent get out of bound
    currentGroup = math.floor(index*len(firstList.getList())/numOfProcessing)
    currentPoint = 0
    maxGroup = math.floor((index+1)*len(firstList.getList())/numOfProcessing)
    secondGroupIndex = secondList.getIndex(firstList.getList()[currentGroup][currentPoint].getX())

    filePath = fileLocation + "/" + str(index) + fileName
    with open(filePath, 'a') as file:
        while(currentGroup != maxGroup):
            #The biggest index of a certain group of the first list
            maxPoint = len(firstList.getList()[currentGroup])
            while(currentPoint != maxPoint):
                #reset the value that make the comparison
                closestDistanceValue = math.inf
                closestIndex = 0
                firstPoint = firstList.getList()[currentGroup][currentPoint]
                #number of point in a certain group of the second list
                comparisonNum = len(secondList.getList()[secondGroupIndex])
                for i in range(comparisonNum):
                    #Formula that calculate how close is two points
                    currentDistanceValue = math.sqrt((firstPoint.getX()-secondList.getList()[secondGroupIndex][i].getX())**2+(firstPoint.getY()-secondList.getList()[secondGroupIndex][i].getY())**2+(firstPoint.getZ()-secondList.getList()[secondGroupIndex][i].getZ())**2)
                    if(currentDistanceValue < closestDistanceValue):
                        closestDistanceValue = currentDistanceValue
                        closestIndex = i
                    if(currentDistanceValue <= distanceLimit):
                        closestIndex = i
                        print("break distance " + str(distanceLimit) + "m")
                        break
                secondPoint = secondList.getList()[secondGroupIndex][closestIndex]
                #write to the XYZ file
                
                file.writelines(str(firstPoint.getX()) + " " + str(firstPoint.getY()) + " " + str(firstPoint.getZ()) + " " + str(firstPoint.getB1()) + " " + str(firstPoint.getB2()) + " " + str(firstPoint.getB3()) + " " + str(secondPoint.getB1()) + " " + str(secondPoint.getB2()) + " " + str(secondPoint.getB3()) + '\n')    
                currentPoint = currentPoint + 1
            currentGroup = currentGroup + 1
            secondGroupIndex = secondGroupIndex + 1
            currentPoint = 0
            #break the loop if the second file get to the end of the points
            if(secondGroupIndex == len(secondList.getList())):
                print('Stop the loop the second list is done!')
                break
    return None

def startProcessing(NDREpoints,RGBpoints,filePathMerge,fileName, numProc):
    #This function split the processing load in multiples parts and excute
    #each part in parallel.
    
    global process
    process =[]
    for i in range(numProc):
        process.append(Process(target = findPoints, args =(NDREpoints, RGBpoints, filePathMerge, fileName,numProc, i  )))
    for j in process:
        j.start()
    for q in process:
        q.join()
        

def mergeAll(fileLocation, fileName, numProcess):
    #This function append all the files to the first one to give the final result
    filePaths = []
    for q in range(numProcess):
        filePaths.append(fileLocation + "/" + str(q) + fileName)
    
    with open(filePaths[0], 'a') as firstFile:
        for i in range(numProcess-1):
            with open(filePaths[i+1], 'r') as otherFile:
                otherFileContent = otherFile.readlines()
                for j in otherFileContent:
                    firstFile.writelines(j)

def stopAll():
    if(process != None):
        for i in process:
            i.terminate()












                
