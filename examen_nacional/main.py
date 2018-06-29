# flavio toro"
#santo tomas rancagua
from funciones import *
apro = inicio()
while (apro == True):
    print(" ")
    print("     Menu Principal")
    opcion = menu_principal().lower().strip()
    print(" ")
    if(opcion.__contains__("a")):
        r_valor()
    elif(opcion.__contains__("b")):
        r_prove()
    elif(opcion.__contains__("c")):
        r_elec()
    elif(opcion.__contains__("d")):
        lis_provee()
    elif(opcion.__contains__("e")):
        lis_electro()
    else:
        print("ingrese una opcion valida!!: ")


