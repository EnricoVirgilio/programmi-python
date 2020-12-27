print("benvenuto nel programma che calcola la media degli stipendi \
della tua azienda o in euro o sterline o dollari o tutti e tre\n")

stipendi = []
contatore = 0
while True:
    valuta = input("inerisci la valuta con cui vuoi scrivere gli stipendi ")
    if valuta == "dollari" or valuta == "euro" or valuta == "sterline":
        break
    else:
        print("penso che tu abbia sbagliato a digitare")
        print("le risposte accettabili sono: \n-dollari \n-euro \n-sterline")

print("\nora ti chiederò di dirmi gli stipendi dei dipendenti senza la valuta, quando avrai \
finito di inserirli scrivi -1 al posto dello stipendio")
while True:
    contatore += 1
    richiesta_input = "inserisci lo stipendio mensile dipendente " + str(contatore) + " "
    stipendio_mensile = int(input(richiesta_input))
    if stipendio_mensile < -1:
        print("penso che tu abbia sbagliato a digitare, puoi inserire soltanto numeri positivi")
        contatore -= 1
    elif stipendio_mensile == -1:
        break
    else:
        stipendi.append(stipendio_mensile)
    
richiesta_input2 = "desideri calcolare la media in tutte e tre le valute o soltanto in " + valuta + " "
media = sum(stipendi)/len(stipendi)
while True:
    valuta_della_media = input(richiesta_input2)
    if valuta_della_media == valuta:
        print("la media degli stipendi in", valuta, "è uguale a", round(media, 2))
        break
    elif valuta_della_media == "tutte e tre":
        if valuta == "dollari":
            print("la media degli stipendi in", valuta, "è uguale a ", round(media, 2))
            print("la media degli stipendi in euro è uguale a", round(media*0.84, 2))
            print("la media degli stipendi in sterline è uguale a", round(media*0.75, 2))
        elif valuta == "euro":
            print("la media degli stipendi in", valuta, "è uguale a ", round(media, 2))
            print("la media degli stipendi in dollari è uguale a", round(media*1.18, 2))
            print("la media degli stipendi in sterline è uguale a", round(media*0.89, 2))
        else:
            print("la media degli stipendi in", valuta, "è uguale a ", round(media, 2))
            print("la media degli stipendi in euro è uguale a", round(media*1.12, 2))
            print("la media degli stipendi in dollari è uguale a", round(media*1.33, 2))
        break
        
    else:
        print("penso che tu abbia sbagliato a digitare, le risposte accettabili sono: \n-tutte e tre \n-", valuta)