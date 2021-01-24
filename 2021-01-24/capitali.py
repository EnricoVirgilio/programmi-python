def main():
    print("benvenuto nel programma che ti dice lo stato di una capitale a tua scelta.")
    print("Il programma, però, non conosce tutte le capitali")
    naz_cap = {
        "Italia": "Roma",
        "Francia": "Parigi",
        "Spagna": "Madrid",
        "Germania": "Berlino",
        "Australia": "Canberra",
        "Portogallo": "Lisbona",
        "Norvegia": "Oslo",
        "Svizzera": "Berna",
        "Svezia": "Stoccolma", 
        "USA": "Washington",
        "Russia": "Mosca", 
        "Cina": "Pechino"
    }
    cap_naz = {}

    for nazione in naz_cap:
        cap_naz[naz_cap[nazione]] = nazione
    #print(cap_naz)
    while True:
            capitale = input("inserisci il nome della capitale di cui vuoi conoscere lo stato ")
            if capitale not in cap_naz:
                print("Il programma non conosce questa nazione")
                print("le capitali che conosco sono:")
                for stato in naz_cap:
                    print("-", naz_cap[stato])
                continue
            else:
                stato = cap_naz[capitale]
                print("lo stato con capitale", capitale, "è", stato)
            while True:
                ripetizione = input("vuoi riprovare? ")
                if ripetizione == "sì" or ripetizione == "no":
                    break
                else:
                    print("errore nella digitazione, le risposte possibili sono: \n -sì \n -no. \n Riprova")       
            if ripetizione == "no":    
                break
main()