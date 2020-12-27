print("benvenuto in questo gioco matematico.")
print("bisogna inserire 2 numeri e se il prodotto di questi è maggiore di 10\
calcolerò la differenza tra il primo e il secondo")
print("se il prodotto è minore o uguale a 10 calcolerò la somma dei due numeri")
    
while True:
    
    a = int(input("\ninserisci il primo numero "))
    b = int(input("inserisci il secondo numero "))
    if a*b > 10:
        print("\nil prodotto dei due numeri è maggiore di 10, precisamente", a*b)
        print("quindi calcolerò la differenza tra il primo e il secondo")
        print("\nla differenza è", a-b)
    else:
        if a*b < 10:
            print("\nil prodotto dei due numeri è minore di 10, precisamente", a*b)
        else:
            print("\nil prodotto dei due numeri è uguale a 10")    
        print("quindi calcolerò la somma dei due numeri")
        print("\nla somma è", a+b)
    while True:
        ripetizione = input("\nvuoi riprovare? Rispondi con sì o con no ")
        if ripetizione != "sì" and ripetizione != "no":
            print("errore nella digitazione\npuoi rispondere con:\n-sì\n-no")
        else:
            break
    if ripetizione == "no":
        break