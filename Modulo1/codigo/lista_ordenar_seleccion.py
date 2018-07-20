# https://www.youtube.com/watch?v=X5VERDU1U8A&list=PLCh9J2_B_crLJN8L_1aVfJL-kjfEiazvv&index=3
"""
Ordenamiento por selección

Es un algoritmo que consiste en ordenar los elementos
de una lista de manera ascendente o descendente

Funcionamiento
- Buscar el dato mas pequeño de la lista
- Intercambiarlo por el actual
- Seguir buscando el dato mas pequeño de la lista
- Intercambiarlo por el actual
- Esto se repite sucesivamente
"""

lista = [4,2,6,8,5,7]
print(lista)

for i in range(len(lista)):
	minimo = i
	for x in range(i,len(lista)):
		if lista[x]< lista[minimo]:
			minimo = x

	aux = lista[i]
	lista[i] = lista[minimo]
	lista[minimo] = aux

print(lista)
