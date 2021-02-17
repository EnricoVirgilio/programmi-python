def percentuale_vendite(lista_fatturati, fatturato, zona):
    somma = sum(lista_fatturati)
    if zona != "Isole":
        print("la percentuale delle vendite nel", zona, "è", round(fatturato/somma*100, 2), "%")
    else:
        print("la percentuale delle vendite nelle", zona, "è", round(fatturato/somma*100, 2), "%")

def main():
    contatore = 0
    zone = ["Nord", "Centro", "Sud", "Isole"]
    lista_fatturati = []
    for zona in zone:
        fatturato = int(input("Inserisci il fatturato del " + zona + " "))
        lista_fatturati.append(fatturato)
    print("\nil fatturato totale è uguale a", sum(lista_fatturati))
    
    while contatore < len(zone):
        percentuale_vendite(lista_fatturati, lista_fatturati[contatore], zone[contatore])
        contatore += 1
main()