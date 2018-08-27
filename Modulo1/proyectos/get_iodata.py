"""
:Autor:
       Víctor R. Rojas 
       E-mail: vr.rojaspozo@gmail.com
:Moculo:
    get_iodata    
:Proporciona:
    1. get_range
    2. save_files
    
"""
def get_range(inicio, fin, inc):
    """
    Genera un rango  de valores en una lista:
    Uso:
    lista = get_range(2,12,0.5)        
    """
    valor= inicio
    rangeval = []
    while valor<=fin:
        rangeval.append(valor)
        valor = valor + inc
    
    return rangeval

def save_files(lats, lons, saveName):
    """
    Genera un archivo plano (ASCII) de dos columnas en un directorio

    uso:
        save_files(lats, lons, save)

    Donde:
        [lats] y [lons] son variables de tipo lista y de igual número de
        elementos

        [saveName] es una cadena de  caracteres.

    """
    f = open(saveName, 'w')
    f.write('{0:2} {1:3}\n'.format("lons", "lats"))
    for ilat, ilon in zip(lats,lons):
        f.write('{0:2} {1:3}\n'.format(ilat, ilon))
    f.close()
    
    print(saveName, "se creo sin problema...!")