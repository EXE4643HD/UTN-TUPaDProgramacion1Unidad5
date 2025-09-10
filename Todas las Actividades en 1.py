# 1) Crear una lista con los números del 1 al 100 que sean 
# múltiplos de 4. Utilizar la función range.
numero=list(range(0,101,4))
print (numero)

print()
print()
# 2) Crear una lista con cinco elementos (colocar los 
# elementos que más te gusten) y mostrar elpenúltimo.
# ¡Puedes hacerlo como se muestra en los videos o bien 
# investigar cómo funciona el indexing con números 
# negativos!
miLista=["Novo","Pablo","Lucas","Iris","Iker"]
print(miLista[-2])

print()
print()
# 3) Crear una lista vacía, agregar tres palabras con append
# e imprimir la lista resultante por pantalla. Pista: para 
# crear una lista vacía debes colocar los corchetes sin 
# nada en su interior. Por ejemplo:
# lista_vacia = []
miLista=[]
miLista.append("Exequiel")
miLista.append("Franco")
miLista.append("David")
print(miLista)

print()
print()
# 4) Reemplazar el segundo y último valor de la lista
# “animales” con las palabras “loro” y “oso”, 
# respectivamente. Imprimir la lista resultante por 
# pantalla. ¡Puedes hacerlo como se muestra en los videos 
# o bien investigar cómo funciona el indexing con números 
# negativos!
# animales = ["perro", "gato", "conejo", "pez"]
listaAnimeles=["perro", "gato", "conejo", "pez"]
listaAnimeles[1]="loro"
listaAnimeles[-1]="oso"
print(listaAnimeles)
print()
print()
animeles=["perro", "gato", "conejo", "pez"]
animeles.remove("gato")
animeles.pop()
animeles.insert(1,"loro")
animeles.append("oso")
print(animeles)

print()
print()
# 5) Analizar el siguiente programa y explicar con tus 
# palabras qué es lo que realiza.
# numeros= [8,15,3,22,7]
# numeros.remove(max(numero))
# Print (numero)
print("Se crea una lista con 5 elementos numericos [8,15,3,22,7], " \
"luego remueve el elemento mas grande de la lista y al final imprime " \
"la lista sin el numero mas grande (22)")

print()
print()
# 6) Crear una lista con números del 10 al 30 (incluído),
# haciendo saltos de 5 en 5 y mostrar por pantalla los 
# dos primeros.
numero=list(range(10,31,5))
print(numero[0], numero[1])

print()
print()
# 7) Reemplazar los dos valores centrales (índices 1 y 2)
# de la lista “autos” por dos nuevos valores cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]
autos=["sedan","polo","suran","gol"]
autos[1]="vento"
autos[2]="amarok"
print(autos)

print()
print()
# 8) Crear una lista vacía llamada "dobles" y agregar el 
# doble de 5, 10 y 15 usando append directamente. Imprimir
# la lista resultante por pantalla.
dobles=[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

print()
print()
# 9) Dada la lista “compras”, cuyos elementos representan
# los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras=[["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1]="tallarines"
# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
# d) Imprimir la lista resultante por pantalla
print(compras)

print()
print()
# 10) Elaborar una lista anidada llamada “lista_anidada” 
# que contenga los siguientes elementos:
listaAnidada=[[15],[True],[25.5,57.9,30.6],[False]]
# ● Posición lista_anidada[0]: 15
print(listaAnidada[0])
# ● Posición lista_anidada[1]: True
print(listaAnidada[1])
# ● Posición lista_anidada[2][0]: 25.5
print(listaAnidada[2][0])
# ● Posición lista_anidada[2][1]: 57.9
print(listaAnidada[2][1])
# ● Posición lista_anidada[2][2]: 30.6
print(listaAnidada[2][2])
# ● Posición lista_anidada[3]: False
print(listaAnidada[3])
# Imprimir la lista resultante por pantalla.
print(listaAnidada)
