#url = "https://www.aviationweather.gov/metar/data?ids=spjc&format=decoded&hours=0&taf=off&layout=on&date=201808190404"
# http://www.corpac.gob.pe/app/Meteorologia/somos/estaciones.php
# http://www.corpac.gob.pe/app/Meteorologia/tiempo/reportemetar.php

"""
:Autor:
       Víctor R. Rojas 
       E-mail: vr.rojaspozo@gmail.com
:Moculo:
    getmetar
:Proporciona:
    1. getMetar
"""
def getMetar(year, imonth,iday,ihour,idMet):
	import urllib.request as gw
	if imonth<10:
		imonth = "0"+str(imonth)
	if iday<0:
		iday = "0"+str(iday)
	if ihour <10:
		ihour = "0"+str(ihour)


	date = str(year)+str(imonth)+str(iday)+str(ihour)
	#print(date)

	url = "https://www.aviationweather.gov/metar/data?ids="+idMet+"&format=decoded&hours=0&taf=off&layout=on&date="+date
	response = gw.urlopen(url)

	data = response.read()
	text = data.decode('utf-8') 
	idmetar = idMet.upper()

	findID = text.find(idmetar)
	#print(findID)
	varsPhy = text[findID+4:findID+900]
	findID = varsPhy.find(idmetar)
	varsPhy = varsPhy[findID+4:findID+2500]
	varsPhy = varsPhy.split("</td>")
	metarList = varsPhy[0]
	metarList = metarList.split()
	if 5<len(metarList)<20:
		metdate = metarList[0]
		newmetdate = str(year)+str(imonth)+metdate
		metarList[0]=newmetdate
		metarList=" ".join(metarList)
		#print(metarList)

		return metarList