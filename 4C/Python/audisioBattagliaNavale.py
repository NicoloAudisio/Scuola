#Audisio 4C esercizio

campo = [[0,0,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0,0,1],[1,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0]]
naviColpite = []
counter = 0
colpiti = 0
uscita = 0

while uscita == 0:
	colpi = int(input("Quanti colpi hai a disposizione: "))
	while colpi < 1 or colpi > 100:
		colpi = int(input("\nErrore!\nQuanti colpi hai a disposizione: "))
	for i in range(colpi):
		print("Hai ancora a disposizione ", colpi - counter, "colpi!\n");
		cX = int(input("Inserisci le coordinate x: "))
		while cX < 0 or cX > 9:
			cX = int(input("\nErrore!\nInserisci le coordinate x: "))
		cY = int(input("Inserisci le coordinate y: "))
		while cY < 0 or cX > 9:
			cY = int(input("\nErrore!\nInserisci le coordinate y: "))
		if campo[cX][cY] == 'X' or campo[cX][cY] == "/":
			cX = int(input("\nAttenzione qua hai già colpito!\nInserisci le coordinate x: "))
			while cX < 0 or cX > 9:
				cX = int(input("\nErrore!\nInserisci le coordinate x: "))
			cY = int(input("Inserisci le coordinate y: "))
			while cY < 0 or cX > 9:
				cY = int(input("\nErrore!\nInserisci le coordinate y: "))
		elif campo[cX][cY] == 1:
			print("Colpito e affondato!\n")
			campo[cX][cY] = "/"
			counter += 1
			colpiti += 1
			campo[cX][cY] = "X"
		else:
			campo[cX][cY] = "X"
			print("Mare\n")
			counter += 1
	if colpiti == 1:
		print("\nHai affondato una nave!\n")
	elif colpiti == 0:
		print("\nNon hai colpito navi!\n")	
	elif colpiti > 1:
		print("\nHai affondato ", colpiti, "navi!\n")
	continuo = input("Vuoi ancora giocare (yes - no): ")
	if continuo == "yes":
		uscita = 0
	elif continuo == "no":
		uscita = 1
	else:
		print("Errore!\n")
		exit(-1)
	 
