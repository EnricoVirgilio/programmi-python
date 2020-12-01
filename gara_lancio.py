print("benvenuto nel programma che ti dice il migliore di una gara di lancio del peso")
lanci = []
contatore = 1
nome_e_lanci = []
while True:
    nome_candidato = input("inserisci nome candidato numero" + str(contatore) + " ")
    lancio_candidato = input("inserisci la lunghezza del lancio del candidato numero" + str(contatore) + " ")
    nome_e_lanci.append(nome_candidato)
    nome_e_lanci.append(lancio_candidato)
    lanci.append(lancio_candidato)
    contatore += 1
    nuovo_candidato = int(input("vuoi inserire altri candidati, digita 1 per il sì, digita 0 per il no "))
    if nuovo_candidato == 0:
        break
lanci.sort(reverse = True, key = int)
print("il vincitore della gara è", nome_e_lanci[nome_e_lanci.index(lanci[0]) - 1], "con un lancio di", lanci[0], "metri")
