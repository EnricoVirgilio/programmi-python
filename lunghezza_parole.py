print("benvenuto nel programma che calcola la lunghezza delle parole")
numero_parole = int(input("inserisci il numero di parole che vuoi inserire"))
lista_parole = []
parole_e_lunghezza = []
for parole in range(1, numero_parole+1):
    parola = input("inserisci parola numero" + str(parole) + " ")
    lista_parole.append(parola)
    parole_e_lunghezza.append(parola)
    parole_e_lunghezza.append(len(parola))
while lista_parole != []:
    print("la parola", lista_parole[0], "è lunga\
", str(parole_e_lunghezza[parole_e_lunghezza.index(lista_parole.pop(0)) +1]))