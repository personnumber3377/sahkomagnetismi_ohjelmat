
from sympy import *
import math

def s():
    # Do the stuff here.
    
    eps0, E0, B0, k, y, w, t, u0, c = symbols("eps0 E0 B0 k y w t u0 c")

    E = 2*E0*sin(k*y)*cos(w*t)
    B = -2*B0*cos(k*y)*sin(w*t)
    
    res = 1/2*eps0*E**2 + 1/(2*u0)*(B**2)

    res = simplify(res)
    print("Res: "+str(res))

    thing = res.subs({B0: E0/c, u0: 1/(c**2*eps0)})
    thing = simplify(thing)
    print(thing)

    E_vec = Matrix([0,0,E])
    B_vec = Matrix([B,0,0])

    another_thing = E_vec.cross(B_vec)

    another_thing = another_thing.subs({B0: E0/c, u0: 1/(c**2*eps0)})
    another_thing = simplify(another_thing)
    print(another_thing)

    return



if __name__=="__main__":
    s()
    exit(0)

