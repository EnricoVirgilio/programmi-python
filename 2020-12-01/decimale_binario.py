print("benvenuto nel programma che calcola il numero binario corrispondente a un numero decimale")
NUMERO_DECIMALE_INIT = int(input("dimmi il numero che vuoi trasformare in binario "))
numero_decimale = NUMERO_DECIMALE_INIT
numero_binario = ""
NUMERO_BINARIO = str(bin(NUMERO_DECIMALE_INIT)) 
while True:
    cifra = numero_decimale % 2
    numero_decimale //= 2
    numero_binario += str(cifra)
    if numero_decimale == 0:
        break
print("\nil numero decimale trasformato in binario è, secondo il mio programma, uguale a", numero_binario[::-1])
print("\nil numero decimale trasformato in binario è, secondo la funzione predefinita di python\
, uguale a", NUMERO_BINARIO[2:])
if numero_binario[::-1] == NUMERO_BINARIO[2:]:
    print("\ni due numeri coincidono")     