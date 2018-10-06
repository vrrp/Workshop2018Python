# -*- coding: utf-8 -*-
import numpy as np
import numpy.ma as ma
import netCDF4 as nc 

def __version__():
    return "atmocean-v0.1"

def verImagen(data, interpol):
	import matplotlib.pyplot as plt
	import numpy as np

	fig = plt.figure(figsize=(9,6))
	ax0 = plt.axes((0.08, 0.15, 0.85, 0.8))

	if(interpol=="nearest"):
		img=ax0.imshow(data, interpolation='nearest')

	elif(interpol=="bilinear"):
		img = ax0.imshow(data, interpolation='bilinear')
	elif(interpol=="bicubic"):
		img = ax0.imshow(data, interpolation='bicubic')
	img.set_cmap('nipy_spectral')
	#colorbar_ax = fig.add_axes([0.09, 0.05, 0.84, 0.05]) # horizontal
	colorbar_ax = fig.add_axes([0.1, 0.05, 0.8, 0.05]) # horizontal
	fig.colorbar(img,orientation='horizontal', cax=colorbar_ax)
	#plt.figure()
	#plt.hist(data.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
	plt.show()

def near2d(x, y, x0, y0):
    """
    Ubicar los indices de los puntos de grilla
    que estan más proximos a las coordenadas (x0,y0)
    Ejemplo: line, col = near2d(x, y, x0, y0)
    """
    dx = np.abs(x - x0); dx = dx / dx.max()
    dy = np.abs(y - y0); dy = dy / dy.max()
    dn = dx + dy    
    fn = np.where(dn == dn.min())
    line = int(fn[0])
    col  = int(fn[1])
    return line, col 

class ncread(object):
	"""Almacenar, manipular informacion de archivos netcdf y extraer información.
	Ejemplo:
	--------"""	
	def __init__(self, filename):
		self.filename = filename    
		self.ncfile   = nc.Dataset(filename, mode='r+')
				
	def getvars(self):
		self.ncfile = nc.Dataset(self.filename)
		fo =self.ncfile
		for varname in fo.variables.keys():
			var = fo.variables[varname]
			print(varname, var.dtype, var.dimensions, var.shape)
		
	def getdata(self, vardata):
		self.data  = self.ncfile.variables[vardata][...]
		data = np.array(self.data)
		return data

