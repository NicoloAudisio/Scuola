import tkinter

class Finestra(tkinter.Tk):
	#costruttore
	def __init__(self,nome):
		super().__init__()
		self.title("Finestra grafica "+nome)
		self.geometry("300x200")
		self.resizable(0,0)
		self.crea_widgets()
		
	def crea_widgets(self):
		mf=tkinter.Frame(self)
		mf.grid()
		lbl1=tkinter.Label(mf,text="Premi il pulsante -->")
		lbl1.grid(row=0,column=0)
		btn1=tkinter.Button(mf, text="premi quì")
		btn1.grid(row=0,column=1)
		
def main():
	f=Finestra("Main")
	f.mainloop()
	
main()

