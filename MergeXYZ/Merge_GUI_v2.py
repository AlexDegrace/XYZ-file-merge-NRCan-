from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import time

## (2019-07-17) This programme is the GUI that go with the programme
#   "PointCloud_RGB_NDRE_merge_vX" where X is the version. This cersion of the
#   GUI is for the version 5 or more.

class Root(Tk):
    
    def __init__(self):
        super(Root,self).__init__()
        self.merge = __import__('PointCloud_RGB_NDRE_merge_v6')
        
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

        #The last frame fome the top
        self.bottomFrame = Frame(self, background="white")
        self.bottomFrame.pack(side = BOTTOM)

        self.timeLabel = Label(self.bottomFrame, text = "Processing time: ?? seconds", background="white")
        self.timeLabel.pack(side = BOTTOM, padx = 10, pady=10)

        #This create the start button
        self.startButton = Button(self.bottomFrame, text = 'Start', command=self.startProgramme, background="gray5", foreground = "white")
        self.startButton.pack(side = BOTTOM, padx = 10, pady=10)
        

    # This method start the merge adn is call when clicking the start button
    def startProgramme(self):
        #read what is the name text box
        fileName = self.fileNameText.get("1.0","end-1c")
        #create the two list of points(RGB and NDRE)
        NDREpoints = self.merge.ListOfPoint(self.fileNameNDRE)
        print("The list base on the NDRE file was created!")
        RGBpoints = self.merge.ListOfPoint(self.fileNameRGB)
        print("The list base on the RGB file was created!")
        myTime = time.time()
        #call the code that merge the file in one
        self.merge.startProcessing(NDREpoints, RGBpoints, self.filePathMerge, fileName)
        self.merge.mergeAll(self.filePathMerge,fileName)
        print("It took " + str(time.time() - myTime) + " seconds.")
        self.timeLabel.configure(text = "Processing time: " + str(time.time() - myTime) + " seconds")

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

    

root = Root()
root.mainloop()
