#flavio toro
#santo tomas
from vacio import *
sesion = list()
productos = list()
provee = list()

def base_inicial_produ():
    proc = dict()
    n_cod = 1
    proc['cod'] = "cod_"+str(n_cod)
    proc['nom'] = "Lenovo Z470"
    proc['cate'] = "computador"
    proc['mar'] = "Lenovo"
    proc['mode'] = "Z470"
    proc['from'] = "Asia"
    proc['prec'] = 150
    proc['cant'] = 4
    proc['prov'] = "Lenovo S.A"

    productos.append(proc)

    proc = dict()
    n_cod += 1
    proc['cod'] = "cod_"+str(n_cod)







#menu listo, revisar art attack
def menu_principal():
    print("a.   Registrar Valor Dólar (US en CLP)")
    print("b.   Registrar Proveedor")
    print("c.   Registrar Producto Electrónico")
    print("d.   Listar Proveedores")
    print("e.   Listar Producto Electrónico")
    opc = s_input("opcion: ")
    return opc
#usuarios listo... analizar opcion de ingresar uno nuevo
def usuarios():
    usu_cla = dict()
    usu_cla['usuario'] = "admin"
    usu_cla['clave'] = "admin"
    sesion.append(usu_cla)
#-------------------------------------------
#mejorar el registro de inicio de sesion
def nombre():
    usuarios()
    for x in sesion:
        usu = x['usuario']
        return usu

def clave():
    usuarios()
    for y in sesion:
        clav = y['clave']
        return clav

def inicio(): #mejorar pero sirve de beta1
    usu = nombre()
    clav = clave()
    print("     Bienvenido a bodega")
    print("     Ingrese sus credenciales:")
    nom = input("Usuario: ").lower().strip()
    while(nom != usu):
        nom = input("Ingrese un usuario valido!: ").lower().strip()
    password = input("Password: ").lower().strip()
    while(password != clav):
        password = input("Contraseña incorrecta: ").lower().strip()
    return True
#---------------------------------------------

#listo, revisar detalles en funcionamiento ya
def r_valor():
    print(" ")
    print("     Seccion dolar diario")
    clp = float(input("valor del dolar en moneda nacional: "))
    return clp

#revisada y funcionando
def r_prove():
    while(True):
        prov = dict()
        print(" ")
        print("     Registro de proveedores")
        print(" ")

        cod = s_input("codigo: ")
        prov['cod'] = cod

        nom = s_input("nombre: ")
        prov['nom'] = nom

        pais = s_input("pais: ")
        prov['pai'] = pais

        dire = s_input("direccion: ")
        prov['dir'] = dire

        fono = int(s_input("numero de telefono: +"))
        prov['tel'] = fono

        mail = s_input("correo electronico")
        mail = mail.__contains__("@") == True
        while(mail == False):
            print("mail invalido ('@')")
            mail = s_input("correo electronico")
            mail = mail.__contains__("@") == True
        prov['cor'] = mail

        provee.append(prov)
        op = input("¿Desea registrar otro proveedor? s/n").lower().strip()
        if (op.__contains__("n")):
            break
        while(op == ""):
            op = input("ingrese una opcion valida")

#revisada y correcta funcion
def r_elec():
        while(True):
            p_ele = dict()
            print("")
            print("     registro de producto electronico: ")
            print("")
            cod = input("codigo: ").lower().strip()
            cod_p = veri_cod()
            while(cod == "" or cod == cod_p):
                print("ingrese  ")
                cod = input("codigo valido: ")
            p_ele['cod'] = cod

            nom = s_input("nombre: ").lower().strip()
            p_ele['nom'] = nom

            cate = categoria()
            p_ele['cate'] = cate

            marc = s_input("marca: ").lower().strip()
            p_ele['mar'] = marc

            mode = s_input("modelo:")
            p_ele['mode'] = mode

            proce = procedencia()
            p_ele['from'] = proce

            us = float(s_input("precio en usd:"))
            p_ele['prec'] = us

            cant = int(s_input("cantidad: "))
            p_ele['cant'] = cant

            prove = s_input("proveedor: ")
            p_ele['prov'] = prove

            productos.append(p_ele)

            opc = s_input("desea registrar otro producto? s/n: ")
            if (opc.__contains__("n") or opc.__contains__("no")):
                break

