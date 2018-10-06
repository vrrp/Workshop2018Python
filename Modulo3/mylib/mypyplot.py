
"""
  :Autor:
		VR. Rojas 
        E-mail: vr.rojaspozo@gmail.com
  
  :Catergoria:
      Visualización de datos
"""

def plot1p(data1, lats, lons, cbarName, out_name, putshp=None, subR=None, city=None):
	# Crear base para graficar panel 1
	import matplotlib.pyplot as plt
	import numpy as np
	import matplotlib
	params = {'font.size'     : 18,
	          'figure.figsize':(12.0, 9.0), # 'figure.figsize':(ncols, nfilas)
	          'lines.linewidth': 2.,
	          'lines.markersize': 15,
	          'lines.linestyle' : "-",
	          'lines.marker' : 'o'}
	matplotlib.rcParams.update(params)
	fig = plt.figure(facecolor='w')
	ax =fig.add_axes([0.08,0.1,0.79,0.85])

	cmap = plt.cm.get_cmap('rainbow')
	ax.set_xlabel(r'$\mathtt{LON} $')
	ax.set_ylabel(r'$\mathtt{LAT}$')
	if subR is not None:
		ax.set_ylim([subR[0], subR[1]])
		ax.set_xlim([subR[2], subR[3]])

	ax.grid(b=True, which='major', color='grey', linestyle='--', alpha=0.4)

	if np.ndim(lats)==1:
		x, y = np.meshgrid(lons, lats)
	else: 
		x,y = lons, lats

	# contourf
	con = plt.contourf(x, y, data1,30, 
		               alpha=.95, 
		               cmap=cmap)

	# contour
	cs = plt.contour(x, y, data1,30,
		             linewidths=0.5,
		             colors="k")
	plt.clabel(cs, fontsize=14, inline=1, fmt='%1.1f')

	# Poner shape
	if putshp is not None:
		# colocar shapefile
		import shapefile as shp
		sf = shp.Reader(putshp)
		for shape in sf.shapeRecords():
			# indexando cada componente del mapa 
			l = shape.shape.parts
			len_l = len(l)  # cantidad de paises i.e. islas y continentes
			xsh = [i[0] for i in shape.shape.points[:]] # lista de latitudes
			ysh = [i[1] for i in shape.shape.points[:]] # lista de longitudes
			l.append(len(xsh)) # asegurar el cierre del último componente
			for k in range(len_l):
				# graficar cada componente del mapa
				# l[k] a l[k + 1] es el conjunto de puntos que forman cada componente
				plt.plot(xsh[l[k]:l[k + 1]],ysh[l[k]:l[k + 1]], 'k-')
	
	# Poner etiquetas en el mapa
	if city is not None:
		clon = city["lons"]
		clat = city["lats"]
		delta_lon = 0.8
		nameCity = city["cname"]
		
		for i in range(len(nameCity)):
			plt.plot(clon[i], clat[i], "bo", markersize=15)
			plt.text(clon[i] + delta_lon, clat[i], nameCity[i], size=10, rotation=30.,
			         ha="center", va="center",
					 bbox=dict(boxstyle="round",
					 ec=(1., 0.5, 0.5),
					 fc=(1., 0.8, 0.8),
					 ))
		
	# barra de colores
	name_colobar = cbarName
	ax_cbar = fig.add_axes([0.88, 0.1, 0.03, 0.43])			
	cbar = plt.colorbar(con,cax=ax_cbar, orientation='vertical')
	cbar.set_label(name_colobar)
	cbar.ax.tick_params(labelsize=20)

	
	# Guardar grafico
	#plt.savefig(out_name+".png", format='png', dpi=200, transparent=True, pad_inches=0.05)
	#plt.savefig(out_name+".eps", format='eps')
	plt.savefig(out_name+".pdf", format='pdf')
	#plt.savefig(out_name+".ps", format='ps')
	#plt.savefig(out_name+".svg", format='svg')
	print("Tienes suerte, los graficos se crearon sin problemas...")

