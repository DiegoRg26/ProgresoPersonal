from os import system
system("cls")

print("[-- Promedio de notas --]")

print("\nPorfavor leer atentamente y rellenar de manera correcta los siguientes campos")
nom = input("\nIngrese el nombre del estudiante: ")
nom2 = input("Ingrese el numero de documento del estudiante: ")
print("\nA continuacion rellenar los campos de notas.")
print("\n-----------------")
print("[Calculo]")
print("-----------------")
ncalex = float(input("\tIngrese la nota de su examen: "))
ncalt1 = float(input("\tIngrese la nota de la primera tarea: "))
ncalt2 = float(input("\tIngrese la nota de la segunda tarea: "))
ncalt3 = float(input("\tIngrese la nota de la tercera tarea: "))
ncaltf = ((ncalt1 + ncalt2 + ncalt3)/3) * 0.1
ncalexf = ncalex * 0.9
ncalf = ncaltf + ncalexf
print("-----------------")
print("[Fisica]")
print("-----------------")
nfisex = float(input("\tIngrese la nota de su examen: "))
nfist1 = float(input("\tIngrese la nota de la primera tarea: "))
nfist2 = float(input("\tIngrese la nota de la segunda tarea: "))
nfistf = ((nfist1 + nfist2)/2) * 0.2
nfisexf = nfisex * 0.8
nfisf = nfistf + nfisexf
print("-----------------")
print("[Quimica]")
print("-----------------")
nquimex = float(input("\tIngrese la nota de su examen: "))
nquimt1 = float(input("\tIngrese la nota de la primera tarea: "))
nquimt2 = float(input("\tIngrese la nota de la segunda tarea: "))
nquimt3 = float(input("\tIngrese la nota de la tercera tarea: "))
nquimtf = ((nquimt1 + nquimt2 + nquimt3)/3) * 0.15
nquimexf = nquimex * 0.85
nquimf = nquimtf + nquimexf
print("-----------------")
print("[Algoritmos]")
print("-----------------")
nalgex = float(input("\tIngrese la nota de su examen: "))
nalgt1 = float(input("\tIngrese la nota de la primera tarea: "))
nalgt2 = float(input("\tIngrese la nota de la segunda tarea: "))
nalgtf = ((nalgt1 + nalgt2)/2) * 0.4
nalgexf = nalgex * 0.6
nalgf = nalgtf + nalgexf
#-=-=-=-=-=-=-=-=-=-=-=-=-
pgen = ((ncalf * 4)+ (nfisf*3)+ (nquimf * 4)+ (nalgf * 3))/14
#-=-=-=-=-=-=-=-=-=-=-=-=-
print("\n----------------------------")
print("[-Informacion final-]")
print("----------------------------")
print("La informacion con respecto a las notas del estudiante",nom,"N.D.",nom2,"Son:")
print("\tNota fina de Calculo:",ncalf)
print("\tNota fina de Fisica:",nfisf)
print("\tNota fina de Quimica:",nquimf)
print("\tNota fina de Algoritmo:",nalgf)
print("\tEL promedio General es de:",pgen)

#Estudiante Diego Román