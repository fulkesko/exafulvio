# flavio toro"
#santo tomas rancagua
from funciones import *
apro = inicio()
base_inicial_produ()
base_inicial_prove()

while (apro == True):
    print(" ")
    print("     Menu Principal")
    opcion = menu_principal().lower().strip()
    print(" ")
    if(opcion == "a"):
        r_valor()
    elif(opcion == "b"):
        r_prove()
    elif(opcion == "c"):
        r_elec()
    elif(opcion == "d"):
        lis_provee()
    elif(opcion == "e"):
        len = usd_clp.__len__()
        if(len == 0):
            print("aun no define usd en peso nacional")
        if(len != 0):
            lis_electro()
    else:
        print("ingrese una opcion valida!!: ")
