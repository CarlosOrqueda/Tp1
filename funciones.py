
#funcion pide opciones submenu
def opciones_submenu():
    opcion=0
    while opcion==0: 
        try:
            print("1 - Continuar")
            print("2 - Ir al menú")
            print("3 - Ir al menú principal")
            opcion=int(input("¿Quiere continuar operando?: "))
        except ValueError:
            print("Ingrese una opcion valida, solo un numero")
    return opcion

#se usa esta

def palabraMasLargaCantidadDeLetras():

    frase=input("Ingrese una cadena de texto: ")

    cantidadDeLetras = 0
    listaLarga = []
    reemplazar = frase.maketrans(",;.", "   ")
    listaDePalabras = frase.translate(reemplazar).lower().split()
    palabraMasLarga = listaDePalabras[0]
    listaLarga.append(palabraMasLarga)
    for palabra in listaDePalabras:
        if len(palabraMasLarga) == len(palabra) and palabraMasLarga != palabra:
            listaLarga.append(palabra)
        elif len(palabraMasLarga) < len(palabra):
            palabraMasLarga = palabra
            del listaLarga[:]
            listaLarga.append(palabraMasLarga)
    for cantidad in listaLarga:
        if cantidadDeLetras < len(cantidad):
            cantidadDeLetras = len(cantidad)
    
    mensaje="Las palabras largas son: "
    palabras_largas_mensaje= mensaje + str(listaLarga)
    
    return  palabras_largas_mensaje #,listaLarga, cantidadDeLetras





#La acabo de ver, parece andar bien
def string_corto():
    
    cadena=input("Ingrese una cadena de texto: ")
    outside="  "
    inside=".,;"
    trans=cadena.maketrans(".,;!","    ")
    cadena=cadena.translate(trans)
    lista_cadena=cadena.split()
    palabra_corta= lista_cadena[0]
    lista_auxiliar=[]
    #lista_auxiliar.append(palabra_corta)
    for i in lista_cadena:
       if len(palabra_corta)>len(i):
          del lista_auxiliar[::]
          palabra_corta=i
          lista_auxiliar.append(palabra_corta)
       elif len (palabra_corta)==len(i):
          #lista_auxiliar.append(palabra_corta)
          lista_auxiliar.append(i)
          palabra_corta=i
    
    #print ("Las palabras cortas son: ",lista_auxiliar)
    palabras_cortas=lista_auxiliar
    mensaje="Las palabras cortas son: "
    palabras_cortas_mensaje= mensaje + str(palabras_cortas)
    #print (palabras_cortas_mensaje)
    return palabras_cortas_mensaje #palabras_cortas


#La acabo hacer y ver, parece andar bien

def contar_cadena():
    cadena=input("Ingrese una cadena de texto: ")
    trans=cadena.maketrans(".,;!","    ")
    cadena=cadena.translate(trans)
    
    lista_cadena=cadena.split()
  
    cantidad_palabras=len(lista_cadena)
    
    #print("Hay",cantidad_palabras, "palabras en la cadena de texto.")
    mensaje="La cantidad de palabras en el texto es: "
    cantidad_mensaje=mensaje + str(cantidad_palabras)
    
    return cantidad_mensaje #cantidad_palabras


##Se usa esta
def division(valor1, valor2):
    valorA=int(valor1)
    valorB=int(valor2)

    
    cociente = 0
    contadorDeDecimales = 0
    porMenosUno = False
    mensaje = ""
    if valorA < 0 or valorB < 0:
        porMenosUno = True
    valorA = abs(valorA)
    valorB = abs(valorB)
    if valorB != 0:
        if valorA == 0:
            while valorA >= valorB:
                valorA -= valorB
                cociente += 1
            resto = valorA
        elif valorA <= valorB and valorB % valorA == 0:
            while valorB >= valorA:
                valorB += -valorA
                cociente += 1
            resto = valorB
            if porMenosUno == True:
                cociente = -cociente
            cociente = 1 / cociente
        else:
            while valorA <= valorB:
                valorA = valorA * 10
                contadorDeDecimales += 1
            while valorA >= valorB:
                valorA -= valorB
                cociente += 1
            resto = valorA
            if porMenosUno == True:
                cociente = -cociente
            cociente = cociente / (10 ** contadorDeDecimales)
    else:
        mensaje = "No se puede dividir por 0"
        resto = ""
        cociente = ""
        return mensaje
   
    print("La division es: ", cociente)
    print("El resto es: ", resto)
    return cociente, resto 

