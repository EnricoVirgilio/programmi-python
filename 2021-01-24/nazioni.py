def main():
    print("benvenuto nel programma che ti dice la capitale di una nazione a tua scelta.")
    print("Il programma, però, non conosce tutte le nazioni")

    nazioni = ["Italia", "Francia", "Spagna", "Germania", "Australia", 
    "Portogallo", "Norvegia", "Svizzera", "Svezia", "USA", "Russia", "Cina"]
    capitali = ["Roma", "Parigi", "Madrid", "Berlino", "Canberra", 
    "Lisbona", "Oslo", "Berna", "Stoccolma", "Washington", "Mosca", "Pechino"]
    while True:
        stato = input("inserisci il nome dello stato di cui vuoi conoscere la capitale ")
        if stato not in nazioni:
            print("Il programma non conosce questa nazione")
            print("la nazioni che conosco sono:")
            for naz in nazioni:
                print("-", naz)
            print("Riprova")
            continue
        else:
            capitale = capitali[nazioni.index(stato)]
            print("la capitale di", stato, "è", capitale)
        while True:
            ripetizione = input("vuoi riprovare? ")
            if ripetizione == "sì" or ripetizione == "no":
                break
            else:
                print("errore nella digitazione, le risposte possibili sono: \n -sì \n -no. \n Riprova")       
        if ripetizione == "no":    
            break
main()