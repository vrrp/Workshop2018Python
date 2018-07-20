"""
Ordenamiento por Inserción

Funcionamiento

1- Recorremos cada elemento de la lista
2- Cada elemento de la lista se ordena si su izquierda tiene un 
   elemento mayor que el actual
3- Si es correcto que el paso anterior, se hace el intercambio
   de valores
4- El elemento se sigue recorriendo hacia la izquierda hasta que 
   hasta que tenga un elemento menor.   
"""

lista =[5,10,3,12,10,6]
print(lista)

for i in range(1, len(lista)):
	aux = lista[i]
	j = i - 1
	while j >=0 and aux < lista[j]:
		lista[j+1] = lista[j]
		lista[j] = aux
		j -= 1
print(lista)