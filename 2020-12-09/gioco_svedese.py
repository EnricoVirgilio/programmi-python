print("benvenuto nel programma che, secondo un gioco svedese, raddoppia tutte le \
consonanti di una parola o di una frase e ci inserisce una o tra le due consonanti.")
print("questo gioco è chiamato Rövarspråket")
def gioco_svedese():
    global vocali
    global alfabeto
    vocali = "aeiou"
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    parola = input("inserisci la parola o la frase ")
    parola2 = ""
    for lettera in parola:
        if lettera.lower() not in alfabeto:
            parola2 += lettera
        elif lettera.lower() not in vocali:
            parola2 = parola2 + lettera + "o" + lettera
        else:
            parola2 += lettera
    print(parola2)

gioco_svedese()

while True:
    ripetizione = input("vuoi riprovare? Rispondi con sì o no\n")
    if ripetizione == "sì":
        gioco_svedese()
    elif ripetizione != "sì" and ripetizione != "no":
        print("errore nella digitazione, puoi rispondere soltanto con sì o con no")
    else:
        break