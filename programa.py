import random
print("Piedra = 1")
print("Papel = 2")
print("Tijera = 3")

P = int(input("Piedra, papel o tijeras: "))
M = random.randint(1,3)


if (M==1):
    if (P==1):
        rta= "Empate"
    elif (P==2):
        rta= "Pierdes"
    elif (P==3):
        rta="Ganaste"
elif (M==2):
    if(P==1):
        rta="Pierdes"
    elif(P==2):
        rta="empate"
    elif(P==3):
        rta="Ganaste"
elif(M==3):
    if(P==1):
        rta= "Ganaste"
    elif (P==2):
        rta="Pierdes"
    elif (P==3):
        rta="Empate"

if P>3:
    print("no flaco imposible sacarse una basuca")
else: 
    print(rta)