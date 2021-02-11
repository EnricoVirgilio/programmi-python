'''
I nomi delle città e i corrispondenti Codici di Avviamento Postale (CAP) vengono inseriti da tastiera e 
memorizzati in un dizionario dove il CAP è la chiave. Fornito poi da tastiera il nome di una città, costruisci
un programma che visualizzi il suo CAP oppure un messaggio nela caso la città non sia compresa nell'elenco.
Analogamente, fornendo il CAP restituisce il nome della città oppure un messaggio di errore
'''

def aggiungi_CAP():
    CAP = int(input("inserisci CAP di una città "))
    citta = input("inserisci la città corrispondente al CAP ")
    CAP_citta[CAP] = citta
    print(CAP_citta)
    
def inverti_dizionario(dizionario):
    dict_flipped = {}
    for chiave in dizionario:
        dict_flipped[dizionario[chiave]] = chiave
    return dict_flipped

def cerca_citta_tramite_CAP():
    if CAP_citta == {}:
        print("\nIl dizionario è vuoto")
    else:
        citta = input("inserisci il nome citta di cui vuoi vedere il CAP ")
        citta_CAP = inverti_dizionario(CAP_citta)
        if citta in citta_CAP:
            print("\nIl CAP di", citta, "è", citta_CAP[citta])
        else:
            print("\nla città cercata non è presente nell'elenco ")
            
def cerca_CAP_tramite_città():
    if CAP_citta == {}:
        print("\nIl dizionario è vuoto")
    else:
        CAP = int(input("inserisci il CAP di cui vuoi vedere la città "))
        if CAP in CAP_citta:
            print("\nla città con CAP", CAP, "è", CAP_citta[CAP])
        else:
            print("\nIL CAP cercato non è presente nell'elenco")
    

def mostra_elenco_citta():
    print("Stampo elenco citta")
    if CAP_citta == {}:
        print("\nIl dizionario è vuoto")
    else:    
        for CAP in CAP_citta:
            print("-", CAP_citta[CAP])
            
def mostra_elenco_CAP():
    print("Stampo elenco CAP")
    if CAP_citta == {}:
        print("\nIl dizionario è vuoto")
    else:    
        for CAP in CAP_citta:
            print("-", CAP)
    
def main():
    global CAP_citta
    CAP_citta = {}
    while True:
        print("\nOperazioni possibili")
        print("[1] Aggiungi CAP \n[2] Cerca CAP dalla città \n[3] Cerca città dal \
CAP \n[4] Stampa elenco citta \n[5] Stampa elenco CAP \n[6] Esci")
        
        scelta = input("Cosa vuoi fare? ")
        
        if not scelta.isdigit():
            print("\nErrore nella digitazione, riprova ...\n")
        else:
            scelta_int = int(scelta)
            if scelta_int == 1:
                aggiungi_CAP()
            elif scelta_int == 2:
                cerca_citta_tramite_CAP()
            elif scelta_int == 3:
                cerca_CAP_tramite_città()
            elif scelta_int == 4:
                mostra_elenco_citta()
            elif scelta_int == 5:
                mostra_elenco_CAP()
            elif scelta_int == 6:
                break
            else:
                print("\nErrore nella digitazione, riprova ...\n")
    
main()