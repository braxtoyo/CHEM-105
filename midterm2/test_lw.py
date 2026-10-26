import sys
from tiinterp import run, Env, Halt
progs={n:open('src/%s.txt'%n,encoding='utf-8').read().rstrip('\n').replace('Pause ','Pause') for n in ['MT2LW','MT2G','MT2SN','MIDTERM2','MT2H']}
def lewis(f,c):
    env=Env(); scr=[]
    try: run(progs,'MT2LW',env,[f,str(c)],[],scr)
    except Halt: pass
    return scr
cases=sys.argv[1:] or ['SO4:-2','CO2:0','H2O:0','NH3:0','CH4:0','NH4:1','NO3:-1','CO3:-2','SO2:0','CO:0','NO:0','NO2:0','O3:0','BF3:0','XEF4:0','SF4:0','CLF3:0','I3:-1','PCL5:0','SF6:0','HNO3:0','H2SO4:0','HOCL:0','CL2O:0','N2O:0','HCN:0','CH2O:0','SCN:-1','CLO4:-1','CLO2:-1','PO4:-3','H3O:1','OH:-1','CN:-1','O2:0','N2:0','N3:-1','BECL2:0','XEF2:0','BRF5:0','H3PO3:0','H3PO4:0','H2O2:0','CLO3:-1','SO3:-2','HSO3:-1','HCO3:-1','H2PO4:-1','ICL4:-1','XeO3:0','CS2:0','OF2:0','S2:-2','CLO:-1','BRO3:-1']
for cs in cases:
    f,c=cs.split(':')
    try: scr=lewis(f,int(c))
    except Exception as e: print(f,c,'ERROR',repr(e)); continue
    out=[l for l in scr if l not in ('----','[pause]','WORKING...') and not l.startswith(('LEWIS SOLVER','TYPE CAPS','NUMBER AFTER'))]
    print('\n'.join(out)); print('=====')
