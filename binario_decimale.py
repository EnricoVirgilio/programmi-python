print("benvenuto nel programma che calcola il numero decimale corrispondente a un numero binario")
lenght = int(input("dimmi il numero di cifre del numero binario che vuoi trasformare "))
numero_decimale = 0
contatore_esponente = 0
lista_cifre = []
numero_binario = ""
for numero in range(1, lenght + 1):
    while True:
        cifra = int(input("dimmi la " + str(numero) +".a cifra a partire da destra" + " "))
        if cifra != 1 and cifra != 0:
            print("valore errato, le risposte accettabili sono 0 ed 1")
            continue
        else:
            numero_decimale += (2**contatore_esponente)*cifra
            contatore_esponente += 1
            numero_binario += str(cifra)
            break

print("il numero binario che hai inserito è", numero_binario[::-1])
print("\nil numero binario trasformato in decimale è, secondo il mio programma, uguale a", numero_decimale)
print("\nil numero binario trasformato in decimale è, secondo la funzione predefinita di python\
, uguale a", int(numero_binario[::-1], 2))
print("i due numeri coincidono")