class ncwrite(object):
	"""Almacenar, manipular informacion de archivos netcdf y extraer información.
	Ejemplo:
	--------"""	
	def __init__(self,lats,lons,data, ncOutName):
		self.data = data   
		
		ndimData =data.ndim
		self.ndimData = ndimData
				
		ncfile = nc.Dataset(ncOutName+'.nc','w') 

		if(ndimData ==2):
			pass
		elif(ndimData ==4):
			ngrps, nlevels, nlats, nlons = data.shape
			
			ncfile.createDimension('latitude',nlats)
			ncfile.createDimension('longitude',nlons)
			ncfile.createDimension('months',nlevels)

			nclats = ncfile.createVariable('latitude',np.dtype('float64').char,('latitude',))
			nclons = ncfile.createVariable('longitude',np.dtype('float64').char,('longitude',))

			nclats.units = 'degrees_north'
			nclons.units = 'degrees_east'

			nclats[:] = lats[:]
			nclons[:] = lons[:]

			varName = ['xgradMLS', 'ygradMLS', 'gradMLS']
			print(data.shape)
		
			for ivar in range(len(varName)):
				data2nc = ncfile.createVariable(varName[ivar],np.dtype('float32').char,('months','latitude','longitude'))
				data2nc.long_name = varName[ivar] ;
				data2nc.units = "PSU" ;
				data2nc.missing_value = float(999) ;
				data2nc.FillValue = float(999) ;
				data2nc.add_offset = float(0) ;
				data2nc.scale_factor = float(1) ;
				data2nc.valid_min = np.nanmin(data) ;
				data2nc.valid_max = np.nanmax(data);
				data2nc.standard_name = varName[ivar] ;
				data2nc[:] = data[ivar,:,:,:]

		ncfile.title = "Gradiente de salinidad zonal[xgradSalt], meridional[ygradSalt] y modulo [gradSalt]" ;
		ncfile.dsd_entry_id = "Grad Salt mensual V01" ;
		ncfile.references = "None" ;
		ncfile.institution = "PE Instituto Geofisico del Peru" ;
		ncfile.contact = "Victor R. Rojas: vr.rojaspozo@gmail.com" ;
		ncfile.gds_version_id = "v1.0" ;
		ncfile.netcdf_version_id = "version 4.4.1.1 of Dec 25 2016 19:06:13" ;
		ncfile.creation_date = "Sep  05  2017" ;
		ncfile.product_version = "0.1" ;
		ncfile.history = "www.marine.csiro.au/atlas. cars2009a" ;
		ncfile.grid_resolution = "0.5 degree" ;
		ncfile.source_data = " CSIRO Atlas of Regional Seas (CARS)" ;
		#ncfile.start_date = "20170131 UTC" ;
		#ncfile.start_time = "00:00:00 UTC" ;
		#ncfile.stop_date = "20170131 UTC" ;
		#ncfile.stop_time = "23:59:59 UTC" ;
		ncfile.southernmost_latitude = lats.min() ;
		ncfile.northernmost_latitude = lats.max() ;
		ncfile.westernmost_longitude = lons.min() ;
		ncfile.easternmost_longitude = lons.max() ;
		ncfile.file_quality_index = 0 ;
		ncfile.close()
		print(ncOutName, "was creaded succefully <|:>D")

class ncwrite_new(object):
	"""Almacenar, manipular informacion de archivos netcdf y extraer información.
	Ejemplo:
	--------"""	
	def __init__(self,lats,lons,data, attributes, ncOutName):
		self.data = data   
		
		ndimData =data.ndim
		self.ndimData = ndimData
				
		ncfile = nc.Dataset(ncOutName,'w') 

		if(ndimData ==2):
			pass
		elif(ndimData==3):
			nlevels, nlats, nlons = data.shape

			ncfile.createDimension('latitude',nlats)
			ncfile.createDimension('longitude',nlons)
			ncfile.createDimension('months',nlevels)

			nclats = ncfile.createVariable('latitude',np.dtype('float64').char,('latitude',))
			nclons = ncfile.createVariable('longitude',np.dtype('float64').char,('longitude',))

			nclats.units = 'degrees_north'
			nclons.units = 'degrees_east'

			nclats[:] = lats[:]
			nclons[:] = lons[:]

			data2nc = ncfile.createVariable(attributes["varName"],np.dtype('float32').char,('months','latitude','longitude'))
			data2nc.long_name = attributes["standardName"];
			data2nc.units = attributes["varUnit"] ;
			data2nc.missing_value = float(999) ;
			data2nc.FillValue = float(999) ;
			data2nc.add_offset = float(0) ;
			data2nc.scale_factor = float(1) ;
			data2nc.valid_min = np.nanmin(data) ;
			data2nc.valid_max = np.nanmax(data);
			#data2nc.standard_name =  ;
			data2nc[:] = data[:,:,:]

		elif(ndimData ==4):
			ngrps, nlevels, nlats, nlons = data.shape
			
			ncfile.createDimension('latitude',nlats)
			ncfile.createDimension('longitude',nlons)
			ncfile.createDimension('months',nlevels)

			nclats = ncfile.createVariable('latitude',np.dtype('float64').char,('latitude',))
			nclons = ncfile.createVariable('longitude',np.dtype('float64').char,('longitude',))

			nclats.units = 'degrees_north'
			nclons.units = 'degrees_east'
			
			nclats[:] = lats[:]
			nclons[:] = lons[:]

			varName  = attributes["varName"]
			unitName = attributes["varUnit"]
			
			for ivar in range(len(varName)):
				data2nc = ncfile.createVariable(varName[ivar],np.dtype('float32').char,('months','latitude','longitude'))
				data2nc.long_name = varName[ivar] ;
				data2nc.units = unitName[ivar] ;
				data2nc.missing_value = float(999) ;
				data2nc.FillValue = float(999) ;
				data2nc.add_offset = float(0) ;
				data2nc.scale_factor = float(1) ;
				data2nc.valid_min = np.nanmin(data[ivar,:,:,:]) ;
				data2nc.valid_max = np.nanmax(data[ivar,:,:,:]) ;
				#data2nc.standard_name = varName[ivar] ;
				data2nc[:] = data[ivar,:,:,:]

		from datetime import date
		dd=date.today()
		ncfile.title = attributes["title"]
		ncfile.references = attributes["references"] ;
		ncfile.institution = attributes["institution"] ;
		ncfile.contact = attributes["contact"];
		ncfile.source_data = attributes["source"] ;
		#ncfile.start_date = "20170131 UTC" ;
		#ncfile.start_time = "00:00:00 UTC" ;
		#ncfile.stop_date = "20170131 UTC" ;
		#ncfile.stop_time = "23:59:59 UTC" ;
		ncfile.southernmost_latitude = lats.min() ;
		ncfile.northernmost_latitude = lats.max() ;
		ncfile.westernmost_longitude = lons.min() ;
		ncfile.easternmost_longitude = lons.max() ;
		ncfile.grid_resolution = attributes["gridData"];
		ncfile.file_quality_index = 0 ;
		ncfile.netcdf_version_id = "version 4.4.1.1 of Dec 25 2016 19:06:13" ;
		ncfile.creation_date = dd.strftime("%A %d. %B %Y") ;
		ncfile.close()
		print(ncOutName, "\n\n\t The  netCDF file was creaded succefully\n\t\t <|:>D")

