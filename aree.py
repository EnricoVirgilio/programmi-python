import math
figure = ["quadrato", "triangolo", "cerchio", "rettangolo"]
def area(figura):  
    if figura == "quadrato":
        lato = int(input("inserisci il lato "))
        print("l'area del quadrato è uguale a", lato**2)
    elif figura == "rettangolo":
        base = int(input("inserisci la base "))
        altezza = int(input("inserisci l'altezza "))
        print("l'area del rettangolo è uguale a", base*altezza)
    elif figura == "triangolo":
        base = int(input("inserisci la base "))
        altezza = int(input("inserisci l'altezza "))
        print("l'area del triangolo è uguale a", base*altezza/2)
    else:
        raggio = int(input("inserisci il raggio "))
        print("l'area del cerchio è uguale a", raggio**2*math.pi)
while True:
    figura = input("inserisci la figura di cui vuoi calcolare l'area tra quadrato, rettangolo, triangolo e cerchio ")
    if figura not in figure:
        print("errore nella digitazione le risposte \
accettabili sono: \n-quadrato \n-rettangolo \n-triangolo \n-cerchio")   
    else:
        break    
area(figura)        