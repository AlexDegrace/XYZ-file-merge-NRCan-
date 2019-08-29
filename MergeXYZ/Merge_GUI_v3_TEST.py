from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import time

## (2019-07-17) This programme is the GUI that go with the programme
#   "PointCloud_RGB_NDRE_merge_vX" where X is the version. This cersion of the
#   GUI is for the version 7.
## (2019-07-18) I have added a stop button that stop all process and a slider button that
#   let you choose in how many process you whant to split your programme.

###### Bug : one Tkinter window open for each slices of the programme

merge = __import__('PointCloud_RGB_NDRE_merge_v7')

class Root(Tk):
    
    def __init__(self):
        super(Root,self).__init__()
        
        self.title("Merge NDRE and RGB .xyz file")
        self.configure(background='white')

        #The first frame from the top
        self.topFrame = Frame(self, background="white")
        self.topFrame.pack(side = TOP)

        #This create the tow label and the button for NDRE file selection
        self.NDRElabel = Label(self.topFrame, text = "Choose the NDRE file", background="white")
        self.NDRElabel.pack(side = LEFT, padx = 10, pady= 10)
        self.NDREbutton = Button(self.topFrame, text = "Browse Files", command = self.fileDialogNDRE, background="gray5", foreground = "white")
        self.NDREbutton.pack(side = LEFT, padx = 10, pady= 10)
        self.NDREfileLabel = Label(self.topFrame, text = "", background="white")
        self.NDREfileLabel.pack(side = LEFT, padx = 10, pady= 10)

        #The first frame from the top
        self.secondFrame = Frame(self, background="white")
        self.secondFrame.pack(side = TOP)
        
        #This create the tow label and the button for RGB file selection
        self.RGBlabel = Label(self.secondFrame, text = "Choose the RGB file", background="white")
        self.RGBlabel.pack(side = LEFT, padx = 10, pady= 10)
        self.RGBbutton = Button(self.secondFrame, text = "Browse Files", command = self.fileDialogRGB, background="gray5", foreground = "white")
        self.RGBbutton.pack(side = LEFT, padx = 10, pady= 10)
        self.RGBfileLabel = Label(self.secondFrame, text = "", background="white")
        self.RGBfileLabel.pack(side = LEFT, padx = 10, pady= 10)

        #The third frame from the top
        self.thirdFrame = Frame(self, background="white")
        self.thirdFrame.pack(side = TOP)

        #This create the tow label and the button for the location of the
        #merge file after processing
        self.locationLabel = Label(self.thirdFrame, text = "Choose the merge file location", background="white")
        self.locationLabel.pack(side = LEFT, padx = 10, pady= 10)
        self.locationButton = Button(self.thirdFrame, text = "Browse Folders", command = self.fileDialogLocation, background="gray5", foreground = "white")
        self.locationButton.pack(side = LEFT, padx = 10, pady= 10)
        self.locationFileLabel = Label(self.thirdFrame, text = "", background="white")
        self.locationFileLabel.pack(side = LEFT, padx = 10, pady= 10)

        #The fourth frame from the top
        self.fourthFrame = Frame(self, background="white")
        self.fourthFrame.pack(side = TOP)

        #This create the label and the text box for the file name
        self.fileNameLabel = Label(self.fourthFrame, text = "Enter your file name(add .xyz at the end):", background="white")
        self.fileNameLabel.pack(side = LEFT, padx = 10, pady = 10)
        self.fileNameText = Text(self.fourthFrame, height=1, width=14, background='old lace')
        self.fileNameText.pack(side = LEFT, padx =10, pady =10)

        #The Fifth frame from the top
        self.fifthFrame = Frame(self, background="white")
        self.fifthFrame.pack(side = TOP)

        #Label for the number of process
        self.ProcessLabel = Label(self.fifthFrame, text = "Number of process", background="white")
        self.ProcessLabel.pack(side = LEFT, padx = 10, pady=10)

        #The horizontal sliding bar for the numbers of proccess
        self.numberOfProcessing = Scale(self.fifthFrame, from_=1, to=8,orient=HORIZONTAL)
        self.numberOfProcessing.set(1)
        self.numberOfProcessing.pack()

        #The last frame fome the top
        self.sixthFrame = Frame(self, background="white")
        self.sixthFrame.pack(side = TOP)

        #This create the start button
        self.startButton = Button(self.sixthFrame, text = 'Start', command=startProgramme, background="gray5", foreground = "white")
        self.startButton.pack(side = LEFT, padx = 10, pady=10)

        #This create the stop button
        self.endButton = Button(self.sixthFrame, text = 'Stop', command=merge.stopAll, background="gray5", foreground = "white")
        self.endButton.pack(side = RIGHT, padx = 10, pady=10)

        #The last frame fome the top
        self.bottomFrame = Frame(self, background="white")
        self.bottomFrame.pack(side = BOTTOM)

        #Label for the time
        self.timeLabel = Label(self.bottomFrame, text = "Processing time: ?? seconds", background="white")
        self.timeLabel.pack(side = BOTTOM, padx = 10, pady=10)

    def getFileName(self):
        return self.fileNameText.get("1.0","end-1c")

    def getFileNameNDRE(self):
        return self.fileNameNDRE

    def getFileNameRGB(self):
        return self.fileNameRGB

    def getFilePath(self):
        return self.filePathMerge

    def getFilePathMerge(self):
        return self.filePathMerge

    def getNumberOfProcessing(self):
        return self.numberOfProcessing
    
    #This method is call when the NDRE browse button is click
    def fileDialogNDRE(self):
        self.fileNameNDRE = filedialog.askopenfilename(initialdir = "/", title = "select a file", filetype = (("xyz", "*.xyz"),("All", "*.*")))
        self.NDREfileLabel.configure(text = self.fileNameNDRE)

    #This method is call when the RGB browse button is click
    def fileDialogRGB(self):
        self.fileNameRGB = filedialog.askopenfilename(initialdir = "/", title = "select a file", filetype = (("xyz", "*.xyz"),("All", "*.*")))
        self.RGBfileLabel.configure(text = self.fileNameRGB)

    #This method is call when the folder browse button is click
    def fileDialogLocation(self):
        self.filePathMerge = filedialog.askdirectory()
        self.locationFileLabel.configure(text = self.filePathMerge)

    
# This method start the merge adn is call when clicking the start button
def startProgramme():
    #read what is the name text box
    fileName = root.getFileName()
    #create the two list of points(RGB and NDRE)
    NDREpoints = merge.ListOfPoint(root.getFileNameNDRE())
    print("The list base on the NDRE file was created!")
    RGBpoints = merge.ListOfPoint(root.getFileNameRGB())
    print("The list base on the RGB file was created!")
    myTime = time.time()
    #call the code that merge the file in one
    merge.startProcessing(NDREpoints, RGBpoints, root.getFilePath(), fileName,root.getNumberOfProcessing().get())
    merge.mergeAll(root.getFilePathMerge(),fileName,root.getNumberOfProcessing().get())
    print("It took " + str(time.time() - myTime) + " seconds.")
    self.timeLabel.configure(text = "Processing time: " + str(time.time() - myTime) + " seconds")
    
global root
root = Root()
root.mainloop()
