# GUI application to run pulse EPR Fitting scripts
# This initializes the GUI and should allow one to interface with the program

from Tkinter import Tk, Label, Button

class data_fit_gui:
    def __init__(self, master):
        self.master = master
        master.title("Pulse EPR Fitting")

        self.label = Label(master, text='Filename')
        self.label.pack()

        self.import_button = Button(master, text="Import Data", command=self.import_data)
        self.import_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def import_data(self):
        
