def Somma():
    n_1 =int(input("Inserisci il primo numero"))
    n_2 =int(input("Inserisci il secondo numero"))
    print(f"{n_1} + {n_2} = {n_1 + n_2}")
def Sottrazzione():
    n_1 =int(input("Inserisci il primo numero"))
    n_2 =int(input("Inserisci il secondo numero"))
    print(f"{n_1} - {n_2} = {n_1 - n_2}")
while(true):
    print("Benvenuto nella nostra calcolatrice")
    print("Inserisci l'operazione che vuoi effettuare")
    scelta =int(input("1)Sottrazione\n2)Addizzione\n0)Exit\n"))
    if scelta==0:
        print("Grazie per aver usato la nostra calcolatrice, a presto!")
        break
    if scelta==1:
        Sottrazione()
    elif scelta==2:
        Somma()
    else:
        print("Scelta non corretta!")