def lis_provee():
    print("listar proveedores")

#listo el esquema
def lis_electro():
    while(True):
        print("i.   Listar por tipo de Electrodomestico")
        print("ii.  Listar todo")
        print("iii. Volver a menu anterior")
        elec = s_input("Elija una opcion: ").lower().strip()
        if (elec.__contains__("i") or elec.__contains__("1")):
            print("a) Computador")
            print("b) Camara Fotográfica")
            print("c) Drone")
            tipo = s_input("Categoria a buscar:").lower().strip()
            #if(tipo.__contains__(tipo)):
            #for tip in list_electr:
                #print("----------------------------------")
                #print("            informacion:")
                #print("Codigo:          "tip['cod'])
                #print("Nombre:          "tip['nom'])
                #print("Categoria:       "tip['cate'])
                #print("Marca:           "tip['mar'])
                #print("Modelo:          "tip['mod'])
                #print(" ")
                #print("----------------------------------")
                #print("            precios: ")
                #print("local:          $"tip['pre_l'])
           #definir funcion
                #print("arancel importacion:    "tip['aran'])
                #print("costo transporte:       "tip['cost'])
                #print(""tip['pre_n'])
                #print(tip['iva'])
                #print(tip['pre_f'])
                #print(tip['can'])
          #print("----------------------------------")
        elif(elec.__contains__("ii") or elec.__contains__("2")):
            pass
            #if(tipo.__contains__(tipo)):
            #for tip in list_electr:
            #print("----------------------------------")
            #print("            informacion:")
            #print("Codigo:          "tip['cod'])
            #print("Nombre:          "tip['nom'])
            #print("Categoria:       "tip['cate'])
            #print("Marca:           "tip['mar'])
            #print("Modelo:          "tip['mod'])
            #print(" ")
            #print("----------------------------------")
            #print("            precios: ")
            #print("local:          $"tip['pre_l'])
            #print("arancel importacion:    "tip['aran'])
            #print("costo transporte:       "tip['cost'])
            #print(""tip['pre_n'])
            #print(tip['iva'])
            #print(tip['pre_f'])
            #print(tip['can'])
            #print("----------------------------------")
        elif(elec.__contains__("iii") or elec.__contains__("3")):
            break
        else:
            print("No es una opcion valida!!")

def test():
    clp = r_valor()
    test = float(input("ingrese el dinero a convertir: "))

    us = test / clp
    us = round(us,2)
    print(us)

def veri_cod():
    for x in provee:
        cod_p = x['cod']
        return cod_p

def categoria():
    print("     categorias")
    print("a) computador")
    print("b) camara fotografica")
    print("c) drone")
    op = s_input("eliga el tipo: ").lower().strip()
    if(op.__contains__("a") or op.__contains__("computador") or op.__contains__("1")):
        return ("computador")
    if(op.__contains__("b") or op.__contains__("camara") or op.__contains__("2")):
        return ("camara fotografica")
    if (op.__contains__("c") or op.__contains__("drone") or op.__contains__("3")):
        return ("drone")

def procedencia():
    print("     procedencia")
    print("a) America")
    print("b) Asia")
    print("c) Europa")
    op = s_input("eliga el tipo: ").lower().strip()
    if (op.__contains__("a") or op.__contains__("america") or op.__contains__("1")):
        return ("America")
    if (op.__contains__("b") or op.__contains__("asia") or op.__contains__("2")):
        return ("Asia")
    if (op.__contains__("c") or op.__contains__("europa") or op.__contains__("3")):
        return ("Europa")

