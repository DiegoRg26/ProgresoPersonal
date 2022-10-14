#Diego Alejandro Román Guzmán

from os import system
system("cls")

sumac = 0
sumao = 0
sumae = 0
tcarta = 0
toficio = 0
textra = 0
amy = 0
m = 0
f = 0
ff = 0

print("Ingrese el dia de la semana teniendo en cuenta el siguiente formato")
print("Lunes = 1")
print("Martes = 2")
print("Miercoles = 3")
print("Jueves = 4")
print("Viernes = 5")
print("Sabado = 6")
print("Domingo = 7")
dia = int(input("\nIngrese el dia de la semana: "))

cant = int(input("Ingrese la cantidad de clientes a procesar: "))

for i in range (cant):
    cod = int(input("Ingrese la cedula del cliente " + str (i+1) + " : "))
    while cod <= 0:
        print("Dato NO valido")
        cod = int(input("Ingrese la cedula del cliente " + str (i+1) + " : "))

    con = input("Ingrese nombre del cliente " + str (i+1) + " : ")

    cos = int(input("Ingrese el sexo del cliente " + str (i+1) + " .Coloque 1 si es Masculino .Coloque 2 si es Femenino : "))
    while cos < 1 or cos > 2:
        print("Dato NO valido")
    cos = int(input("Ingrese el sexo del cliente " + str (i+1) + " .Coloque 1 si es Masculino .Coloque 2 si es Femenino : "))
    if cos == 1:
        m = m + 1
    else:
        f = f + 1

    coe = int(input("Ingrese la edad del cliente " + str (i+1) + " : "))
    while coe <= 0 or coe > 120:
        print("Dato NO valido")
        coe = int(input("Ingrese la edad del cliente " + str (i+1) + " : "))

    if coe > 25 and coe < 35 and cos == 2:
        ff = ff + 1

    if coe > 60:
        amy = amy + 1
    

copias={"carta":50, "oficio":100, "Extra oficio":150}

for i in range (cant):
    print()
    print("informacion cliente " + str (i+1) + " :")
    carta = int(input("\ningrese cuantas copias carta desea comprar: "))
    oficio = int(input("ingrese cuantas copias oficio desea comprar: "))
    extra = int(input("ingrese cuantas copias extra oficio desea comprar: "))

    tcarta = tcarta + carta
    toficio = toficio + oficio
    textra = textra + extra

    if dia == 1:
        ccarta = (carta * 50)*0,10
        coficio = (oficio * 100)*0,10
        cextra = (extra * 150)*0,10
    else:
        ccarta = carta * 50
        coficio = oficio * 100
        cextra = extra * 150        

    sumac = sumac + ccarta
    sumao = sumao + coficio
    sumae = sumae + cextra

tftc = sumac + sumao + sumae


#------------
#Impresiones
#------------
for clave, valor in copias.items():
    print(clave, valor)

print("\n\t[-CANTIDAD DE FOTOCOPIAS TOTALES-]")
print("\nTipo carta:" ,tcarta)
print("Tipo oficio:" ,toficio)
print("Tipo Extra oficio:" ,textra)

print("\n\t[-Total vendido-]")
if dia == 1:
    print ("Se le aplica un descuento a las fotocopias del 10% puesto que el dia actual es Lunes")
print()
copias["carta:"]= sumac
copias["oficio:"]= sumao
copias["Extra oficio:"]= sumae
for c in copias:
    print(c,copias[c])

print("\n\t[-Cantidad de fotocopias por sexo-]")
if m > f:
    print("\n La mayor cantidad de fotocopias fue por parte de los hombres con un total" ,m ,"compradores")
else:
    print("\n La mayor cantidad de fotocopias fue por parte de las mujeres con un total" ,f ,"compradores")
print("Cantidad de fotocopias de mujeres entre 25 y 35:" ,ff)
print("Total vendido a personas del genero masculino:" ,m)

print("\n\t[-Total vendido en general-]")
print("\nTotal vendido" ,tftc)

print("\n\t[Cantidad de dultos mayores de 60 años]")
print("\nCantidad:" ,amy)

if dia == 1:
    fdia = tcarta + toficio + textra
    print("\n\t[-Total de Fotocopias impresas el lunes-]")
    print("\nEl total de fotocopias fueron de:" ,fdia)
    print("Estas fueron:")
    print("Carta" ,tcarta)
    print("Oficio" ,toficio)
    print("Extra oficio" ,textra)