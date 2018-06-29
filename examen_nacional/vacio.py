#flavio toro
#mi amado super input
def s_input(text):
    var = text
    text = input(var).lower()
    while(text == ""):
        text = input("ingrese "+var).lower()
    return text

n_cod = 1
print ("cod_"+str(n_cod))