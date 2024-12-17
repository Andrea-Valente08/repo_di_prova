scelta=-1
while(scelta!=0):
    print("Benvenuto nella nostra calcolatrice")
    print("Inserisci l'operazione che vuoi effettuare")
    scelta =int(input("1)Sottrazione\n2)Addizzione\n0)Exit\n"))

    if scelta==1:
        n_1 =int(input("Inserisci il primo numero"))
        n_2 =int(input("Inserisci il secondo numero"))
        print(f"{n_1} - {n_2} = {n_1 - n_2}")
    elif scelta==2:
        pass
    else:
        print("Scelta non corretta!")