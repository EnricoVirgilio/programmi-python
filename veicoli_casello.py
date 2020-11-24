print("benvenuto nel programma che somma e da la media di quanti veicoli sono transitati in un casello in tot giorni\n")
giorni = int(input("inserisci numero giorni "))
veicoli = []
veicoli2 = []
somma_risultati = []
contatore = 0
contatore1 = 0
somma = 0
while True: 
    if contatore == 0:
        veicolo = input("dimmi un tipo di veicolo passato al casello(al plurale) ")
        nuovi_veicoli = input("vuoi dirmi altri veicoli?  rispondi con 0 se vuoi finire o con 1 se vuoi continuare ")
        veicoli.append(veicolo)
    else:
        nuovi_veicoli = input("vuoi dirmi altri veicoli? rispondi con 0 se vuoi finire o con 1 se vuoi continuare ")
    if nuovi_veicoli == "0":
        break
    elif nuovi_veicoli != "1":
        print("penso che tu abbia sbagliato a digitare, le risposte possibili sono: \n-1 ,se vuoi continuare\
        \n-0 ,se vuoi chiudere")
        contatore = 1
    else:
        contatore = 0
    
for date in range(1, giorni+1):
    for numero_veicolo in range(1, len(veicoli)+1):
        veicoli2.append(veicoli[numero_veicolo-1])
        domanda_input = "quanti/e " + str(veicoli2[0]) + " sono passati il giorno numero " + str(date) + " "
        numero_di_veicoli = int(input(domanda_input))
        somma_risultati.append(numero_di_veicoli)
        if numero_veicolo == len(veicoli)+1:
            break
        veicoli2 = []

for resto in range(1, len(veicoli)+1):      
    while contatore1 < len(somma_risultati):
        if contatore1 % len(veicoli) == resto -1:
            somma += somma_risultati[contatore1]
        contatore1 += 1
            
    print("\nla somma dei/delle", veicoli[resto -1], "passati/e al casello in", giorni, "giorni è uguale a", somma)
    print("la media dei/delle", veicoli[resto -1], "passati/e al casello ogni giorno è uguale a", round(somma/giorni, 2))
    somma = 0
    contatore1 = 0
        
somma_totale = sum(somma_risultati)
print("\nin totale sono passati in", giorni, "giorni", somma_totale, "veicoli")
print("la media totale dei veicoli passati al casello ogni giorno è uguale a", round(somma_totale/giorni, 2))