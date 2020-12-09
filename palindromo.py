print("benvenuto nel programma che ti dice se una parola è palindroma oppure no")
parola = input("inserisci una parola ")
parola_girata = parola[::-1]
if parola_girata == parola:
    print("la parola è palindroma")
else:
    print("la parola non è palindroma")