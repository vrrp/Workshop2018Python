"""
Busqueda lineal:

Funcionamiento:

1: Recorrer cada elemento de la lista
2: Ir comparando el elemento que se desea buscar con cada
   elemento de la lista
3: En caso de ser en contrado, retornar el índice en el que se
   encuentra, en caso contrario, falso, None, etc.
"""

def busquedaLineal(dato):
	for x in range(len(lista)):
		if lista[x]==dato:
			return x
	return None

def buscar(dato):
	if busquedaLineal(dato)==None:
		return "El dato %d no se encuentro"%(dato)
	else: 
		return "El dato %d se encontro en el indice: %d"%(dato,busquedaLineal(dato))



lista = [12,45,78,9,6,5,4,2,1,0,12,45,78,63,25,98]

for i in range(len(lista)):
	print("%d => %d"%(i,lista[i]))

print(buscar(0))