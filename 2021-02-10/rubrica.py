''' 
Organizza un dizionario con i nomi delle persone e i rispettivi numeri telefonici. Fornito poi il nome
della persona, lil programma visualizza il suo numero di telefono oppure un messaggio nel caso la persona non 
sia presente nella rubrica
'''

import random as r

def rubrica_inizializza():
    cognomi = ["Ferrari", "Rossi", "Magnani", "Barbieri", "Montanari", 
"Guidetti", "Catellani", "Benassi", "Ferretti", "Davoli"]
    nomi = ["Marco", "Andrea", "Stefano", "Paolo", "Giuseppe", "Roberto", 
"Luca", "Francesco", "Massimo", "Alessandro"]
    for cognome in cognomi:
        rubrica[cognome + " " + nomi[r.randint(0, 9)]] = "0522" + str(r.randint(100000, 999999))

def numero_cerca():
    nome = input("Inserire cognome e nome della persona di cui si vuole vedere il numero di telefono.\nCognome \
e nome devono essere separati da uno spazio ")
    if nome in rubrica:
        print("\nil numero di", nome, "è", rubrica[nome])
    else:
        print("\nLa persona cercata non è presente nella rubrica")
        
def stampa_elenco_nomi():
    print("Stampo elenco nomi")
    for chiave in rubrica:
        print("-", chiave)
    
def main():
    global rubrica
    rubrica = {}
    rubrica_inizializza()
    while True:
        print("\nOperazioni possibili")
        print("[1] Cerca numero persona \n[2] Mostra elenco persone \n[3] Esci")
        
        scelta = input("Cosa vuoi fare? ")
        
        if not scelta.isdigit():
            print("\nErrore nella digitazione, riprova ...\n")
        else:
            scelta_int = int(scelta)
            if scelta_int == 1:
                numero_cerca()
            elif scelta_int == 2:
                stampa_elenco_nomi()
            elif scelta_int == 3:
                break
            else:
                print("\nErrore nella digitazione, riprova ...\n")

main()