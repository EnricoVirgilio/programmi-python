print("benvenuto nel programma che calcola la percentuale dei voti di ogni candidato in una elezione")
candidati = int(input("inserisci il numero dei candidati "))
votazioni = []

for voti in range(1, candidati+1):
    x = "inserisci numero voti candidato numero" + str(voti) + " "
    voto = int(input(x))
    votazioni.append(voto)

for risultati in range(0, len(votazioni)):
    print("risultato candidato" + str(risultati + 1) + " ")
    print(str(votazioni[risultati]/sum(votazioni)*100) + "%")
