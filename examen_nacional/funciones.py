# flavio toro
# santo tomas
from vacio import *
sesion = list()
productos = list()
provee = list()
usd_clp = list()
#bases iniciales
def base_inicial_produ():
    proc = dict()
    n_cod = 1
    proc['cod'] = "cod_"+str(n_cod)
    proc['nom'] = "Lenovo Z470"
    proc['cate'] = "computador"
    proc['mar'] = "Lenovo"
    proc['mode'] = "Z470"
    proc['from'] = "Europa"
    proc['prec'] = 1500
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
    proc['prec'] = 1650
    proc['cant'] = 7
    proc['prov'] = "JianJian"

    productos.append(proc)

    proc = dict()
    n_cod += 1
    proc['cod'] = "cod_"+str(n_cod)
    proc['nom'] = "Canon T6"
    proc['cate'] = "camara"
    proc['mar'] = "Canon"
    proc['mode'] = "T6"
    proc['from'] = "America"
    proc['prec'] = 640
    proc['cant'] = 9
    proc['prov'] = "Falabella"

    productos.append(proc)

def base_inicial_prove():
    prov = dict()
    code = 1
    prov['cod'] = "prove_"+str(code)
    prov['nom'] = "Fulvio"
    prov['pai'] = "Chile"
    prov['dir'] = "Vivanco #1387"
    prov['tel'] = "+56942200288"
    prov['cor'] = "torentk@live.com"

    provee.append(prov)

    prov = dict()
    code +=1
    prov['cod'] = "prove_"+str(code)
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
    usd_clp.append(clp)


def arancel(tipo):
    var = tipo
    if(var == "computador"):
        ara = 0.03
        return ara
    if(var == "camara"):
        ara = 0.05
        return ara
    if(var == "drone"):
        ara = 0.04
        return ara

def cost_trans(desde):
    var = desde
    if (var == "Asia"):
        ara = 0.07
        return ara
    if (var == "America"):
        ara = 0.1
        return ara
    if (var == "Europa"):
        ara = 0.14
        return ara

#revisada y funcionando
def r_prove():
    while(True):
        prov = dict()
        print(" ")
        print("     Registro de proveedores")
        print(" ")

        while(True):
            cod = s_input("codigo: ")
            cod_pro = veri_cod_prodc(cod)
            cod_prove = veri_cod_prove(cod)
            if(cod_prove != True and cod_pro != True):
                break
            else:
                print("ingrese ")
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
        while (op != "n" and op != "s"):
            print("ingrese una opcion valida: ")
            op = s_input("desea registrar otro proveedor? s/n: ")
        if (op == "n"):
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
            while(opc != "n" and opc != "s" ):
                print("ingrese una opcion valida: ")
                opc = s_input("desea registrar otro producto? s/n: ")
            if (opc == "n"):
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
        if (elec == "i" or elec == "1"):
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
                    usd_p = tip['prec']
                    for x in usd_clp:
                        pesos = x
                    peso = pesos
                    valor_naci = usd_p * peso
                    valor_naci = round(valor_naci)
                    print("precio local:                  $",valor_naci)
                    # arancel
                    tipo = tip['cate']
                    ara = arancel(tipo)
                    ara_tipo = valor_naci * ara
                    ara_tipo = round(ara_tipo)
                    print("arancel importacion:           $",ara_tipo)

                    #costo transporte
                    desde = tip['from']
                    impo = cost_trans(desde)
                    costo_t = impo * valor_naci
                    costo_t = round(costo_t)
                    print("costo transporte:              $",costo_t)
                    # valor neto
                    neto = valor_naci + ara_tipo + costo_t
                    print("valor neto:                    $",neto)
                    #~iva
                    iva = neto * 0.19
                    iva = round(iva)
                    print("IVA:                           $",iva)
                    #precio final
                    pre_final = neto + iva
                    print("precio final unitario:         $",pre_final)
                    print("cantidad:                       ",tip['cant'])
                    canti = tip['cant']
                    pre_final_final = canti * pre_final
                    print("precio total:                  $",pre_final_final)
                    print("-----------------------------------------")

        elif(elec == "ii" or elec == "2"):

            for tip in productos:
                print("-----------------------------------------")
                print("            informacion:")
                print("Codigo:          ",tip['cod'])
                print("Nombre:          ",tip['nom'])
                print("Categoria:       ",tip['cate'])
                print("Marca:           ",tip['mar'])
                print("Modelo:          ",tip['mode'])
                print(" ")
                print("-----------------------------------------")
                print("            precios: ")
                usd_p = tip['prec']
                for x in usd_clp:
                    pesos = x

                peso = pesos
                valor_naci = usd_p * peso
                valor_naci = round(valor_naci)
                print("precio local:                  $", valor_naci)
                # arancel
                tipo = tip['cate']
                ara = arancel(tipo)
                ara_tipo = valor_naci * ara
                ara_tipo = round(ara_tipo)
                print("arancel importacion:           $", ara_tipo)

                # costo transporte
                desde = tip['from']
                impo = cost_trans(desde)
                costo_t = impo * valor_naci
                costo_t = round(costo_t)
                print("costo transporte:              $", costo_t)
                # valor neto
                neto = valor_naci + ara_tipo + costo_t
                print("valor neto:                    $", neto)
                # ~iva
                iva = neto * 0.19
                iva = round(iva)
                print("IVA:                           $", iva)
                # precio final
                pre_final = neto + iva
                print("precio final unitario:         $", pre_final)
                print("cantidad:                       ", tip['cant'])
                canti = tip['cant']
                pre_final_final = canti * pre_final
                print("precio total:                  $", pre_final_final)
                print("-----------------------------------------")
        elif(elec.__contains__("iii") or elec.__contains__("3")):
            break
        else:
            print("No es una opcion valida!!")




#verificador
def veri_cod_prove(cod):
    codi = cod
    for x in provee:
        cod_pr = x['cod']
        if (cod_pr == codi):
            return True

def veri_cod_prodc(cod):
    codi = cod
    for x in productos:
        cod_p = x['cod']
        if (cod_p == codi):
            return True


#categorias de los productos
def categoria():
    print("   categorias")
    print("a) computador")
    print("b) camara fotografica")
    print("c) drone")
    while (True):
        op = s_input("eliga el tipo: ")
        if(op == "a" or op.__contains__("computador") or op.__contains__("1")):
          return ("computador")
        if(op == "b" or op.__contains__("camara") or op.__contains__("2")):
          return ("camara")
        if (op == "c" or op.__contains__("drone") or op.__contains__("3")):
          return ("drone")

#procedencias, revisado y confirmado
def procedencia():
    print("     procedencia")
    print("a) America")
    print("b) Asia")
    print("c) Europa")
    while(True):
        op = s_input("eliga alternativa: ").lower().strip()
        if (op == "a" or op.__contains__("america") or op.__contains__("1")):
            return ("America")
        if (op == "b" or op.__contains__("asia") or op.__contains__("2")):
            return ("Asia")
        if (op == "c" or op.__contains__("europa") or op.__contains__("3")):
            return ("Europa")

