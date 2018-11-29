import random
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E, PhotoImage, Radiobutton,IntVar

class Morpho:

	def __init__(self, master):
		self.master = master
		master.title("Morhpological Operations")
		photo = PhotoImage(file="")
		self.message = "Choose A Test"
		self.label_text = StringVar()
		self.label_text.set(self.message)
		self.label = Label(master, textvariable=self.label_text)
		#vcmd = master.register(self.validate) # we have to wrap the command
		#self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
		self.RFCall = Button(master, text="(NOTHING)", command=self.guess_number)
		self.reset_button = Button(master, text="RESET", command=self.reset, fg="red")
		self.quit = Button(master, text="QUIT", command=self.master.destroy, bg="red")
		self.img = Label(master, image = photo )
		self.img.image = photo
		self.var = IntVar()
		self.choice = Radiobutton(master, text="Image 1", variable=self.var, value=1, command=self.sel)
		self.choice1 = Radiobutton(master, text="Image 2", variable=self.var, value=2, command=self.sel)
		self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
		#self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
		self.RFCall.grid(row=2, column=0)
		self.reset_button.grid(row=2, column=1)
		self.choice.grid(row=3,column=0)
		self.choice1.grid(row=3,column=1)
		self.quit.grid(row=4, column=0, columnspan=2, sticky=W+E, pady=5)
		self.img.grid(row=5, columnspan=2)

	def sel(self):
		print("selecting photo", str(self.var.get()) )
		if(self.var.get() == 1):
			photo = PhotoImage(file="QR.png")
			self.img.configure(image=photo)
			self.img.image = photo
		elif(self.var.get() == 2):
			photo = PhotoImage(file="img.gif")
			self.img.configure(image=photo)
			self.img.image = photo

	def validate(self, new_text):
		print("validating", new_text)
		if not new_text:
			self.guess = None
			return True
		try:
			guess = int(new_text)
			if 1 <= guess <= 100:
				self.guess = guess
				return True
			else:
				self.message = "INVALID NUMBER"
				self.label_text.set(self.message)
				return False
		except ValueError:
			self.message = "INVALID CHARACTER"
			self.label_text.set(self.message)
		return False

	def guess_number(self):
		print("guessing")
		self.label_text.set(self.message)
		
	def reset(self):
		#self.entry.delete(0, END)
		photo = PhotoImage(file="")
		self.img.configure(image=photo)
		self.img.image = photo
		self.message = "TRY AGAIN"
		self.label_text.set(self.message)
		#self.RFCall.configure(state=NORMAL)
root = Tk()
my_gui = Morpho(root)
root.mainloop()