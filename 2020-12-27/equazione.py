print("benvenuto nel programma che calcola il risultato di un equazione")
print("l'equazione è di tipo ax + b = 0")
def equazione():
    global a
    global b
    a = int(input("\ninserisci coefficiente a "))
    b = int(input("inserisci coefficiente b "))
    if a == b and a == 0:
        print("l'equazione è indeterminata")
    elif a == 0 and b != 0:
        print("l'equazione è impossibile")
    elif b == 0 and a != 0:
        print("l'equazione risulta 0")
    else:
        print("l'equazione risulta", -b/a)
        
equazione()

while True:
    ripetizione = input("Vuoi riprovare? Rispondi con si o no ")
    if ripetizione == "sì":
        equazione()
    elif ripetizione == "no":
        break
    else:
        print("\nerrore nella digitazione.\nPuoi rispondere soltanto con:\n-sì\n-no")    