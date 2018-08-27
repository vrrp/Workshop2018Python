"""
:Autor:
       Víctor R. Rojas 
       E-mail: vr.rojaspozo@gmail.com

:Moculo:
    cinematica

:Proporciona:
    1. movMRU
    2. movMRUV
    
"""

def movMRU(t,v):
    """
    Movimiento rectilineo uniforme
    Uso:
        d = movMRU(t,v)

    Donde:
    t : tiempo (s)
    v : velocidad (m/s)
    d : distancia recorrida (m)
    
    """
    print("\nMRU")
    print("-"*len("MRU"))
    d = v*t
    print("d = ",v , "(", t, ") = ", d)
    return d

def movMRUV(t,v,a):
    """
    Movimiento rectilineo uniforme variado
    Uso:
        d = movMRUV(t,v,a)

    Donde:
    t : tiempo (s)
    v : velocidad (m/s)
    a : aceleración (m/s2)
    d : distancia recorrida (m)
    
    """
    print("\nMRUV")
    print("-"*len("MRU"))
    d=v*t + 1/2*a*t**2
    print("d = ", d)
    return d
