print("benvenuto nel programma che calcola quanti veicoli sono passati in un \
casello autostradale in tot giorni\n")
contatore = 1
veicoli = []
print("ora mi dovrai quanti veicoli sono passati giorno per giorno al casello, \
quando avrai finito digita 0 al posto del numero di veicoli")
while True: 
    richiesta_input = "quanti veicoli sono passati al casello il giorno numero " + str(contatore) + " "
    numero_veicoli = int(input(richiesta_input))
    veicoli.append(numero_veicoli)
    if numero_veicoli == 0:
        break
    else:
        contatore +=1

print("il numero di veicoli passati in", contatore -1, "giorni è uguale a", sum(veicoli))