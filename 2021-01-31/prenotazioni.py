import time

def persona_aggiungi():
    persona = {}
    #
    nome = input("\nInserisci nome persona: ")
    cognome = input("Inserisci cognome persona: ")
    mail = input("Inserisci mail: ")
    #
    persona["nome"] = nome.lower().capitalize()
    persona["cognome"] = cognome.lower().capitalize()
    persona["mail"] = mail.lower()
    persona["data_eng"] = time.strftime("%Y-%m-%d %H:%M:%S")
    persona["data_ita"] = time.strftime("%d-%m-%Y %H:%M:%S")
    persona["conferma"] = 0
    #
    chiave = len(elenco_iscritti)
    elenco_iscritti[chiave] = persona
    print("%s %s Iscritto correttamente" % (persona["nome"], persona["cognome"]))
    #stampa_persona(persona)
    
def stampa_elenco_complessivo():
    if len(elenco_iscritti) == 0:
        print("\nNon ci sono persone iscritte")
    else:
        print("\nNOME".ljust(20, ' '), "COGNOME".ljust(20, ' '), "DATA".ljust(20, ' '), "EMAIL")
        for chiave in elenco_iscritti:
            persona = elenco_iscritti[chiave]
            stampa_persona(persona)
        
def stampa_elenco_da_confermare():
    contatore = 0
    for chiave in elenco_iscritti:
        persona = elenco_iscritti[chiave]
        if persona["conferma"] == 1:
            continue
        if chiave == 0:
            print("\nNOME".ljust(20, ' '), "COGNOME".ljust(20, ' '), "DATA".ljust(20, ' '), "EMAIL")
        stampa_persona(persona)
        persona["conferma"] = 1
        contatore += 1
    if contatore == 0:
        print("\nNon ci sono persone da confermare")
        
def stampa_persona(persona):
    print(persona["nome"].ljust(20, ' '), persona["cognome\
"].ljust(20, ' '), persona["data_ita"].ljust(20, ' '), persona["mail"])
    
def main():
    global elenco_iscritti
    elenco_iscritti = {}
    
    while True:
        print("\nOperazioni possibili")
        print("[1] Aggiungi persona \n[2] Mostra elenco complessivo \n[3] Mostra elenco solo delle persone \
da confermare \n[4] Esci")
        
        scelta = input("Cosa vuoi fare? ")
        
        if not scelta.isdigit():
            print("\nErrore nella digitazione, riprova ...\n")
        else:
            scelta_int = int(scelta)
            if scelta_int == 1:
                persona_aggiungi()
            elif scelta_int == 2:
                stampa_elenco_complessivo()
            elif scelta_int == 3:
                stampa_elenco_da_confermare()
            elif scelta_int == 4:
                print("\nArrivederci\n")
                break
            else:
                print("\nErrore nella digitazione, riprova ...\n")

main()
