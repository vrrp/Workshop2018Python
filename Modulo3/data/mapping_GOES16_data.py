import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from datetime import datetime, timedelta
from netCDF4 import Dataset
import numpy as np
from pyproj import Proj 
import os 

"""
Source :
	https://github.com/blaylockbk/pyBKB_v2/blob/master/BB_goes16/mapping_GOES16_data.ipynb
"""
dataGoes16_path = "/home/data/goes/goes16/"
os.chdir(dataGoes16_path)
# F is for the Full Disk NetCDF file
#F_file = 'OR_ABI-L2-MCMIPF-M3_G16_s20172531745358_e20172531756131_c20172531756202.nc'
F_file = 'OR_ABI-L2-MCMIPF-M3_G16_s20180051715394_e20180051726166_c20180051726251.nc'
F = Dataset(F_file, 'r')

# Load the RGB arrays and apply a gamma correction (square root)
R = np.sqrt(F.variables['CMI_C02']) # Band 2 is red (0.64 um)
G = np.sqrt(F.variables['CMI_C03']) # Band 3 is "green" (0.865 um)
B = np.sqrt(F.variables['CMI_C01']) # Band 1 is blue (0.47 um)

# "True Green" is some linear interpolation between the three channels
G_true = 0.48358168 * R + 0.45706946 * B + 0.06038137 * G

# The final RGB array :)
RGB = np.dstack([R, G_true, B])

# Seconds since 2000-01-01 12:00:00
add_seconds = F.variables['t'][0]


#DATE = datetime(2000, 1, 1, 12) + timedelta(seconds=add_seconds)


# goes_imager_projection
#--------------------------------------------------------------------------------------
# Satellite height
sat_h = F.variables['goes_imager_projection'].perspective_point_height
# Satellite longitude
sat_lon = F.variables['goes_imager_projection'].longitude_of_projection_origin
# Satellite sweep
sat_sweep = F.variables['goes_imager_projection'].sweep_angle_axis

# geospatial_lat_lon_extent
#--------------------------------------------------------------------------------------
lon_0 = F.variables["geospatial_lat_lon_extent"].geospatial_lon_center

# The projection x and y coordinates equals
# the scanning angle (in radians) multiplied by the satellite height (http://proj4.org/projections/geos.html)
X = F.variables['x'][:] * sat_h
Y = F.variables['y'][:] * sat_h

# Convert map points to latitude and longitude with the magic provided by Pyproj
#--------------------------------------------------------------------------------------
XX, YY = np.meshgrid(X, Y)

p = Proj(proj='geos', h=sat_h, lon_0=sat_lon, sweep=sat_sweep)
lons, lats = p(XX, YY, inverse=True)

"""
# The geostationary projection
plt.figure(figsize=[10, 8])
m = Basemap(projection='geos', lon_0=lon_0,
            llcrnrx=X.min(),llcrnry=Y.min(),
            urcrnrx=X.max(),urcrnry=Y.max())
m.imshow(np.flipud(RGB)) # Remember, "images" are upside down, so flip up/down
m.drawcoastlines()
m.drawcountries()
plt.title(DATE)
#plt.show()

print(np.ndim(lons), np.shape(lons))
for i,j in zip(XX[100,:], lons[100,:]):
	print(i, "----->", j)
exit()
"""

import atmocean as ao
# Perú
#limit_lats = [-23.25, 15.25]     
#limit_lons = [-110.25, -59.25]

# Sudamérica
limit_lats = [-40.25, 15.25]    
limit_lons = [-110.25, -45.25]


newDom=ao.subdominio(lons, lats, limit_lons, limit_lats, R)
idxlat, idxlon = newDom.getIndexSubDom()
print(idxlat,"\n", idxlon)

newR = R[idxlat[1]:idxlat[0], idxlon[0]:idxlon[1]]
newG = G[idxlat[1]:idxlat[0], idxlon[0]:idxlon[1]]
newB = B[idxlat[1]:idxlat[0], idxlon[0]:idxlon[1]]

subLats = lats[idxlat[1]:idxlat[0], idxlon[0]:idxlon[1]]
subLons = lons[idxlat[1]:idxlat[0], idxlon[0]:idxlon[1]]


def verImagen(data,lats, lons, interpol):
	import matplotlib.pyplot as plt
	import numpy as np

	fig = plt.figure(figsize=(9,6))
	ax0 = plt.axes((0.08, 0.15, 0.85, 0.8))

	if(interpol=="nearest"):
		img=ax0.imshow(data, interpolation='nearest')

	elif(interpol=="bilinear"):
		cmap = plt.cm.get_cmap('jet_r')
		#img = ax0.imshow(data, interpolation='bilinear')
		img = ax0.pcolormesh(lons, lats, data, cmap=cmap)

	elif(interpol=="bicubic"):
		img = ax0.imshow(data, interpolation='bicubic')
	img.set_cmap('nipy_spectral')
	"""

	import shapefile as shp
	sf = shp.Reader('/home/data/shape/Countries_Shape/ne_10m_admin_0_countries.shp')

	for shape in sf.shapeRecords():
		# indexando cada componente del mapa 
		l = shape.shape.parts
		len_l = len(l)  # cantidad de paises i.e. islas y continentes
		xsh = [i[0] for i in shape.shape.points[:]] # lista de latitudes
		ysh = [i[1] for i in shape.shape.points[:]] # lista de longitudes
		l.append(len(xsh)) # asegurar el cierre del último componente
		for k in range(len_l):
			# graficar cada componente del mapa
			# l[k] a l[k + 1] es el conjunto puntos que forman cada componente
			plt.plot(xsh[l[k]:l[k + 1]],ysh[l[k]:l[k + 1]], 'k-')

	# colocar polígono
	latlon = [2,-86,-23, -63]
	xpolig = [latlon[1], latlon[1], latlon[3], latlon[3], latlon[1]]
	ypolig = [latlon[0], latlon[2], latlon[2], latlon[0], latlon[0]]
	plt.plot(xpolig, ypolig, "b--")
	"""

	#colorbar_ax = fig.add_axes([0.09, 0.05, 0.84, 0.05]) # horizontal
	colorbar_ax = fig.add_axes([0.1, 0.05, 0.8, 0.05]) # horizontal
	fig.colorbar(img,orientation='horizontal', cax=colorbar_ax)
	#plt.figure()
	#plt.hist(data.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
	plt.show()

verImagen(newG,subLats, subLons, "bilinear")


