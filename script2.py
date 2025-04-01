
from sympy import *
import math
def s():
    # Do the stuff here.
    #E0, l, z, c, t = symbols("E0 l z c t")
    #the_thing = Matrix([0,0,-1/c])
    #x = E0*sin(2*pi/l*(z+c*t))
    #other_thing = Matrix([x, x, 0])
    
    q, E_0, c, t, m_p, l, tg, tf = symbols("q E_0 c t m_p l tg tf", real=True)
    # Now do the stuff...

    a_t = q*E_0/((1+((c*t)**2/(l**2)))*m_p)

    res = integrate(integrate(a_t, (t, 0, tg)), (tg, 0, tf))
    res = simplify(res)
    print("res: "+str(res))

    # Substitute stuff 

    # jossa E0 = 100 kV/m ja ℓ = 0,3 m. Arvioi protonin sijainti yhden mikrosekunnin jälkeen pulssin
    # pyyhkäisystä.

    # 1.67262192 × 10-27


    thing = res.subs({q: 1.602176634*10**(-19), m_p: 1.67262192*10**(-27), c: 299792458, tf: 1*(10**(-6)), l: 0.3, E_0: 100000})
    print(thing)

    return

def s2():

    c, I, r, u_0, l = symbols("c I r u_0 l")
    # Now do the stuff...

    w = 2*pi*c/l

    B_0 = sqrt(2*I/(c*u_0))

    res = B_0*w*pi*(r**2)

    res2 = res.subs({c: 299792458, r: 0.075, l: 6.9, I: 0.0275, u_0: 1.25663706127*10**(-6), pi: math.pi}) # 1.25663706127(20)×10−6
    print(res2)
    return


def s3():
    # Redefine everything with floating-point pi
    c, I, r, u_0, l = symbols("c I r u_0 l")

    # Substitute numerical values using float pi
    values = {
        c: 299_792_458,
        r: 0.075,
        l: 6.9,
        I: 0.0275,
        u_0: 4 * math.pi * 1e-7,
    }

    # Angular frequency
    w = 2 * math.pi * c / l
    print("w value: "+str(w.subs(values).evalf()))
    # Peak magnetic field from intensity
    # B_0 = sqrt(2 * I / (c * u_0))
    # B_0 = sqrt(2*I*u_0)

    eps0 = 8.85*10**(-12)

    B_0 = (sqrt(2*I/(c**3*eps0)))
    print("B_0 value: "+str(B_0.subs(values).evalf()))

    # Area

    A = math.pi * r**2

    print("A value: "+str(A.subs(values).evalf()))
    # EMF max = A * B0 * omega
    emf_max = B_0 * w * A

    emf_max_numeric = emf_max.subs(values).evalf()

    print(emf_max_numeric)
    return

if __name__=="__main__":
    # s2()
    s3()
    exit(0)

