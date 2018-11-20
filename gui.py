import random
from tkinter import *

class Morpho:

	def __init__(self, master):
		self.master = master
		master.title("Morhpological Operations")
		self.message = "Choose A Test"
		self.radiogroup = LabelFrame(master, text="Options")

		imoptions = ["Image 1", "Image 2", "Image 3"]
		imvar = StringVar(master)
		imvar.set(imoptions[0])
		stoptions = ["Square", "Cross"]
		stvar = StringVar(master)
		stvar.set(stoptions[0])
		inphoto = PhotoImage(file="placeholder.png")
		resphoto = PhotoImage(file="placeholder.png")
		blobphoto = PhotoImage(file="placeholder.png")
		difphoto = PhotoImage(file="placeholder.png")
		#Widgets
		
		#Image Seletcion    Dropdown
		#Windows Selection  Dropbown
		#Morpho Operations  Radios
		#Run 				Button
		#Save 				Button
		#Blob 				Button
		#Input 				Image
		#Output 			Image
		#Difference 		Image
		#Blob  				Image
		self.runB = Button(master, text="RUN", command=self.run)
		self.resetB = Button(master, text="RESET", command=self.reset)
		self.blobB = Button(master, text="BLOB COUNT", command=self.blob)

		self.imageS = OptionMenu(master, imvar, imoptions[1], imoptions[2])
		self.structS = OptionMenu(master, stvar, stoptions[1])

		self.inIm = Label(master, image=inphoto)
		self.inIm.photo = inphoto
		self.resIm = Label(master, image=resphoto)
		self.resIm.photo = resphoto
		self.difIm = Label(master, image=difphoto)
		self.difIm.photo = difphoto
		self.blobIm = Label(master, image=blobphoto)
		self.blobIm.photo = blobphoto

		self.r1 = Radiobutton(self.radiogroup, text="Erode")
		self.r2 = Radiobutton(self.radiogroup, text="Dilate")
		self.r3 = Radiobutton(self.radiogroup, text="Open")
		self.r4 = Radiobutton(self.radiogroup, text="Close")
		self.r5 = Radiobutton(self.radiogroup, text="Open-Close")
		self.r6 = Radiobutton(self.radiogroup, text="Close-Open")


		#Layout / Initialization
		self.runB.grid(row=4, column=0)
		self.resetB.grid(row=4,column=1)
		self.blobB.grid(row=5, column=0)
		
		self.imageS.grid(row=0, column=0)
		self.structS.grid(row=1, column=0)
		
		self.inIm.grid(row=2, column=3)
		self.resIm.grid(row=2, column=4)
		self.difIm.grid(row=3, column=3)
		self.blobIm.grid(row=3, column=4)

		self.radiogroup.grid(row=2, column=0)
		self.r1.grid(row=0, column=0)
		self.r2.grid(row=1, column=0)
		self.r3.grid(row=2, column=0)
		self.r4.grid(row=3, column=0)
		self.r5.grid(row=4, column=0)
		self.r6.grid(row=5, column=0)


	def sel(self):
		print("sel command chosen")
	def run(self):
		print("RUN")
	def reset(self):
		print("RESET")
	def blob(self):
		print("BLOB")


root = Tk()
my_gui = Morpho(root)
root.mainloop()