class index4latlon(object):
	def __init__(self, lons, lats, limit_lons, limit_lats):
		#lons = self.lons
		self.lons = lons
		self.lats = lats
		
		if(np.ndim(self.lons)==1):
			lons, lats =np.meshgrid(self.lons, self.lats)
			self.lons=lons
			self.lats=lats
		else: pass

		self.cornerlon, self.cornerlat =[],[]
		for index in range(len(limit_lons)):
			lin, col = near2d(lons, lats, limit_lons[index], limit_lats[index]) 
			self.cornerlon.append(col)
			self.cornerlat.append(lin)
		self.sublons = lons[cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]
		self.sublats = lats[cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]

	def getindex(self):
		indexLon = self.cornerlon
		indexLat = self.cornerlat
		return indexLat, indexLon

	def getlonlat(self):
		newlons = self.sublons
		newlats = self.sublats
		return newlons[0,:], newlats[:,0]
		
class subdominio(object):
	def __init__(self, lons, lats, limit_lons, limit_lats, dominio):
		#lons = self.lons
		self.lons = lons
		self.lats = lats
		self.dominio = dominio
		#print(np.shape(self.dominio))
		#print(np.ndim(self.dominio))
		

		cornerlon, cornerlat =[],[]
		if(np.ndim(self.lons)==1):
			lons, lats =np.meshgrid(self.lons, self.lats)
			self.lons=lons
			self.lats=lats
		if(np.ndim(self.dominio)==2):
			for index in range(len(limit_lons)):
				lin, col = near2d(lons, lats, limit_lons[index], limit_lats[index]) 
				cornerlon.append(col)
				cornerlat.append(lin)
			self.cornerlat = cornerlat
			self.cornerlon = cornerlon
			self.sublons = lons[cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]
			self.sublats = lats[cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]
			self.subdominio= dominio[cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]
		if(np.ndim(self.dominio)==3):
			for index in range(len(limit_lons)):
				lin, col = near2d(lons, lats, limit_lons[index], limit_lats[index]) 
				cornerlon.append(col)
				cornerlat.append(lin)
			self.cornerlat = cornerlat
			self.cornerlon = cornerlon
			self.sublons = lons[cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]
			self.sublats = lats[cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]
			self.subdominio= dominio[:,cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]
		if(np.ndim(self.dominio)==4):
			for index in range(len(limit_lons)):
				lin, col = near2d(lons, lats, limit_lons[index], limit_lats[index]) 
				cornerlon.append(col)
				cornerlat.append(lin)
			self.cornerlat = cornerlat
			self.cornerlon = cornerlon
			self.sublons = lons[cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]
			self.sublats = lats[cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]
			self.subdominio= dominio[:,:,cornerlat[0]:cornerlat[1], cornerlon[0]:cornerlon[1]]
					
	def getdata(self):
		#subdominio = self.subdominio
		return self.subdominio
	
	def getlat(self):
		#newlats = self.sublats
		#return newlats[:,0]
		return self.sublats

	def getlon(self):
		#newlons = self.sublons
		#return newlons[0,:]
		return self.sublons
	def getIndexSubDom(self):
		return self.cornerlat, self.cornerlon

	def m2e(self):
		#subdominio = self.subdominio
		EFM = np.mean(self.subdominio[0:3], axis=0)
		AMJ = np.mean(self.subdominio[3:6], axis=0)
		JAS = np.mean(self.subdominio[6:9], axis=0)
		OND = np.mean(self.subdominio[9:12], axis=0)
		return EFM, AMJ, JAS, OND

	def data2serietiempo(self):
		subdominio = self.subdominio
		ntimes, nrowa, ncols = subdominio.shape
		data = np.zeros((ntimes))
		for i in range(ntimes):
			idata = subdominio[i,:,:]
			data[i] = np.mean(idata)

		return data
