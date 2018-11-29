import random
from tkinter import *
import cv2
import numpy as np
from opencv_f import eroder, dilater, opener, closer, ocer, coer, boundary, blobber, different
from skeletonfunction import skeletonizer

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
		self.selgroup.grid_columnconfigure(2, weight=1)
		self.selgroup.grid_rowconfigure(0, weight=1)
		self.selgroup.grid_rowconfigure(1, weight=1)

		self.radiogroup.grid_rowconfigure(0, weight=1)
		self.radiogroup.grid_rowconfigure(1, weight=1)
		self.radiogroup.grid_rowconfigure(2, weight=1)
		self.radiogroup.grid_rowconfigure(3, weight=1)
		self.radiogroup.grid_rowconfigure(4, weight=1)
		self.radiogroup.grid_rowconfigure(5, weight=1)
		self.radiogroup.grid_rowconfigure(6, weight=1)
		self.radiogroup.grid_rowconfigure(7, weight=1)

		self.bgroup.grid_columnconfigure(0, weight=1)
		self.bgroup.grid_columnconfigure(1, weight=1)
		self.bgroup.grid_rowconfigure(0, weight=1, pad=10)
		self.bgroup.grid_rowconfigure(1, weight=1)
		self.bgroup.grid_rowconfigure(2, weight=1, pad=10)

		self.selgroup.grid(row=0, column=0, sticky=E+W)
		self.radiogroup.grid(row=1, column=0, sticky=E+W+N+S)
		self.bgroup.grid(row=2, column=0, sticky=E+W)

		#Variables
		self.imoptions = ["binary_1", "binary_2", "binary_3", "binary_4", "grayscale_1", "grayscale_2"]
		self.imvar = StringVar(master)
		self.imvar.set("Select Image")
		self.stoptions = ["Square", "Cross"]
		self.windSize = ["3-cross","5-cross"]
		self.windVar = StringVar(master)
		self.windVar.set("Cross Size")
		self.stvar = StringVar(master)
		self.stvar.set("S.E.")
		self.stvar2 = StringVar(master)
		self.stvar2.set("S.E. Size")
		self.inphoto = PhotoImage(file="placeholder.png")
		self.resphoto = PhotoImage(file="placeholder.png")
		self.blobphoto = PhotoImage(file="placeholder.png")
		self.difphoto = PhotoImage(file="placeholder.png")
		self.opVar = IntVar()
		self.opVar.set(99)
		self.count = 0

		#Widgets
		self.imageS = OptionMenu(self.selgroup, self.imvar, self.imoptions[0], self.imoptions[1], self.imoptions[2], self.imoptions[3], self.imoptions[4], self.imoptions[5], command=self.sel)
		self.structS = OptionMenu(self.selgroup, self.stvar, self.stoptions[0], self.stoptions[1], command=self.windSet)
		self.structS2= Entry(self.selgroup, text=self.stvar2, width=10)
		self.crossSel = OptionMenu(self.selgroup, self.windVar, self.windSize[0], self.windSize[1])

		self.inF = LabelFrame(self.imgroup, text="INPUT")
		self.resF = LabelFrame(self.imgroup, text="RESULT")
		self.difF = LabelFrame(self.imgroup, text="DIFFERENCE")
		self.blobF = LabelFrame(self.imgroup, text="BLOB")

		self.inIm = Label(self.inF, image=self.inphoto)
		self.inIm.photo = self.inphoto
		self.resIm = Label(self.resF, image=self.resphoto)
		self.resIm.photo = self.resphoto
		self.difIm = Label(self.difF, image=self.difphoto)
		self.difIm.photo = self.difphoto
		self.blobIm = Label(self.blobF, image=self.blobphoto)
		self.blobIm.photo = self.blobphoto

		self.r1 = Radiobutton(self.radiogroup, text="Erode", variable=self.opVar, value=0 )
		self.r2 = Radiobutton(self.radiogroup, text="Dilate", variable=self.opVar, value=1 )
		self.r3 = Radiobutton(self.radiogroup, text="Open", variable=self.opVar, value=2 )
		self.r4 = Radiobutton(self.radiogroup, text="Close", variable=self.opVar, value=3 )
		self.r5 = Radiobutton(self.radiogroup, text="Open-Close", variable=self.opVar, value=4)
		self.r6 = Radiobutton(self.radiogroup, text="Close-Open", variable=self.opVar, value=5)
		self.r7 = Radiobutton(self.radiogroup, text="Skeletonize", variable=self.opVar, value=6)
		self.r8 = Radiobutton(self.radiogroup, text="Boundary Extraction", variable=self.opVar, value=7)

		self.runB = Button(self.bgroup, text="RUN", command=self.run)
		self.resetB = Button(self.bgroup, text="RESET", command=self.reset)
		self.blobB = Button(self.bgroup, text="BLOB COUNT", command=self.blob)

		#Layout / Initialization
		self.imageS.grid(row=0, column=0, padx=5, pady=10)
		self.structS.grid(row=0, column=1, padx=5, pady=10)
		self.structS2.grid(row=0, column=2, padx=5,pady=10)
		self.crossSel.grid(row=0, column=2, padx=5,pady=5)
		self.crossSel.grid_remove()
		
		self.r1.grid(row=0, column=0, sticky=W)
		self.r2.grid(row=1, column=0, sticky=W)
		self.r3.grid(row=2, column=0, sticky=W)
		self.r4.grid(row=3, column=0, sticky=W)
		self.r5.grid(row=4, column=0, sticky=W)
		self.r6.grid(row=5, column=0, sticky=W)
		self.r7.grid(row=6, column=0, sticky=W)
		self.r8.grid(row=7, column=0, sticky=W)

		self.runB.grid(row=0, column=0, columnspan=2, sticky=E+W, padx=20)
		self.blobB.grid(row=1, column=0, columnspan=2, sticky=E+W, padx=20)
		self.resetB.grid(row=2,column=0, columnspan=2, sticky=E+W, padx=20)

		self.inF.grid(row=0, column=0, padx=2, pady=2)
		self.resF.grid(row=0, column=1, padx=2, pady=2)
		self.difF.grid(row=1, column=0, padx=2, pady=2)
		self.blobF.grid(row=1, column=1, padx=2, pady=2)

		self.inIm.grid(row=0, column=0, padx=2, pady=2)
		self.resIm.grid(row=0, column=0, padx=2, pady=2)
		self.difIm.grid(row=0, column=0, padx=2, pady=2)
		self.blobIm.grid(row=0, column=0, padx=2, pady=2)

	#Functions
	def sel(self, var):
			print("Selecting ", var)
			self.inphoto.configure(file=str(var)+".png")
			self.resphoto.configure(file=str(var)+".png")

	def windSet(self, var):
		if(self.stvar.get() == "Square"):
			print("window set to square")
			self.structS2.grid()
			self.crossSel.grid_remove()

		elif(self.stvar.get() == "Cross"):
			print("window set to cross")
			self.stvar2.set("S.E. Size")
			self.structS2.grid_remove()
			self.crossSel.grid()

	def run(self):
		var = self.opVar.get()

		if(self.imvar.get() == "Select Image"):
			print("Select An Image")
			return(99)
		if (var not in [6, 7]):
			if(self.stvar2.get() == "S.E. Size"):
				if(self.stvar.get() == "Square"):
					print("Set Window")
					return(99)
				if(self.windVar.get() == "Cross Size"):
					print("Set Window")
					return(99)
			window= self.stvar.get()
			if(window == "Square"):
				size= int(self.stvar2.get())
			elif(window == "Cross"):
				size= (self.windVar.get())

		self.count += 1

		if (var == 0):
				if (self.count == 1):
					print("RUNNING Erode on image: ", self.imvar.get())
					print("Window: ", window,"Size: ", size, "x", size)
					img=cv2.imread(self.imvar.get()+".png", 0)
					newImg=(eroder(img,window,size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")
				elif(self.count != 1):
					print("RUNNING Erode on image: ", self.imvar.get())
					print("Window: ", window,"Size: ", size, "x", size)
					img=cv2.imread(self.imvar.get()+"_result.png", 0)
					newImg=(eroder(img,window,size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")

				#compute diff


		elif(var == 1):
				if (self.count == 1):
					print("RUNNING Dilate on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+".png", 0)
					newImg=(dilater(img, window, size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")
				elif(self.count != 1):
					print("RUNNING Dilate on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+"_result.png", 0)
					newImg=(dilater(img, window, size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")

		elif(var == 2):
				if (self.count == 1):
					print("RUNNING Open on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+".png", 0)
					newImg=(opener(img,window,size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")
				elif(self.count != 1):
					print("RUNNING Open on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+"_result.png", 0)
					newImg=(opener(img,window,size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")


		elif(var == 3):
				if (self.count == 1):
					print("RUNNING Close on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+".png", 0)
					newImg=(closer(img,window,size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")
				elif(self.count != 1):
					print("RUNNING Close on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+"_result.png", 0)
					newImg=(closer(img,window,size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")


		elif(var == 4):
				if (self.count == 1):
					print("RUNNING Open-Close on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+".png", 0)
					newImg=(ocer(img,size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")
				elif(self.count != 1):
					print("RUNNING Open-Close on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+"_result.png", 0)
					newImg=(ocer(img,size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")

		elif(var == 5):
				if (self.count == 1):
					print("RUNNING Close-Open on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+".png", 0)
					newImg=(coer(img,size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")
				elif(self.count != 1):
					print("RUNNING Close-Open on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+"_result.png", 0)
					newImg=(coer(img,size))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")

		elif(var == 6):
				if (self.count == 1):
					print("RUNNING Skeletonization on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+".png", 0)
					newImg=(skeletonizer(img))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")
				elif(self.count != 1):
					print("RUNNING Skeletonization on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+"_result.png", 0)
					newImg=(skeletonizer(img))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")

		elif(var == 7):
				if (self.count == 1):
					print("RUNNING Boundary Extraction on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+".png", 0)
					newImg=(boundary(img))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")
				elif(self.count != 1):
					print("RUNNING Boundary Extraction on image: ", self.imvar.get())
					img=cv2.imread(self.imvar.get()+"_result.png", 0)
					newImg=(boundary(img))
					cv2.imwrite(self.imvar.get()+"_result.png", newImg)
					self.resphoto.configure(file=self.imvar.get()+"_result.png")

		else:
			print("CHOOSE AN OPERATION")

		img=cv2.imread(self.imvar.get()+".png",0)
		newImg=cv2.imread(self.imvar.get()+"_result.png",0)
		diff = (different(img,newImg))
		cv2.imwrite(self.imvar.get()+"_diff.png", diff)
		self.difphoto.configure(file=self.imvar.get()+"_diff.png")

	def reset(self):
		print("RESET")
		self.opVar.set(99)
		self.inphoto.configure(file="placeholder.png")
		self.resphoto.configure(file="placeholder.png")
		self.blobphoto.configure(file="placeholder.png")
		self.difphoto.configure(file="placeholder.png")
		self.imvar.set("Select Image")
		self.stvar.set("S.E.")
		self.stvar2.set("S.E. Size")
		self.count = 0
		self.windVar.set("Cross Size")


	def blob(self):
		if(self.imvar.get() == "Select Image"):
			print("Select An Image")
			return(99)
		if (self.count < 1):
			print("Blob Count")
			print("RUNNING BLOB on image: ", self.imvar.get(), "_result")
			img=cv2.imread(self.imvar.get()+".png", 0)
			newImg=(blobber(img))
			cv2.imwrite(self.imvar.get()+"_blobresult.png", newImg)
			self.blobphoto.configure(file=self.imvar.get()+"_blobresult.png")
		if (self.count >= 1):
			print("Blob Count")
			print("RUNNING BLOB on image: ", self.imvar.get(), "_result")
			img=cv2.imread(self.imvar.get()+"_result.png", 0)
			newImg=(blobber(img))
			cv2.imwrite(self.imvar.get()+"_blobresult.png", newImg)
			self.blobphoto.configure(file=self.imvar.get()+"_blobresult.png")

#WINDOW LOOP
root = Tk()
my_gui = Morpho(root)
root.mainloop()