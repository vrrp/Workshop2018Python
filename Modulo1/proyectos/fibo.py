# Módulo de números Fibonacci

def fib(n):
	a,b = 0, 1
	while b < n:
		print(b, end=' ')
		a, b = b, a+b
	print("se ejecuto fib")


def fib2(n):
	a,b = 0, 1
	resultado = []

	while b < n:
		resultado.append(b)
		a, b = b, a+b
	print(resultado)
	return resultado
	

if __name__ == "__main__":
	import sys
	fib2(int(sys.argv[1]))
