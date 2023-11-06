import xml.etree.ElementTree as ET
from xml.dom import minidom


def catfile(nomefile="pytoxml.xml"):
	with open(nomefile, 'r') as _file:
		for _line in iter((_file.readline),""):
			print(_line, end="")
	print()

def indenta(nomef_in="pytoxml.xml", nomef_out="pytoxml-ok.xml"):
	dom = minidom.parse(nomef_in)
	with open(nomef_out, 'w', encoding='UTF-8') as fh:
		 dom.writexml(fh, indent='', addindent='   ', newl='\n', encoding='UTF-8')


sep = "------------------"
data = ET.Element('mappa')

# prima città
country = ET.SubElement(data, 'citta')
country.set('nome', 'Liechtenstein')
rank = ET.SubElement(country, 'punteggio')
rank.text = "1"
year = ET.SubElement(country, 'anno')
year.text = "2008"
gdppc = ET.SubElement(country, 'gdppc')
gdppc.text = "141100"
neighbor = ET.SubElement(country, 'vicino')
neighbor.set('nome', 'Austria')
neighbor.set('direzione', 'E')
neighbor1 = ET.SubElement(country, 'vicino')
neighbor1.set('nome', 'Svizzera')
neighbor1.set('direzione', 'W')

#seconda città
country = ET.SubElement(data, 'citta')
country.set('nome', 'Singapore')
rank = ET.SubElement(country, 'punteggio')
rank.text = "4"
year = ET.SubElement(country, 'anno')
year.text = "2011"
gdppc = ET.SubElement(country, 'gdppc')
gdppc.text = "59900"
neighbor = ET.SubElement(country, 'vicino')
neighbor.set('nome', 'Malaysia')
neighbor.set('direzione', 'N')

# terza città
country = ET.SubElement(data, 'citta')
country.set('nome', 'Panama')
rank = ET.SubElement(country, 'punteggio')
rank.text = "68"
year = ET.SubElement(country, 'anno')
year.text = "2011"
gdppc = ET.SubElement(country, 'gdppc')
gdppc.text = "13600"
neighbor = ET.SubElement(country, 'vicino')
neighbor.set('nome', 'Costa Rica')
neighbor.set('direzione', 'W')
neighbor1 = ET.SubElement(country, 'vicino')
neighbor1.set('nome', 'Colombia')
neighbor1.set('direzione', 'E')

# STAMPA
print(sep+"dump"+sep)
ET.dump(data)


print(sep+"figli"+sep)
for child in data:
	print(child.tag, child.attrib)

print(sep+"testo"+sep)
print(data[0][2].text)

print(sep+"vicini"+sep)
for neighbor in data.iter('vicino'):
	print(neighbor.attrib)
	print(neighbor.attrib['nome'])

print(sep+"nome e punteggio"+sep)
for country in data.findall('citta'):
	rank = country.find('punteggio').text
	name = country.get('nome')
	print(name, rank)

for rank in data.iter('punteggio'):
	new_rank = int(rank.text) + 1
	rank.text = str(new_rank)
	rank.set('updated', 'yes')
print(sep+"dump update"+sep)
ET.dump(data)

print(sep+"cat pytoxml.xml"+sep)
tree = ET.ElementTree(data)
tree.write('pytoxml.xml')
catfile('pytoxml.xml')

print(sep+"cat pytoxml-ok.xml minidom"+sep)
indenta('pytoxml.xml','pytoxml-ok.xml')
catfile('pytoxml-ok.xml')

print(sep+"remove"+sep)
for country in data.findall('citta'):
	rank = int(country.find('punteggio').text)
	if rank == 5:
		data.remove(country)
tree.write('pytoxml.xml')

indenta('pytoxml.xml','pytoxml-ok.xml')
catfile('pytoxml-ok.xml')
'''
import json
named_entity = {"form":"Bob", "type":"firstname", "span":[0,1,2]}
print(named_entity)
serialized = json.dumps(named_entity, indent=4, sort_keys=True)
print(serialized)
restored = json.loads(serialized)
print(restored)
with open("my_json.json", "w") as nfile:
	json.dump(restored, nfile, indent=3)
'''
