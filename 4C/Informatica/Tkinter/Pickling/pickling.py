import os
import pickle

file_attributes = open("test.txt", "wb")
print("Nome del file: ", file_attributes.name)
print("File chiuso o no: ", file_attributes.closed)
print("ModalitÃ  apertura: ", file_attributes.mode)
file_attributes.close()


# scrivi un file in binario
file_write_bytes = open("test.txt", "wb")
file_write_bytes.write(bytes("Python Ã¨ un linguaggio spettacolare!", 'UTF-8'))
file_write_bytes.close()

# leggi da un file binario
file_readb = open("test.txt", "rb+")
textb = file_readb.read()
print("La stringa binaria letta Ã¨: ", textb)
file_readb.close()

# scrivi un file in puro ascii
file_write = open("test.txt", "w")
file_write.write("Python Ã¨ un linguaggio spettacolare!")
file_write.close()

# leggi da un file ascii
file_read = open("test.txt", "r+")
text = file_read.read()
print("La stringa letta Ã¨: ", text)
file_read.close()

# Append to a file
file_append = open("test.txt", "a")
file_append .write("\nPython Ã¨ un linguaggio potentissimo.")
file_append.close()

# leggi da un file ascii
file_read = open("test.txt", "r+")
text = file_read.read()
print("La stringa letta Ã¨: ", text)
file_read.close()


# Delete a file
#os.remove("test.txt)

#############################################################

mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
   pickle.dump(mylist, fh)
#fh.close()

# scrive in una stringa l'oggetto serializzato
varpick = pickle.dumps(mylist)
print(varpick)


# legge l'oggetto serializzato da una stringa e lo ricostruisce
mylist_rit = pickle.loads(varpick)
print('Lista recuperata:',mylist_rit)
print('Lista originale: ',mylist)


pickle_off = open ("datafile.txt", "rb")
emp = pickle.load(pickle_off)
print('Lista letta da file:',emp)
pickle_off.close()

EmpID = {1:"Zack",2:"53050",3:"IT",4:"38",5:"Flipkart"}
print("Diz originale:",EmpID)
pickling_on = open("EmpID.pickle","wb")
pickle.dump(EmpID, pickling_on)
pickling_on.close()

pickle_diz = open ("EmpID.pickle", "rb")
diz = pickle.load(pickle_diz)
print("Diz letto da file:",diz)
pickle_diz.close()
