while True:
    print("benvenuto nel programma che ti dice se un numero è pari o dispari")
    numero = int(input("inserisci il numero "))
    if numero % 2 == 0:
        print(numero, "è un numero pari")
    else:
        print(numero, "è un numero dispari")
    while True:
        ripetizione = input("vuoi riprovare? ")
        if ripetizione != "sì" and ripetizione != "no":
            print("errore nella digitazione. Riprova")
        else: 
            break
    
    if ripetizione == "no":
        break        
        
        
            
