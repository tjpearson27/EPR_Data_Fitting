import numpy as np 
import scipy

def select_file(filename_var):
	def f():
		newfilename = tkFileDialog.askopenfilename(initialfile=filename_var.get(), multiple=False)
	
		if (str(newfilename)) != "" and ( len(newfilename)>0):
	        	filename_var.set(newfilename)
		
	return f