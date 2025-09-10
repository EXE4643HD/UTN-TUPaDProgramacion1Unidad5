#4) Reemplazar el segundo y último valor de la lista
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