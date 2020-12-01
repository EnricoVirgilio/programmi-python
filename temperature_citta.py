print("bevenuto nel programma che ti dice quali città hanno superato un valore stabilito di \
escursione termica in un giorno")
val_stab = int(input("inserisci il valore di escursione termica\n"))
num_città = int(input("inserisci il numero di città\n"))
nomi_città = []
escurs_term = []
contatore = 0
for città in range(1, num_città + 1):
    nom_città = input("\ninserisci nome città numero " + str(città) + " ")
    while True:      
        min_città = int(input("inserisci temperatura minima città numero" + str(città) + " "))
        max_città = int(input("inserisci temperatura massima città numero" + str(città) + " "))
        if min_città > max_città:
            print("valore errato, la temperatura minima non può essere maggiore di quella \
massima. Riprova")
            continue
        else:
            break
    if max_città - min_città > val_stab:
        escurs_term.append(max_città - min_città)
        nomi_città.append(nom_città)
        contatore += 1
print("le città che hanno superato il valore prestabilito di escursione termica sono\
:", contatore,"\n")
print("queste città sono:")
for escursione_termica in range(1, len(escurs_term) + 1):
    print("-", nomi_città.pop(0), "con un escursione di " , str(escurs_term.pop(0)), "gradi")