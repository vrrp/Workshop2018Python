# https://www.youtube.com/watch?v=X5VERDU1U8A&list=PLCh9J2_B_crLJN8L_1aVfJL-kjfEiazvv&index=3

https://github.com/SciTools/courses


lista = [4,2,6,8,5,7]
print(lista)

for i in range(len(lista)):
	for x in range(len(lista)-1):
		if lista[x]> lista[x+1]:
			aux = lista[x]

			lista[x]   = lista[x+1]
			lista[x+1] = aux
			print(lista)
