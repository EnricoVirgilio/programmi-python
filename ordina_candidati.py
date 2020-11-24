print("benvenuto nel programma che ordina in ordine alfabetico i nomi dei candidati \
    e in ordine decrescente il numero di voti di ciascun candidato")
candidati = int(input("inserisci il numero dei candidati "))
votazioni = [] #all'interno di questa lista ci saranno i voti dei partecipanti con il corrispettivo nome del partecipante tra due parentesi
candidati_nomi = [] #all'interno di questa lista ci saranno i nomi dei partecipanti con il corrispettivo voto tra due parentesi
voto_solo_numeri = [] #all'interno di questo solo i voti
candidati_solo_nome = [] #all'interno di questa lista solo i nomi

for voti in range(1, candidati+1):
    numero_voti = "inserisci voti candidato numero" + str(voti) + " "
    nome_candidato = "inserisci nome candidato numero" + str(voti) + " "
    voto = int(input(numero_voti))
    candidato = str(input(nome_candidato))
    candidati_solo_nome.append(candidato)
    voto_solo_numeri.append(voto)
    voto_solo_numeri.sort(reverse = True, key = int) #metto in ordine i voti
    candidati_solo_nome.sort() #metto in ordine alfabetico i nomi
    candidato_con_voto = str(candidato) + "(" + str(voto) + ")"
    candidati_nomi.append(candidato_con_voto)
    
while True:
    #inserisco all'interno della lista votazioni il primo elemento della lista voto_con_candidato con il nome del partecipante tra le parentesi
    voto_con_candidato = str(voto_solo_numeri.pop(0)) + "(" + str(candidati_solo_nome.pop(0)) + ")" 
    votazioni.append(voto_con_candidato)
    if voto_solo_numeri == []:
        break

print("ordine alfabetico candidati con corrispetivo voto")
candidati_nomi.sort()
print(candidati_nomi)
print("ordine decrescente voti con il corrispettivo nome del candidato")
print(votazioni)