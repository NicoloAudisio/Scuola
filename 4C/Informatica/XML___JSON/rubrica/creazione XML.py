import xml.etree.ElementTree as ET
from xml.dom import minidom

def catfile(nomefile="esempio1.xml"):
	with open(nomefile, 'r') as _file:
		for _line in iter((_file.readline),""):
			print(_line, end="")
	print()

def indenta(nomef_in="esempio1.xml", nomef_out="esempio1-ok.xml"):
	dom = minidom.parse(nomef_in)
	with open(nomef_out, 'w', encoding='UTF-8') as fh:
		 dom.writexml(fh, indent='', addindent='   ', newl='\n', encoding='UTF-8')

data = ET.Element('main')

# nome 1
nome = ET.SubElement(data, 'Persona1')
nome.set('nome', 'Simone')
eta = ET.SubElement(nome, 'eta')
eta.text = "18"
sport = ET.SubElement(nome, 'sport')
sport.set('disciplina', 'ciclismo')

print("\n--- NO INDENTAZIONE ---\n")
tree = ET.ElementTree(data)
tree.write('esempio1.xml')
catfile('esempio1.xml')

print("\n--- INDENTAZIONE ---\n")
indenta('esempio1.xml','esempio1-ok.xml')
catfile('esempio1-ok.xml')