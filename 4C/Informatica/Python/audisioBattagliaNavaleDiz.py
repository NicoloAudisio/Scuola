#Audisio 4C esercizio
x = 0
y = 0

campo = {(2,3): '2',(2,4): '2', (4,1): '3', (5,1): '3', (6,1): '3', (1,8): '4', (2,8): '4', (3,8): '4', (4,8): '4'}
nave2 = 2
nave3 = 3
nave4 = 4
rimasti = 9

while rimasti > 0:
    x = int(input("Inserisci le coordinate x: "))
    while x < 0 or x > 10:
        x = int(input("\nErrore!\nInserisci le coordinate x: "))
    y = int(input("Inserisci le coordinate y: "))
    while y < 0 or y > 10:
        y = int(input("\nErrore!\nInserisci le coordinate y: "))
    if (x,y) in campo:
        if campo[x,y] == '2':
            nave2 -= 1
            campo[x,y] = '/'
            rimasti -= 1
            if nave2 == 0:
                print("\nColpito e affondato!\n")
            else:
                print("\nColpito!\n")
        elif campo[x,y] == '3':
            nave3 -= 1
            campo[x,y] = '/'
            rimasti -= 1
            if nave3 == 0:
                print("\nColpito e affondato!\n")
            else:
                print("\nColpito!\n")
        elif campo[x,y] == '4':
            nave4 -= 1
            campo[x,y] = '/'
            rimasti -= 1
            if nave4 == 0:
                print("\nColpito e affondato!\n")
            else:
                print("\nColpito!\n")
        else:
            print("\nAcqua!\n")
    else:
        print("\nAcqua!\n")
print("Hai affondato tutte le navi\n")