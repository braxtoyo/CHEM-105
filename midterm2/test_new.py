from tiinterp import run, Env, Halt
progs={n:open('src/%s.txt'%n,encoding='utf-8').read().rstrip('\n').replace('Pause ','Pause') for n in ['MT2LW','MT2G']}
def go(inputs):
    scr=[]
    try: run(progs,'MT2LW',Env(),list(inputs),[],scr)
    except Halt: pass
    except IndexError as e:
        if 'pop' not in str(e): raise
    keep=[l for l in scr if l not in('----','[pause]','WORKING…') and not str(l).startswith(('LEWIS SOLVER','TYPE CAPS','CHARGE OK','EG:','ANGLE','HYBRID','σ','OCTET COMPLETE','VALENCE'))]
    print(inputs,'\n  '+'\n  '.join(map(str,keep[:9])))
for t in [['SBR2','0'],['SBF5','0'],['SIF4','0'],['SNCL4','0'],['H2CO','0'],['CH3OH','0'],['CH3CL','0'],['NH4+'],['SO4-2'],['SO4⁻2'],['NO3-'],['CO3','2-'],['NH4','+'],['NO2','⁻'],['H2O',''],['C2H6','0'],['N2H4','0'],['SO 4','0'],['','0'],['XeF4','0'],['C2H4','0'],['QX','0']]:
    go(t)
