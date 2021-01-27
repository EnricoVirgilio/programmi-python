''' Organizza con un dizionario i dati sui conti correnti bancari con numero del conto e saldo. Fornito 
poi il numero di conto, il programma visualizza il saldo oppure un messaggio nel caso in cui il conto non 
sia presente nella mappa
'''
import random as r

# Aggiunge un conto e il relativo saldo al dizionario conti_elenco
def conto_aggiungi(conto_numero, conto_saldo):    
    # Controllo che il numero conto non sia già presente
    if conto_numero not in conti_elenco:
        conti_elenco[conto_numero] = conto_saldo
    else:
        print("Il numero conto", conto_numero, "è già presente nell'elenco conti")
        
# inizializzo elenco conti
def conti_elenco_inizializza(conti_elenco_numero):    
    print("Genero", conti_elenco_numero, "conti casualmente")
    i = 1
    while i <= conti_elenco_numero:
        conto_numero = r.randint(1000, 2000)
        if conto_numero in conti_elenco:
            continue
        conto_saldo = r.randint(3000, 4000)
        conto_aggiungi(conto_numero, conto_saldo)
        i += 1
        
# Stampa conti_elenco x controllare se ci sono errori
def conti_elenco_stampa():    
    print('Ci sono ', len(conti_elenco), 'conti')
    if len(conti_elenco) < 1:
        print("Non è presente alcun conto")
    else:
        for conto_numero in conti_elenco:
            print("Numero conto:", conto_numero, "saldo conto:", conti_elenco[conto_numero])
        
def conto_cerca():
    while True:
        conto_richiesto = int(input("Inserisci il numero di conto di cui vuoi vedere il saldo "))
        if conto_richiesto in conti_elenco:
            print("Il saldo del conto è", conti_elenco[conto_richiesto])
            break
        else:
            print("Il conto non è presente nell'elenco")
            conto_aggiungi = input("Vuoi aggiungere un nuovo conto? Rispondi con sì o no ")
            if conto_aggiungi == "sì":
                conto_aggiungi_utente()
def conto_aggiungi_utente():
    conto_numero = int(input("Inserisci un nuovo numero di conto "))
    conto_saldo = int(input("Inserisci il saldo del conto "))
    conto_aggiungi(conto_numero, conto_saldo)
    
def main():
    global conti_elenco
    conti_elenco = {}
    conti_elenco_numero = 10
    conti_elenco_inizializza(conti_elenco_numero)
    conti_elenco_stampa()
    conto_cerca()
main()