def multiplicacion(valor1, valor2):

    valorA=int(valor1)
    valorB=int(valor2)
    suma = 0
    if valorA < 0 and valorB < 0 or valorA > 0 and valorB > 0:
        if valorA < 0 and valorB < 0:
            valorA = -valorA
            valorB = -valorB
        if valorA <= valorB:
            for i in range(0, valorA):
                suma += valorB
        elif valorA > valorB:
            for i in range(0, valorB):
                suma += valorA
    elif valorA < 0:
        if abs(valorA) < valorB:
            for i in range(valorA, 0):
                suma += valorB
            suma = -suma
        else:
            for i in range(0, valorB):
                suma += valorA
    else:
        if abs(valorB) < valorA:
            for i in range(valorB, 0):
                suma += valorA
            suma = -suma
        else:
            for i in range(0, valorA):
                suma += valorB
    print("La multiplicacion es", suma)
    return suma


###################


#La acabo de ver, parece andar bien
def string_largo():
    
    cadena=input("Ingrese una cadena de texto: ")
    outside="  "
    inside=".,;"
    trans=cadena.maketrans(".,;","   ")
    cadena=cadena.translate(trans)
    lista_cadena=cadena.split()
    palabra_larga= lista_cadena[0]
    lista_auxiliar=[]
    #lista_auxiliar.append(palabra_corta)
    for i in lista_cadena:
       if len(palabra_larga)<len(i):
          del lista_auxiliar[::]
          palabra_larga=i
          lista_auxiliar.append(palabra_larga)
       elif len (palabra_larga)==len(i):
          #lista_auxiliar.append(palabra_corta)
          lista_auxiliar.append(i)
          palabra_larga=i
    
    print ("Las palabras largas son: ",lista_auxiliar)
    palabras_largas=lista_auxiliar
    return palabras_largas




#se usa esta
def potencias(valor1, valor2):

    valorA=int(valor1)
    valorB=int(valor2)
    multp = 1
    if valorA != 0 and valorB != 0:
        if valorA > 0 and valorB > 0:
            for i in range(0, valorB):
                multp = multp * valorA
        elif valorB < 0:
            for i in range(valorB, 0):
                multp = multp * valorA
            multp = 1 / multp
        elif valorA < 0:
            for i in range(0, valorB):
                multp = multp * valorA
    else:
        multp = 0
    print("La potencia es", multp)   
    return multp
#potencias(4,2)


#No revise mucho
#La dejo de usar
'''
def potencias(valor1,valor2 ):
    c=int(valor1)
    d=int(valor2)
    multi = 1
    e = 0
    potencia = 0
    if (d >= 0):
        for i in range(0, d):
            multi = multi * c
        potencia = multi

    elif (d < 0):
        for i in range(d, 0):
            multi = multi * c
        potencia = 1 / multi
    print("La potencia es", potencia)
    return potencia
'''



    
#Solo con enteros, para cadenas habria que mod o hacer otra
#return un valor generico vacio y otro con cadena. No probe pero con un if se podria solucionar.
def solicitud():
    valor_1=0
    valor_2=0
    while valor_1==0 and valor_2==0:
        try:
            valor_1=int(input("Ingrese un Parametro: "))
            valor_2=int(input("Ingrese un Parametro: "))
        except ValueError:
            print("Ingrese un valor valido, solo un numero")
    return valor_1,valor_2

def imprimir(parametro_1="", parametro_2=""):

    print(parametro_1, parametro_2)

