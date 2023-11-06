# Audisio Nicolò
from tkinter import *

def pressione_pulsante(num):
	global text
	text = text + str(num)
	text_label.set(text)

def controllo():
	global text
	try:
		total = str(eval(text))
		text_label.set(total)
		text = total
	except SyntaxError:
		text_label.set("Errore di sintassi")
		text = ""
	except ZeroDivisionError:
		text_label.set("Errore artimetico")
		text = ""

def pulizia():
	global text
	text_label.set("")
	text = ""


root = Tk()
root.title("Audisio - Calcolatrice")
root.geometry("500x500")

text = ""

text_label = StringVar()

label = Label(root, textvariable = text_label, font = ('consolas',20), bg = "white", width = 24, height = 2)
label.pack()

frame = Frame(root)
frame.pack()

button1 = Button(frame, text = 1, height = 4, width = 9, font = 35, command = lambda: pressione_pulsante(1))
button1.grid(row = 0, column = 0)

button2 = Button(frame, text = 2, height = 4, width = 9, font = 35, command = lambda: pressione_pulsante(2))
button2.grid(row = 0, column = 1)

button3 = Button(frame, text = 3, height = 4, width = 9, font = 35, command = lambda: pressione_pulsante(3))
button3.grid(row = 0, column = 2)

button4 = Button(frame, text = 4, height = 4, width = 9, font = 35, command = lambda: pressione_pulsante(4))
button4.grid(row = 1, column = 0)

button5 = Button(frame, text = 5, height = 4, width = 9, font = 35, command = lambda: pressione_pulsante(5))
button5.grid(row = 1, column = 1)

button6 = Button(frame, text = 6, height = 4, width = 9, font = 35, command = lambda: pressione_pulsante(6))
button6.grid(row = 1, column = 2)

button7 = Button(frame, text = 7, height = 4, width = 9, font = 35, command = lambda: pressione_pulsante(7))
button7.grid(row = 2, column = 0)

button8 = Button(frame, text = 8, height = 4, width = 9, font = 35, command = lambda: pressione_pulsante(8))
button8.grid(row = 2, column = 1)

button9 = Button(frame, text = 9, height = 4, width = 9, font = 35, command = lambda: pressione_pulsante(9))
button9.grid(row = 2, column = 2)

button0 = Button(frame, text = 0, height = 4, width = 9, font = 35, command = lambda: pressione_pulsante(0))
button0.grid(row = 3, column = 0)

addizione = Button(frame, text = '+', height = 4, width = 9, font = 35, command = lambda: pressione_pulsante('+'))
addizione.grid(row = 0, column = 3)

sottrazione = Button(frame, text = '-', height = 4, width = 9, font = 35, command = lambda: pressione_pulsante('-'))
sottrazione.grid(row = 1, column = 3)

moltiplicazione = Button(frame, text = '*', height = 4, width = 9, font = 35, command = lambda: pressione_pulsante('*'))
moltiplicazione.grid(row = 2, column = 3)

divisione = Button(frame, text = '/', height = 4, width = 9, font = 35, command = lambda: pressione_pulsante('/'))
divisione.grid(row = 3, column = 3)

uguale = Button(frame, text = '=', height = 4, width = 9, font = 35, command = controllo)
uguale.grid(row = 3, column = 2)

decimale = Button(frame, text = '.', height = 4, width = 9, font = 35, command = lambda: pressione_pulsante('.'))
decimale.grid(row = 3, column = 1)

pulizia = Button(root, text = 'pulizia', height = 4, width = 12, font = 35, command = pulizia)

pulizia.pack()
root.mainloop()
