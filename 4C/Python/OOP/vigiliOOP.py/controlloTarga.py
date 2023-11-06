import re

def controllare_targa(targa):
	# Verifica se la targa è composta da 7 caratteri alfanumerici
	if not re.match(r"^[A-Za-z0-9]{7}$", targa):
		return False

	# Verifica se la prima due caratteri sono alfabetici
	if not targa[:2].isalpha():
		return False

	# Verifica se i caratteri tra la 2 e la 4 sono numerici
	if not targa[2:5].isdigit():
		return False

	# Verifica se gli ultimi due caratteri sono alfabetici
	if not targa[5:].isalpha():
		return False

	return True

print(controllare_targa("AA123AA")) # True
print(controllare_targa("ABC1234"))