def plot2p(data1, data2,lats, lons,cbarName=None, putshp=None):
	# Crear base para graficar panel 1
	import matplotlib.pyplot as plt
	import numpy as np
	import matplotlib
	params = {'font.size'     : 18,
	          'figure.figsize':(12.0, 12.0), # 'figure.figsize':(ncols, nfilas)
	          'lines.linewidth': 2.,
	          'lines.markersize': 15,
	          'lines.linestyle' : "-",
	          'lines.marker' : 'o'}
	matplotlib.rcParams.update(params)
	fig = plt.figure(facecolor='w')
	ax =fig.add_axes([0.1,0.55,0.76,0.43])

	cmap = plt.cm.get_cmap('rainbow')
	ax.set_xlabel(r'$\mathtt{LON} $')
	ax.set_ylabel(r'$\mathtt{LAT}$')
	ax.grid(b=True, which='major', color='grey', linestyle='--', alpha=0.4)

	if np.ndim(lats)==1:
		x, y = np.meshgrid(lons, lats)
	else: 
		x,y = lons, lats

	# contourf
	con = plt.contourf(x, y, data1,30, 
		               alpha=.95, 
		               cmap=cmap)

	# contour
	cs = plt.contour(x, y, data1,30,
		             linewidths=0.5,
		             colors="k")
	plt.clabel(cs, fontsize=10, inline=1, fmt='%1.1f')
	# Poner shape
	if putshp is not None:
		# colocar shapefile
		import shapefile as shp
		sf = shp.Reader(putshp)
		for shape in sf.shapeRecords():
			# indexando cada componente del mapa 
			l = shape.shape.parts
			len_l = len(l)  # cantidad de paises i.e. islas y continentes
			xsh = [i[0] for i in shape.shape.points[:]] # lista de latitudes
			ysh = [i[1] for i in shape.shape.points[:]] # lista de longitudes
			l.append(len(xsh)) # asegurar el cierre del último componente
			for k in range(len_l):
				# graficar cada componente del mapa
				# l[k] a l[k + 1] es el conjunto de puntos que forman cada componente
				plt.plot(xsh[l[k]:l[k + 1]],ysh[l[k]:l[k + 1]], 'k-')

	if cbarName is not None:
		# barra de colores
		ax_cbar = fig.add_axes([0.88, 0.55, 0.03, 0.43])			
		cbar = plt.colorbar(con,cax=ax_cbar, orientation='vertical')
		cbar.set_label(cbarName[0])
		cbar.ax.tick_params(labelsize=20)
	else:
		ax_cbar = fig.add_axes([0.88, 0.08, 0.03, 0.4])			
		cbar = plt.colorbar(con,cax=ax_cbar, orientation='vertical')
		cbar.ax.tick_params(labelsize=20)
	
	#--------------------------------------------------------------------------------------------
	# Crear base para graficar panel 2
	ax2 =fig.add_axes([0.1,0.08,0.76,0.4])

	cmap = plt.cm.get_cmap('jet')
	ax2.set_xlabel(r'$\mathtt{LON} $')
	ax2.set_ylabel(r'$\mathtt{LAT}$')
	ax2.grid(b=True, which='major', color='grey', linestyle='--', alpha=0.4)

	x, y = np.meshgrid(lons, lats)

	# contourf
	con = plt.contourf(x, y, data2,30, 
		               alpha=.95, 
		               cmap=cmap)

	# contour
	cs = plt.contour(x, y, data2,60,
		             linewidths=0.5,
		             colors="k")
	plt.clabel(cs, fontsize=10, inline=1, fmt='%1.1f')

	# Poner shape
	if putshp is not None:
		# colocar shapefile
		import shapefile as shp
		sf = shp.Reader(putshp)
		for shape in sf.shapeRecords():
			# indexando cada componente del mapa 
			l = shape.shape.parts
			len_l = len(l)  # cantidad de paises i.e. islas y continentes
			xsh = [i[0] for i in shape.shape.points[:]] # lista de latitudes
			ysh = [i[1] for i in shape.shape.points[:]] # lista de longitudes
			l.append(len(xsh)) # asegurar el cierre del último componente
			for k in range(len_l):
				# graficar cada componente del mapa
				# l[k] a l[k + 1] es el conjunto de puntos que forman cada componente
				plt.plot(xsh[l[k]:l[k + 1]],ysh[l[k]:l[k + 1]], 'k-')
	if cbarName is not None:
		# barra de colores
		ax_cbar = fig.add_axes([0.88, 0.08, 0.03, 0.4])			
		cbar = plt.colorbar(con,cax=ax_cbar, orientation='vertical')
		cbar.set_label(cbarName[1])
		cbar.ax.tick_params(labelsize=20)
	else:
		ax_cbar = fig.add_axes([0.88, 0.08, 0.03, 0.4])			
		cbar = plt.colorbar(con,cax=ax_cbar, orientation='vertical')
		cbar.ax.tick_params(labelsize=20)

	# Guardar grafico
	out_name = "./graficos/sst_prc"
	#plt.savefig(out_name+".png", format='png', dpi=200, transparent=True, pad_inches=0.05)
	#plt.savefig(out_name+".eps", format='eps')
	plt.savefig(out_name+".pdf", format='pdf')
	#plt.savefig(out_name+".ps", format='ps')
	#plt.savefig(out_name+".svg", format='svg')
	print("Tienes suerte, los graficos se crearon sin problemas...")