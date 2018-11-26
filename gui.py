import random
from tkinter import *
import cv2
import numpy as np
from opencv_f import eroder

class Morpho:

	def __init__(self, master):
		#create main containers
		self.master = master
		master.title("Morhpological Operations")
		self.message = "Choose A Test"
		self.lframe = Frame(master, height=600, padx=5, pady=5)
		self.imgroup = Frame(master, width=600, height=600, padx=5, pady=5)
		#layout main containers
		self.master.grid_columnconfigure(0, weight=1)
		self.master.grid_columnconfigure(1, weight=2)
		self.master.grid_rowconfigure(0, weight=1)

		self.lframe.grid(row=0, column=0, sticky=N+S+E+W)
		self.imgroup.grid(row=0, column=1, sticky=N+S+E+W)
		self.lframe.grid_rowconfigure(0, weight=1)
		self.lframe.grid_rowconfigure(1, weight=2)
		self.lframe.grid_rowconfigure(2, weight=1)
		self.lframe.grid_columnconfigure(0, weight=1)

		#create left containers
		self.selgroup = Frame(self.lframe)
		self.radiogroup = LabelFrame(self.lframe, text="Options")
		self.bgroup = Frame(self.lframe)
		
		#layout left containers
		self.selgroup.grid_columnconfigure(0, weight=1)
		self.selgroup.grid_columnconfigure(1, weight=1)

		self.radiogroup.grid_rowconfigure(0, weight=1)
		self.radiogroup.grid_rowconfigure(1, weight=1)
		self.radiogroup.grid_rowconfigure(2, weight=1)
		self.radiogroup.grid_rowconfigure(3, weight=1)
		self.radiogroup.grid_rowconfigure(4, weight=1)
		self.radiogroup.grid_rowconfigure(5, weight=1)

		self.bgroup.grid_columnconfigure(0, weight=1)
		self.bgroup.grid_columnconfigure(1, weight=1)
		self.bgroup.grid_rowconfigure(0, weight=1, pad=10)
		self.bgroup.grid_rowconfigure(1, weight=1)
		self.bgroup.grid_rowconfigure(2, weight=1, pad=10)

		self.selgroup.grid(row=0, column=0, sticky=E+W)
		self.radiogroup.grid(row=1, column=0, sticky=E+W+N+S)
		self.bgroup.grid(row=2, column=0, sticky=E+W)

		#Variables
		self.imoptions = ["binary_1", "binary_2", "binary_3", "binary_4"]
		self.imvar = StringVar(master)
		self.imvar.set("Select Image")
		self.stoptions = ["Square", "Cross"]
		self.stvar = StringVar(master)
		self.stvar.set("Select Window")
		self.inphoto = PhotoImage(file="placeholder.png")
		self.resphoto = PhotoImage(file="placeholder.png")
		self.blobphoto = PhotoImage(file="placeholder.png")
		self.difphoto = PhotoImage(file="placeholder.png")
		self.opVar = IntVar()
		self.opVar.set(99)
		self.count = 0

		#Widgets
		self.imageS = OptionMenu(self.selgroup, self.imvar, self.imoptions[0], self.imoptions[1], self.imoptions[2], self.imoptions[3], command=self.sel)
		self.structS = OptionMenu(self.selgroup, self.stvar, self.stoptions[0], self.stoptions[1])

		self.inIm = Label(self.imgroup, image=self.inphoto)
		self.inIm.photo = self.inphoto
		self.resIm = Label(self.imgroup, image=self.resphoto)
		self.resIm.photo = self.resphoto
		self.difIm = Label(self.imgroup, image=self.difphoto)
		self.difIm.photo = self.difphoto
		self.blobIm = Label(self.imgroup, image=self.blobphoto)
		self.blobIm.photo = self.blobphoto

		self.r1 = Radiobutton(self.radiogroup, text="Erode", variable=self.opVar, value=0 )
		self.r2 = Radiobutton(self.radiogroup, text="Dilate", variable=self.opVar, value=1 )
		self.r3 = Radiobutton(self.radiogroup, text="Open", variable=self.opVar, value=2 )
		self.r4 = Radiobutton(self.radiogroup, text="Close", variable=self.opVar, value=3 )
		self.r5 = Radiobutton(self.radiogroup, text="Open-Close", variable=self.opVar, value=4)
		self.r6 = Radiobutton(self.radiogroup, text="Close-Open", variable=self.opVar, value=5)

		self.runB = Button(self.bgroup, text="RUN", command=self.run)
		self.resetB = Button(self.bgroup, text="RESET", command=self.reset)
		self.blobB = Button(self.bgroup, text="BLOB COUNT", command=self.blob)

		#Layout / Initialization
		self.imageS.grid(row=0, column=0, padx=5, pady=10)
		self.structS.grid(row=0, column=1, padx=5, pady=10)
		
		self.r1.grid(row=0, column=0, sticky=W)
		self.r2.grid(row=1, column=0, sticky=W)
		self.r3.grid(row=2, column=0, sticky=W)
		self.r4.grid(row=3, column=0, sticky=W)
		self.r5.grid(row=4, column=0, sticky=W)
		self.r6.grid(row=5, column=0, sticky=W)

		self.runB.grid(row=0, column=0, columnspan=2, sticky=E+W, padx=20)
		self.blobB.grid(row=1, column=0, columnspan=2, sticky=E+W, padx=20)
		self.resetB.grid(row=2,column=0, columnspan=2, sticky=E+W, padx=20)

		self.inIm.grid(row=0, column=0, padx=2, pady=2)
		self.resIm.grid(row=0, column=1, padx=2, pady=2)
		self.difIm.grid(row=1, column=0, padx=2, pady=2)
		self.blobIm.grid(row=1, column=1, padx=2, pady=2)

	#Functions
	def sel(self, var):
			print("Selecting ", var)
			self.inphoto.configure(file=str(var)+".png")
			self.resphoto.configure(file=str(var)+".png")


	def run(self):
		self.count += 1
		var = self.opVar.get()
		if (var == 0):
				if (self.count == 1):
					print("RUNNING Erode on image: ", self.imvar.get())
					img=cv2.imread("binary_1.png", 0)
					newImg=(eroder(img))
					cv2.imwrite("binary_1_result.png", newImg)
					self.resphoto.configure(file="binary_1_result.png")
				elif(self.count != 1):
					print("RUNNING Erode on image: ", self.imvar.get())
					img=cv2.imread("binary_1_result.png", 0)
					newImg=(eroder(img))
					cv2.imwrite("binary_1_result.png", newImg)
					self.resphoto.configure(file="binary_1_result.png")

		elif(var == 1):
			print("RUNNING Dilate ", var)
		elif(var == 2):
			print("RUNNING Open ", var)
		elif(var == 3):
			print("RUNNING Close ", var)
		elif(var == 4):
			print("RUNNING Open-Close", var)
		elif(var == 5):
			print("RUNNING Close-Open ", var)
		else:
			print("CHOOSE AN OPERATION")

	def reset(self):
		print("RESET")
		self.opVar.set(99)
		self.inphoto.configure(file="placeholder.png")
		self.resphoto.configure(file="placeholder.png")
		self.imvar.set("Select Image")
		self.stvar.set("Select Window")
		self.count = 0

	def blob(self):
		print("BLOB")

#WINDOW LOOP
root = Tk()
my_gui = Morpho(root)
root.mainloop()