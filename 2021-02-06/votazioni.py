import random as r
    
def dizionario_inizializza():
    #cognomi = [ "Rossi", "Ferrari", "Russo", "Bianchi", "Romano", "Gallo", "Costa", "Fontana", "Conti", "Esposito", "Ricci", "Bruno", "De Luca", "Moretti", "Marino", "Greco", "Barbieri", "Lombardi", "Giordano", "Innocenti", "Colombo", "Mancini", "Longo", "Leone", "Martinelli", "Marchetti", "Martini", "Galli", "Gatti", "Mariani"]
    #for i in cognomi:
        #studenti[i] = r.randint(18, 30)
        
    while len(studenti) < num_studenti:
        studenti[r.randint(1000, 2000)] = r.randint(18, 30)
    #print(len(studenti))
        

def stampa_studenti_ordinati():
    print("stampo elenco matricole con voto ordinati per voto in maniera crescente")
    for chiave in sorted(studenti, key = studenti.get):
        print("matricola", chiave, "=", studenti[chiave])

def stampa_voti_distinti():
    print("stampo elenco voti distinti")
    for voto in set(studenti.values()):
        print("voto =", voto)

def main():
    global num_studenti
    global studenti
    
    num_studenti = 30
    studenti = {}
    
    dizionario_inizializza()
    
    while True:
        print("\nOperazioni possibili")
        print("[1] Mostra elenco matricole con voto \n[2] Mostra elenco voti distinti \n[3] Esci ")
        scelta = input("cosa vuoi fare ")
        if not scelta.isdigit():
            print("\nErrore nella digitazione, riprova ...\n")
        else:
            scelta_int = int(scelta)
            if scelta_int == 1:
                stampa_studenti_ordinati()
            elif scelta_int == 2:
                stampa_voti_distinti()
            elif scelta_int == 3:
                print("\nArrivederci\n")
                break
            else:
                print("\nErrore nella digitazione, riprova ...\n")
main()