class chGriddata(object):
	def interpol(idomine, irange,fdomine):
		from scipy.interpolate import interp1d
		
		options = ('linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic') 
		f = interp1d(idomine, irange, kind=options[0])   
		#f = interp1d(idomine, irange, kind='cubic')
		frange = f(fdomine) 
		return frange

	def highArray(limitLats,limitLons ,Lowlats, Lowlons, dataLowRes, resEspacial):
		def interpol(idomine, irange,fdomine):
			from scipy.interpolate import interp1d

			options = ('linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic') 
			f = interp1d(idomine, irange, kind=options[0])   
			#f = interp1d(idomine, irange, kind='cubic')
			frange = f(fdomine) 
			return frange
		# Iniciando interpolacion longitudinal
		#----------------------------------------------------------------------------
		ndim = np.ndim(dataLowRes)
		latlonDim= np.ndim(Lowlons)

		if(latlonDim ==1):
			xLowdomine = Lowlons
			yLowdomine = Lowlats
		if(latlonDim ==2):
			yLowdomine = Lowlats[:,0]
			xLowdomine = Lowlons[0,:] 
		xHighdomine = np.arange(limitLons[0], limitLons[1], resEspacial)
		
		#xLowrange = 1*dataLowRes[20,:]
		#xHighrange = interpol(xLowdomine, xLowrange,xHighdomine)
		
		#import matplotlib.pyplot as plt
		#for i in range(len())
		#plt.plot(xHighdomine[:-8], xHighrange[:-8], "ro")
		#plt.plot(xHighdomine, xHighrange, "ro")
		#plt.plot(xLowdomine, xLowrange, "bx")
				
		nrows, ncols = dataLowRes.shape
		dataIntLong = np.ones((nrows,len(xHighdomine))); dataIntLong[...]=np.nan

		for irow in range(nrows):
			xLowrange = dataLowRes[irow,:]
			xHighrange = interpol(xLowdomine, xLowrange,xHighdomine)
			dataIntLong[irow,:] = xHighrange

		# Iniciando interpolacion llatitudinal
		#----------------------------------------------------------------------------
		
		yHighdomine = np.arange(limitLats[0], limitLats[1], resEspacial)
		new_nrows, new_ncols = (len(yHighdomine),dataIntLong.shape[1])
		dataIntLat = np.ones((new_nrows, new_ncols)); dataIntLat[...]=np.nan

		for icol in range(new_ncols):
			yLowrange = dataIntLong[:,icol]
			yHighrange = interpol(yLowdomine, yLowrange,yHighdomine)
			dataIntLat[:,icol] =  yHighrange
		lats = yHighdomine
		lons = xHighdomine

		"""
		print(np.min(dataIntLat), np.max(dataIntLat))
		fig = plt.figure(figsize=(9,6))
		ax0 = plt.axes((0.08, 0.15, 0.85, 0.8))
		img=plt.imshow(dataIntLat[::-1,:], interpolation='nearest')
		colorbar_ax = fig.add_axes([0.1, 0.05, 0.8, 0.05]) # horizontal
		fig.colorbar(img,orientation='horizontal', cax=colorbar_ax)
		plt.show()
		exit()
		"""

		return lats, lons, dataIntLat

	def getIndex(shortArray, bigArray):
		indexArray = []
		for i in range(len(bigArray)):
			for j in range(len(shortArray)):
				if(bigArray[i]==shortArray[j]):
					indexArray.append(i)
		return indexArray

	def getlowFromHighArray(indexLat, indexLon, highArray ):
		nrows, ncols =(len(indexLat), len(indexLon))
		lowArray = np.ones((nrows, ncols))
		for irow in range(nrows):
			for icol in range(ncols):
				idx = indexLon[icol]
				idy = indexLat[irow]
				lowArray[irow, icol] =highArray[idy, idx] 
		return  lowArray

