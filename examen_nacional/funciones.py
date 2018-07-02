#flavio toro
#santo tomas
from vacio import *
sesion = list()
productos = list()
provee = list()

#bases iniciales
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
    proc['nom'] = "JJRC H20"
    proc['cate'] = "drone"
    proc['mar'] = "JJRC"
    proc['mode'] = "H20"
    proc['from'] = "Asia"
    proc['prec'] = 150000
    proc['cant'] = 7
    proc['prov'] = "JianJian"

    productos.append(proc)

    proc = dict()
    n_cod += 1
    proc['cod'] = "cod"+str(n_cod)
    proc['nom'] = "Canon T6"
    proc['cate'] = "camara"
    proc['mar'] = "Canon"
    proc['mode'] = "T6"
    proc['from'] = "America"
    proc['prec'] = 449990
    proc['cant'] = 9
    proc['prov'] = "Falabella"

    productos.append(proc)

def base_inicial_prove():
    prov = dict()
    code = 1
    prov['cod'] = "Prove_"+str(code)
    prov['nom'] = "Fulvio"
    prov['pai'] = "Chile"
    prov['dir'] = "Vivanco #1387"
    prov['tel'] = "+56942200288"
    prov['cor'] = "torentk@live.com"

    provee.append(prov)

    prov = dict()
    code +=1
    prov['cod'] = "Prove_"+str(code)
    prov['nom'] = "Lucas"
    prov['pai'] = "Chile"
    prov['dir'] = "Ventisquero palomo"
    prov['tel'] = "+56962003748"
    prov['cor'] = "lucastoroecheverria@gmail.com"

    provee.append(prov)
#bases iniciales

#menu listo, revisar art attack
def menu_principal():
    print("a.   Registrar Valor Dólar (US en CLP)")
    print("b.   Registrar Proveedor")
    print("c.   Registrar Producto Electrónico")
    print("d.   Listar Proveedores")
    print("e.   Listar Producto Electrónico")
    opc = s_input("opcion: ").lower().strip()
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


#modulo de registro
#listo, revisar detalles en funcionamiento ya
def r_valor():
    print(" ")
    print("     Seccion dolar diario")
    clp = float(s_input("valor del dolar en moneda nacional: "))
    return clp

#revisada y funcionando
def r_prove():
    while(True):
        prov = dict()
        print(" ")
        print("     Registro de proveedores")
        print(" ")

        cod = s_input("codigo: ")
        cod_pro = veri_cod_prodc(cod)
        cod_prove = veri_cod_prove(cod)
        while(cod_prove == True or cod_pro == True):
            print("Ingrese: ")
            cod = s_input("codigo valido: ")
            cod_pro = veri_cod_prove(cod)
            cod_prove = veri_cod_prove(cod)

        prov['cod'] = cod

        nom = s_input("nombre: ")
        prov['nom'] = nom

        pais = s_input("pais: ")
        prov['pai'] = pais

        dire = s_input("direccion: ")
        prov['dir'] = dire

        fono = int(s_input("numero de telefono: +"))
        prov['tel'] = fono

        mail = s_input("correo electronico: ")
        vmail = mail.__contains__("@") == True
        while(vmail == False):
            print("mail invalido ('@')")
            mail = s_input("correo electronico: ")
            vmail = mail.__contains__("@") == True
        prov['cor'] = mail

        provee.append(prov)
        op = s_input("¿Desea registrar otro proveedor? s/n: ")
        if (op.__contains__("n")):
            break


#revisada y correcta funcion
def r_elec():
        while(True):
            p_ele = dict()
            print("")
            print("     registro de producto electronico: ")
            print("")
            cod = s_input("codigo: ")
            cod_pro = veri_cod_prodc(cod)
            cod_prov = veri_cod_prove(cod)
            while(cod_prov == True or cod_pro == True):
                print("ingrese  ")
                cod = s_input("codigo valido: ")
                cod_pro = veri_cod_prodc(cod)
                cod_prov = veri_cod_prove(cod)

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




#modulo de listado
def lis_provee():
    for x in provee:
        print("codigo proveedor:",x['cod'])
        print("nombre:          ",x['nom'])
        print("pais:            ",x['pai'])
        print("direccion:       ",x['dir'])
        print("telefono:        ",x['tel'])
        print("correo:          ",x['cor'])
        print(" ")

#listo
def lis_electro():
    while(True):
        print("i.   Listar por tipo de Electrodomestico")
        print("ii.  Listar todo")
        print("iii. Volver a menu anterior")
        elec = s_input("Elija una opcion: ")
        if (elec.__contains__("i") or elec.__contains__("1")):
            tipo = categoria()

            for tip in productos:
                if(tip['cate'] == tipo):
                    print("----------------------------------")
                    print("            informacion:")
                    print("Codigo:          ",tip['cod'])
                    print("Nombre:          ",tip['nom'])
                    print("Categoria:       ",tip['cate'])
                    print("Marca:           ",tip['mar'])
                    print("Modelo:          ",tip['mode'])
                    print(" ")
                    print("----------------------------------")
                    print("            precios: ")
                    print("local:          $",tip['prec'],"usd")

           #definir funcion
                #print("arancel importacion:    ",tip['aran'])
                #print("costo transporte:       ",tip['cost'])
                #print("",tip['pre_n'])
                #print(tip['iva'])
                #print(tip['pre_f'])
                #print(tip['can'])
          #print("----------------------------------")
        elif(elec.__contains__("ii") or elec.__contains__("2")):

            for tip in productos:
                print("----------------------------------")
                print("            informacion:")
                print("Codigo:          ",tip['cod'])
                print("Nombre:          ",tip['nom'])
                print("Categoria:       ",tip['cate'])
                print("Marca:           ",tip['mar'])
                print("Modelo:          ",tip['mode'])
                print(" ")
                print("----------------------------------")
                print("            precios: ")
                #print("local:          $",tip['pre_l'])
                #print("arancel importacion:    ",tip['aran'])
                #print("costo transporte:       ",tip['cost'])
                #print(""tip['pre_n'])
                #print(tip['iva'])
                #print(tip['pre_f'])
                #print(tip['can'])
                #print("----------------------------------")
        elif(elec.__contains__("iii") or elec.__contains__("3")):
            break
        else:
            print("No es una opcion valida!!")




#verificador
def veri_cod_prove(cod):
    for x in provee:
        cod_pr = x['cod']
        if (cod_pr == cod):
            return True

def veri_cod_prodc(cod):
    for x in productos:
        cod_p = x['cod']
        if (cod_p == cod):
            return True


#categorias de los productos
def categoria():
    print("   categorias")
    print("a) computador")
    print("b) camara fotografica")
    print("c) drone")
    op = s_input("eliga el tipo: ")
    if(op.__contains__("a") or op.__contains__("computador") or op.__contains__("1")):
        return ("computador")
    if(op.__contains__("b") or op.__contains__("camara") or op.__contains__("2")):
        return ("camara fotografica")
    if (op.__contains__("c") or op.__contains__("drone") or op.__contains__("3")):
        return ("drone")

#procedencias, revisado y confirmado
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

