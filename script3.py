
from sympy import *

def s():
    # Do the stuff here.
    #E0, l, z, c, t = symbols("E0 l z c t")
    #the_thing = Matrix([0,0,-1/c])
    #x = E0*sin(2*pi/l*(z+c*t))
    #other_thing = Matrix([x, x, 0])
    #res = the_thing.cross(other_thing)
    #print(res)
    
    I, eps0, c = symbols("I eps0 c")
    eps0 = 8.854187817*10**(-12)
    c = 299792458 # Speed of light
    I = 1360
    E_rms = sqrt((2*I)/(eps0*c))
    
    print("E_rms = "+str(E_rms))

    B_rms = E_rms/c

    print("B_rms = "+str(B_rms))

    # Now the thing

    B_earth = 50*(10**(-6)) # 50 microtesla

    print("As earths magnetic fields: "+str(B_rms/B_earth))

    return

if __name__=="__main__":
    s()
    exit(0)

