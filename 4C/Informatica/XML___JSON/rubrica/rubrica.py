import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

def catfile(nomefile="rubrica.xml"):
	with open(nomefile, 'r', encoding='UTF-8') as _file: # aggiunto l'encoding
		for _line in iter(_file.readline,""):
			print(_line, end="")

def indenta(nomef_in="rubrica.xml", nomef_out="rubrica-ok.xml"):
	dom = minidom.parse(nomef_in)
	with open(nomef_out, 'w', encoding='UTF-8') as fh: # aggiunto l'encoding
		dom.writexml(fh, indent='', addindent=' ', newl='\n', encoding='UTF-8')

def crea_xml():
	rubrica = ET.Element("rubrica")
	while True:
		utente = ET.SubElement(rubrica, "utente")
		os.system("clear")
		print("\n--- AGGIUNGI CONTATTO ---\n")
		cognome = input("Inserisci il cognome dell'utente (0 per uscire): ")
		if cognome == "0":
			break
		ET.SubElement(utente, "cognome").text = cognome
		
		nome = input("Inserisci il nome dell'utente: ")
		ET.SubElement(utente, "nome").text = nome
		
		sesso = input("Inserisci il sesso dell'utente (m/f): ")
		ET.SubElement(utente, "sesso").text = sesso
		
		titolo = input("Inserisci il titolo dell'utente (amico, prof., dott., altro): ")
		ET.SubElement(utente, "titolo").text = titolo
		
		soprannome = input("Inserisci il soprannome dell'utente: ")
		ET.SubElement(utente, "soprannome").text = soprannome
		
		indirizzo = ET.SubElement(utente, "indirizzo")
		via = input("Inserisci la via dell'utente: ")
		ET.SubElement(indirizzo, "via", numero="").text = via
		
		numero = input("Inserisci il numero civico dell'utente: ")
		ET.SubElement(indirizzo.find("via"), "numero").text = numero
		
		cap = input("Inserisci il CAP dell'utente: ")
		ET.SubElement(indirizzo, "cap").text = cap
		
		telefono = input("Inserisci il numero di telefono dell'utente: ")
		tipo = input("E' un numero di telefono fisso o cellulare? ")
		ET.SubElement(utente, "telefono", tipo=tipo).text = telefono

		tree = ET.ElementTree(rubrica)
		tree.write('rubrica.xml', encoding='UTF-8')
		catfile('rubrica.xml')

		indenta('rubrica.xml','rubrica-ok.xml')
		catfile('rubrica-ok.xml')
		print("Rubrica salvata correttamente!")

def cerca_cognome():
	os.system("clear")
	tree = ET.parse("rubrica.xml")
	root = tree.getroot()
	print("\n--- CERCA PER COGNOME ---\n")
	cognome = input("Inserisci il cognome da cercare: ")

	for utente in root.findall("utente"):
		if utente.find("cognome").text == cognome:
			print("\nUtente trovato:")
			print(utente.find("cognome").text, utente.find("nome").text)
			continuo = input("")
			os.system("clear")

def cerca_uomini():
	os.system("clear")
	print("\n--- CERCA UOMINI ---\n")
	tree = ET.parse("rubrica.xml")
	root = tree.getroot()
	for utente in root.findall("utente"):
		if utente.find("sesso").text == "m":
			print(utente.find("cognome").text, utente.find("nome").text)
			continuo = input("")
			os.system("clear")

	print("Ricerca completa.")

def cerca_telefono():
	tree = ET.parse("rubrica.xml")
	root = tree.getroot()
	os.system("clear")
	print("\n--- CERCA PER NUMERO DI TELEFONO ---")
	telefono = input("Inserisci il numero di telefono da cercare: ")

	for utente in root.findall("utente"):
		if utente.find("telefono").text == telefono:
			print("\nUtente trovato!")
			print(utente.find("cognome").text, utente.find("nome").text)
			continuo = input("")
			os.system("clear")
			return

def cancella_utente():
	tree = ET.parse("rubrica.xml")
	root = tree.getroot()
	os.system("clear")
	print("\n--- CANCELLA UTENTE ---\n")
	cognome = input("Inserisci il cognome dell'utente da cancellare: ")
	nome = input("Inserisci il nome dell'utente da cancellare: ")

	for utente in root.findall("utente"):
		if utente.find("cognome").text == cognome and utente.find("nome").text == nome:
			root.remove(utente)
			print("\nUtente cancellato.")
			continuo = input("")
			os.system("clear")
			break
		
	with open("rubrica.xml", "wb") as f:
		f.write(ET.tostring(root))
	catfile('rubrica.xml')
	indenta('rubrica.xml','rubrica-ok.xml')
	catfile('rubrica-ok.xml')

def main():
	while True:
		os.system("clear")
		print("\n--- RUBRICA TELEFONICA ---\n")
		print("1. Crea nuova rubrica")
		print("2. Cerca utente per telefono")
		print("3. Cerca utente per cognome")
		print("4. Cerca tutti gli uomini")
		print("5. Cancella utente")
		print("0. Exit")
		scelta = input("\n")
		
		if scelta == "1":
			crea_xml()
		elif scelta == "2":
			cerca_telefono()
		elif scelta == "3":
			cerca_cognome()
		elif scelta == "4":
			cerca_uomini()
		elif scelta == "5":
			cancella_utente()
		elif scelta == "0":
			os.system("clear")
			print("Premere invio per uscire...")
			continua = input("")
			os.system("clear")
			break
			
		else:
			print("Scelta non valida.")

main()