class saltBudget(object):
	def __init__(self):
		self.w = 2*np.pi/84600 # Velocidad angular de la tierra (velocidad de rotación)

	def Uekman(self, xtau, ytau, dens=None, lat=None, fillVal=None):
		"""
		Transporte horizontal del Ekman (Uek, Vek)

		Tek = (Uek, Vek) =    1       (ytau, -xtau)
						   -------- * 	
						   (dens*f)
		"""		
		if(xtau.ndim==1):
			f=2*self.w*np.sin(lat*np.pi/180)
			Uek = (ytau-xtau)/(dens*f)
			return Uek
			
		elif(xtau.ndim==3 and ytau.ndim==3):
			nlevs, nrows, ncols = xtau.shape
						
			Uek= np.zeros((nlevs,nrows,ncols)); Uek[:,:,:]=np.nan
			Vek= np.zeros((nlevs,nrows,ncols)); Uek[:,:,:]=np.nan
			for ilev in range(nlevs):
				for irow  in range(nrows):
					f=2*self.w*np.sin(lat[irow]*np.pi/180)
					for icol in range(ncols):
						if(xtau[ilev,irow,icol]!=fillVal and ytau[ilev,irow,icol]!=fillVal):
							if(lat[irow]<-0.75 or lat[irow]>0.75):
								Uek[ilev,irow,icol]=(ytau[ilev,irow,icol])/(dens*f)
								Vek[ilev,irow,icol]=(-1)*(xtau[ilev,irow,icol])/(dens*f)

			fillVal_Uek = np.where(Uek==0) 	# cambiar pixeles malos por nan
			fillVal_Vek = np.where(Vek==0) 	# cambiar pixeles malos por nan
			Uek[fillVal_Uek]=np.nan 	
			Vek[fillVal_Vek]=np.nan  		 		# cambiar pixeles malos por nan

			return Uek, Vek

	def Wekman(self,xtau, ytau,dens=None, lat=None, fillVal=None):
		"""
		Transporte vertical de ekman (Wek)
		Donde:
			Wek 	: Transporte vertical
			den = 1023 Kg/m**3 	: Densidad del agua
			[f]   = s**-1		: Factor de Coriolis
		"""	
		gradTaux = np.gradient(xtau)
		gradTauy = np.gradient(ytau)

		if(xtau.ndim==1):
			f=2*self.w*np.sin(lat*np.pi/180)
			Wek = (ytau-xtau)/(dens*f)
			return Wek
			
		elif(xtau.ndim==3 and ytau.ndim==3):
			nlevs, nrows, ncols = xtau.shape

			xgradTauy = gradTauy[1]
			ygradTaux = gradTaux[0]
									
			Wek= np.zeros((nlevs,nrows,ncols)); Wek[:,:,:]=np.nan
			for ilev in range(nlevs):
				for irow  in range(nrows):
					f=2*self.w*np.sin(lat[irow]*np.pi/180)
					for icol in range(ncols):
						if(xgradTauy[ilev,irow,icol]!=fillVal and ygradTaux[ilev,irow,icol]!=fillVal):
							if(lat[irow]<-0.5 or lat[irow]>0.5):
								Wek[ilev,irow,icol]=(xgradTauy[ilev,irow,icol]-ygradTaux[ilev,irow,icol])/(dens*f)
			return Wek


