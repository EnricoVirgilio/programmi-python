def calcola_imposta(reddito):
    if reddito <= 15000:
        imposta = imposta_0_15000(reddito)
        print("\nL'imposta è uguale a:", imposta)
        
    elif reddito > 15000 and reddito <= 28000:
        imposta = imposta_15000_28000(reddito)
        print("\nL'imposta è uguale a:", imposta)

    elif reddito > 28000 and reddito <= 55000:
        imposta = imposta_28000_55000(reddito)
        print("\nL'imposta è uguale a:", imposta)
        
    elif reddito > 55000 and reddito <= 75000:
        imposta = imposta_55000_75000(reddito)
        print("\nL'imposta è uguale a:", imposta)
        
    elif reddito > 75000:
        imposta = imposta_maggiore_75000(reddito)
        print("\nL'imposta è uguale a:", imposta)
        
    tassazione_media =calcola_tassazione_media(imposta, reddito)
    print("La tassazione media è uguale a:", round(tassazione_media, 2), "%")
        
def imposta_0_15000(reddito = 15000):
    imposta = reddito*aliquote[0]
    return imposta
    
def imposta_15000_28000(reddito = 28000):
    imposta = imposta_0_15000() + (reddito - 15000)*aliquote[1]
    return imposta

def imposta_28000_55000(reddito = 55000):
    imposta = imposta_15000_28000() + (reddito - 28000)*aliquote[2]
    return imposta

def imposta_55000_75000(reddito = 75000):
    imposta = imposta_28000_55000() + (reddito - 55000)*aliquote[3]
    return imposta
    
def imposta_maggiore_75000(reddito):
    imposta = imposta_55000_75000() + (reddito - 75000)*aliquote[4]
    return imposta

def calcola_tassazione_media(imposta, reddito):
    tassazione_media = imposta/reddito*100
    return tassazione_media

def main():
    global aliquote
    aliquote = [0.23, 0.27, 0.38, 0.41, 0.43]
    while True:
        print("\nOperazioni possibili")
        print("[1] Calcola imposta \n[2] Esci ")
        scelta = input("cosa vuoi fare ")
        if not scelta.isdigit():
            print("\nErrore nella digitazione, riprova ...\n")
        else:
            scelta_int = int(scelta)
            if scelta_int == 1:
                while True:
                    reddito = input("\nInserisci reddito ")
                    if not reddito.isdigit():
                        print("\nErrore nella digitazione, riprova ...")
                    else:
                        calcola_imposta(int(reddito))
                        break
            elif scelta_int == 2:
                print("\nArrivederci\n")
                break
            else:
                print("\nErrore nella digitazione, riprova ...\n")
    
main()