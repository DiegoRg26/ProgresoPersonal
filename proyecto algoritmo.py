#Kevin José Guerrero Hincapié
#Marlon Lapeira Arias
#Diego Alejandro Román Guzmán

from os import system
system("cls")

n = int(input("Ingrese la cantidad de estudiantes a procesar: "))
suma = 0
i = 1
#Aprobar
apro = 0
rpro = 0
#Promedio curso
aprg = 0
j = 0
#mayor nota
mnota = 0
mnnota = ""
mcnota = ""
#falta de nota
fnota = 0
fnnota = ""


while i <= n:
    nom = input("\nIngrese el nombre del estudiante: "+ str(i)+ ": ")
    cod = int(input("Ingrese el Codigo del estudiante: "))
    while cod < 0:
        print("Codigo no valido")
        cod = int(input("Ingrese el Codigo del estudiante: "))
    nota1 = float(input("\nIngrese la nota 1: "))
    while nota1 < 0 or nota1 >5:
        print("Nota no valida.")
        nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    while nota2 < 0.5 or nota2 >5:
        print("Nota no valida.")
        nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    while nota3 < 0.5 or nota3 >5:
        print("Nota no valida.")
        nota3 = float(input("Ingrese la nota 3: "))
    nota4 = float(input("Ingrese la nota 4: "))
    while nota4 < 0.5 or nota4 >5:
        print("Nota no valida.")
        nota4 = float(input("Ingrese la nota 4: "))

    if nota1 == 0:
        fnota = fnota + 1

    if nota1 == 0:
        
        nota1 = 0.5
        n2 = nota2 * 0.4
        n3 = nota3 * 0.2
        n4 = nota4 * 0.4

        prom = (nota1 + n2 + n3 + n4)
        if prom > 5:
            prom = 5
        cod = str(cod)
        nota1 = str(nota1)
        nota2 = str(nota2)
        nota3 = str(nota3)
        nota4 = str(nota4)
        fnnota = "[" + nom + " ID:" + cod + " Notas:" + nota1 + " - " + nota2 + " - " + nota3 + " - " + nota4 + "]" + " - " + fnnota

    else:
        nota1 = nota1 * 0.2
        nota2 = nota2 * 0.4
        nota3 = nota3 * 0.2
        nota4 = nota4 * 0.2
        prom = (nota1 + nota2 + nota3 + nota4)

    if prom >= 3:
        apro = apro + 1
    else:
        rpro = rpro + 1

    aprg = aprg	+ prom

    if prom > mnota:
        mnota = prom
        mnnota = nom
        mcnota = cod

    i = i + 1


j = (prom / n) * 4

print("\n\t-[INFORMACION]-")

if j < 3:
    print("\El promedio del curso fue DEFICIENTE")
elif j >= 3 and j < 4:
    print("\nEl promedio del curso fue ACEPTABLE")
elif j >= 4:
    print("\nEl promedio del curso fue EXELENTE")

print("\n\t-[CANTIDAD DE APROBADOS/DESAPROBADOS]-")
print("La cantidad de estudiantes que aprobaron fue de:", apro)
print("La cantidad de estudiantes que no aprobaron fue de:", rpro)
print("\n\t-[MAYOR NOTA]-")
print("la mayor nota fue de", mnnota, "y esta fue de", mnota)
print("\n\t-[NOTA INCUMPLIDA]-")
print("El numero de estudiantes que no presentaron la primera nota fue de", fnota)
print("Los estudiantes que no presentaron la primera nota fueron:", fnnota)
print()