class plotMap(object):
	"""docstring for ClassName"""
	def __init__(self, lats, lons, projection=None, axis=None):
		self.pgf_with_latex = {              # setup matplotlib to use latex for output
		   "pgf.texsystem": "pdflatex",        # change this if using xetex or lautex
		   "text.usetex": True,                # use LaTeX to write all text
		   "font.family": "sans-serif",
		   "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
		   "font.sans-serif": [],
		   "font.monospace": [],
		   "font.weight": 'bold',
		   "axes.labelsize": 16,#10,               # LaTeX default is 10pt font.
		   #"text.fontsize": 16,#10,
		   "font.size": 16,#10,
		   "legend.fontsize": 14,#8,               # Make the legend/label fonts a little smaller
		   "xtick.labelsize": 14,#8,
		   "ytick.labelsize": 14,#8,
		   #"figure.figsize": figsize(0.9),     # default fig size of 0.9 textwidth
		   "pgf.preamble": [
		         r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
		         r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
		         ]
		     }
		self.labelfont = {
			'family' : 'textrm',  # (textrm, sans-serif, cursive, fantasy, monospace, serif)
			'color'  : 'black',       # html hex or colour name
			'weight' : 'normal',      # (normal, bold, bolder, lighter)
			'size'   : 16,            # default value:12
			    }
		self.titlefont = {
		   	'family' : 'serif',
		   	'color'  : 'black',
		   	'weight' : 'bold',
		   	'size'   : 20,
		   	 	}

		self.cbarfont = {
			'family' : 'sans-serif',
			'color'  : 'black',
			#'weight' : 'bold',
			'style'  : 'normal',
			'size'   : 20,#'x-large',
			}
		self.temp_label_name = {
		    'family' : 'serif',
		    'color'  : 'black',
		    'weight' : 'bold',
		    'size'   : 14,
		    }
		self.temp_label_value = {
		    'family' : 'serif',
		    'color'  : 'red',
		    'weight' : 'bold',
		    'size'   : 14,
		    }

		self.labelcontour = {
			'family' : 'sans-serif',
			'color'  : 'black',
			#'weight' : 'bold',
			'style'  : 'normal',
			'size'   : 20,#'x-large',
			}
		self.labelaxis = {
			'family' : 'sans-serif',
			'color'  : 'black',
			#'weight' : 'bold',
			'style'  : 'normal',
			'size'   : 20,#'x-large',
			}
		from mpl_toolkits.basemap import Basemap
		import numpy as np
		lats = np.array(lats)
		lons = np.array(lons)

		self.lats = lats
		self.lons = lons

		if(projection=='cyl'):
			self.map = Basemap(llcrnrlon = lons.min(),
						  llcrnrlat = lats.min(),
						  urcrnrlon = lons.max(),
						  urcrnrlat = lats.max(),
						  projection='cyl', 
						  lat_0=-12, lon_0=-75,
						  resolution="h",
						  ax=axis)
		elif(projection is None):
			data_axes = figure.add_axes([0.01, 0.05, 0.9, 0.88])
			self.map = Basemap(llcrnrlon =lons.min(),
				          llcrnrlat = lats.min(),
				          urcrnrlon = lons.max(),
				          urcrnrlat = lats.max(),
				          projection = 'mill',
				          resolution="h",
				          ax=data_axes)

	
	#def displayMap(self, lats, lons,data,cb_axes, saveName):
	def displayMap(self,lats,lons, data,cb_axes,title ,saveName,clevs=None,cbarlevs=None):
		from matplotlib import rcParams, cm
		import matplotlib.pyplot as plt
		#from mpl_toolkits.basemap import Basemap
		import numpy as np

		if(clevs is None):
			cbar_ini, cbar_fin = (int(np.nanmin(data)), int(np.nanmax(data)))
			print(cbar_ini, cbar_fin)
			cbarlevs=np.arange(0,cbar_fin+10, 5)
			clevs = np.arange(0,cbar_fin, 5)
			format_cont = '%d'#'%1.1f'

		else:
			format_cont = '%1.2f'

		overlay_color = 'black'
		
		
		labelfont_contour= 10

		self.lats = lats
		self.lons = lons

		m = self.map
		x, y = m(self.lons, self.lats)
		with plt.style.context('fivethirtyeight'):
			m.drawcoastlines(linewidth=1.4, linestyle='solid', color=overlay_color,\
				             antialiased=1, ax=None, zorder=None)
			m.drawcountries(linewidth=1.4, linestyle='solid',color=overlay_color)

			#m.drawstates(linewidth=1.4, linestyle='solid', color=overlay_color)
			#m.bluemarble()
			#m.shadedrelief()
			#m.etopo()
			m.drawmeridians(np.arange(int(lons.min()),int(lons.max()),10), labels=[0,0,0,1],linewidth=1.4, color=overlay_color)
			m.drawparallels(np.arange(int(lats.min()),int(lats.max()),5), labels=[1,0,0,0],linewidth=1.4, color=overlay_color)
			#m.drawmeridians(np.arange(int(lons.min()),int(lons.max()),1), labels=[0,0,0,1],linewidth=1.4, color=overlay_color)
			#m.drawparallels(np.arange(int(lats.min()),int(lats.max()),1), labels=[1,0,0,0],linewidth=1.4, color=overlay_color)

			# Tipo colores
			cmap = cm.jet
			#cmap = plt.get_cmap('PiYG')
			#cmap = cm.PRGn          #<--- cambia tipo de paleta
			#cmap = cm.rainbow   
			#cmap = plt.get_cmap('hot')

			#im1 = m.pcolormesh(x,y,data,shading='flat',cmap=plt.cm.jet, latlon=True)
			#im1 = m.imshow(data, interpolation='nearest', cmap=plt.get_cmap(cmap))
			im1 = m.contourf(x,y,data,clevs,extend='both', ticks=clevs, cmap=cmap)
			cs = m.contour(x,y,data,clevs,linewidths=.5, colors='k')
			plt.clabel(cs,inline=True, fmt = format_cont, colors = 'k', fontsize=labelfont_contour)
			cbar = plt.colorbar(im1,cax=cb_axes,orientation='vertical', ticks=cbarlevs)
			#cbar.set_label(r'$\mathtt{Temperature }$ [$^\circ$C]', fontdict=cbarfont) # Label nombre de la barra de color
			cbar.ax.tick_params(labelsize=18) 
			cbar.set_ticks(cbarlevs)
			plt.title(title, fontsize=labelfont_contour)
		plt.savefig(saveName, format='png', dpi=100)



		