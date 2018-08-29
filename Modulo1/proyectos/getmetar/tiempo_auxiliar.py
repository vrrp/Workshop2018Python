import os
import pymetar

def visualizar_web(nombre_fichero):
	os.system("explorer"+nombre_fichero)

def cargar_fichero():
	nom_fich = os.path.realpath("id_zonas.txt")

	try:
		# Creamos una lista de listas, esto es, una lista que
		# contendrá listas
		lineas = []

		# Abrimos el fichero
		fichero = open(os.path.realpath(nom_fich), 'r')

		# Tratamos cada línea del fichero
		while True:
			linea = fichero.readline()

			if not linea:
				break

			# Separamos los lugares de sus ID
			linea = linea.split("(")

			# Apilar linea a la lista
			lineas.append(linea)

		# Obtener identificadores
		datos = []
		for dato in lineas:
			lugar = dato[0]
			coordenadas = dato[1].split(",")
			if coordenadas[1].count("-")>0:
				identificador = coordenadas[0][0:5]

			else:
				identificador = coordenadas[1][0:5]

			# Formato de la cadena resultante
			aux = lugar + ": " + identificador

			# Agregar al resultado
			datos.append(aux)

		# Cerrar fichero
		fichero.close
	except:
		print("""
			No se pudo abrir el fichero de zonas geograficas

			""")
		nom_fich = ""
		continuar()

	# Devolder la lista con las filas del fichero
	return datos, nom_fich

def obtener_tiempo(codigo_estacion):
	""" Obtiene datos de centro meteorologico, a partir de ID de estacion"""
	print(codigo_estacion)

	# Conectamos
	try:
		# Obtenemos informe del tiempo climático sin formato
		aux = pymetar.ReportFetcher(codigo_estacion)
		informe_sin_formato = aux.FetchReport()

		# Dar formato al informe
		formateador_informe = pymetar.ReportParser()
		informe = formateador_informe.ParseReport(informe_sin_formato)

	except:
		print("No se puede acceder a la información meteorológica")
		return

	# Obtenemos información
	ret = []
	aux = "Nombre de estación: " + informe.getStationName()
	ret.append(aux)

	aux = "Hora de medición: " + str(informe.getTime())
	ret.append(aux)
	




def menu():
	"""Menu principal de la aplicación"""
	print("""
		Menu Principal
		--------------

		Aplicación para obtener datos meteorológicos de Perú.

		Elegir una opción:

		1) Mostrar las estaciones
		2) Consultar
		3) Guardar datos en formato web
		0) Salir

		""")
	opcion = input("opcion: ")
	return opcion
