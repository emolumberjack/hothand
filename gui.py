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

		frame = Frame(master)
		frame.pack()

		# Create a label for the text entry field
		self.entryBarLabel = Label(master, text="NBA Player Id")
		self.entryBarLabel.pack()

		# Create an entry field for PlayerID
		self.entryBar = Entry(master)
		self.entryBar.pack()

		# Add a button to execute hotHand.main()
		self.execute = Button(frame, text="Execute", command = self.run)
		self.execute.pack(side=LEFT)

		# Add a button to close the window
		self.close = Button(frame, text="Close", command=frame.quit)
		self.close.pack(side=LEFT)

		# Add a Message widget to display output
		self.msg = Message(master)
		self.msg.pack()


	def run(self):
	#Passes hotHand.main() the text stored in the entry field	
		hotHand.main( self.entryBar.get() )

root = Tk()

app = AppWindow(root)

root.mainloop()
root.destroy()