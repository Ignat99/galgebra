#test_latest.py

from sympy import symbols
from ga import Ga
from mv import Mv
from printer import def_prec,GAeval,Eprint,oprint

def main():
    Eprint()

    coords = symbols('x y z')
    (o3d,ex,ey,ez) = Ga.build('ex ey ez',g=[1,1,1],coords=coords)

    mfvar = (u,v) = symbols('u v')

    eu = ex+ey
    ev = ex-ey

    (eu_r,ev_r) = o3d.ReciprocalFrame([eu,ev])

    oprint('Frame',(eu,ev),'Reciprocal Frame',(eu_r,ev_r))

    print 'eu.eu_r =',eu|eu_r
    print 'eu.ev_r =',eu|ev_r
    print 'ev.eu_r =',ev|eu_r
    print 'ev.ev_r =',ev|ev_r

    eu = ex+ey+ez
    ev = ex-ey

    (eu_r,ev_r) = o3d.ReciprocalFrame([eu,ev])

    oprint('Frame',(eu,ev),'Reciprocal Frame',(eu_r,ev_r))

    print 'eu.eu_r =',eu|eu_r
    print 'eu.ev_r =',eu|ev_r
    print 'ev.eu_r =',ev|eu_r
    print 'ev.ev_r =',ev|ev_r

    print 'eu =',eu
    print 'ev =',ev

    def_prec(locals())

    print GAeval('eu^ev|ex',True)
    print GAeval('eu^ev|ex*eu',True)
    return

if __name__ == "__main__":
    main()
