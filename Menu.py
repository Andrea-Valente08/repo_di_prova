import calcolatrice as clc

while True:
    print("Benvenuto nella nostra calcolatrice")
    print("Inserisci l'operazione che vuoi effettuare")
    scelta =int(input("1)Sottrazione\n2)Addizzione\n0)Exit\n"))
    if scelta==0:
        print("Grazie per aver usato la nostra calcolatrice, a presto!")
        break
    if scelta==1:
        clc.Sottrazzione()
    elif scelta==2:
        clc.Somma()
    else:
        print("Scelta non corretta!")
