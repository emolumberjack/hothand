from tkinter import *
import pandas as pd
import nba_py.player
import nba_py.shotchart
import csv 
import csv_reader 
import checker
import hotHand

class AppWindow:

	def __init__(self, master):

		# Label widget for title
		self.entryBarLabel = Label(master, text="NBA Player Id")
		self.entryBarLabel.grid(row=0, columnspan=6)

		# Entry widget for Player ID
		self.entryBar = Entry(master)
		self.entryBar.grid(row=1, columnspan=6)

		# Button widget to run Hothand
		self.execute = Button(master, text="Execute", command = self.run)
		self.execute.grid(row=2, column=2)

		# Button widget to exit
		self.close = Button(master, text="Close", command=master.quit)
		self.close.grid(row=2, column=3)

		# Text widget for output
		self.textBox = Text(master)
		self.textBox.configure(background="light grey", font="Helvetica", bd="6")
		self.textBox.grid(sticky=S, columnspan=6)


	def run(self):

		#Creates the string textOutput
		textOutput = hothand.main(self.entryBar.get())	

		#Clears textBox widget, then sent textOutput to it
		self.textBox.delete(1.0, END)
		self.textBox.insert(END, textOutput)


root = Tk()
app = AppWindow(root)

root.mainloop()
root.destroy()