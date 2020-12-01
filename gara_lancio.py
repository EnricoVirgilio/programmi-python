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
    x = int(input("vuoi inserire altri candidati, digita 1 se sì, digita 0 se no "))
    if x == 0:
        break
    else: 
        continue
print("il vincitore della gara è", nome_e_lanci[nome_e_lanci.index(lanci[0]) - 1], "con un lancio\
di", max(lanci), "metri")