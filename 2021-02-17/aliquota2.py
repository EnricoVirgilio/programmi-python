def imponibili_inizializza(reddito):
    i = 0
    while i < len(aliquote):
        if reddito > intervalli[i]:
            imponibili.append(intervalli[i])
        else:
            if reddito < 0:
                imponibili.append(0)
            else:
                imponibili.append(reddito)
        reddito -= imponibili[i]
        i += 1
        
def calcola_imposta():
    i = 0
    imposta = 0
    while i < len(aliquote):
        imposta += imponibili[i] * aliquote[i] / 100
        i += 1
    return imposta
    
def calcola_tassazione_media(imposta, reddito):
    tassazione_media = imposta/reddito*100
    return tassazione_media
    
def main():
    global aliquote, intervalli, imponibili
    aliquote = [23, 27, 38, 41, 43]
    intervalli = [15000, 13000, 27000, 20000, 99999999999999999999]
    imponibili = []
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
                        imponibili_inizializza(int(reddito))
                        imposta = calcola_imposta()
                        print("l'imposta di", reddito, "€ è", imposta, "€")
                        tassazione_media = calcola_tassazione_media(imposta, int(reddito))
                        print("La tassazione media è uguale a:", round(tassazione_media, 2), "%")
                        imponibili = []
                        break
            elif scelta_int == 2:
                print("\nArrivederci\n")
                break
            else:
                print("\nErrore nella digitazione, riprova ...\n")
    
main()