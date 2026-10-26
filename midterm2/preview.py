import sys
from tiinterp import run, Env, Halt
progs={n:open('src/%s.txt'%n,encoding='utf-8').read().rstrip('\n').replace('Pause ','Pause') for n in ['MT2LW','MT2G','MT2SN','MIDTERM2','MT2H']}
def show(prog,inputs,menus=(),quiet=False):
    scr=[]
    try: run(progs,prog,Env(),list(inputs),list(menus),scr)
    except Halt: pass
    except IndexError as e:
        if 'pop' not in str(e): raise
    # split into screens: a screen ends at Pause; ClrHome resets
    pages=[[]]; bad=0
    for l in scr:
        if l=='----': pages[-1]=[]
        elif l=='[pause]':
            disp=[x for x in pages[-1] if not x.startswith('[out')]
            if len(disp)>9: bad+=1; pages[-1].insert(0,'!!! %d LINES'%len(disp))
            pages.append([])
        else: pages[-1].append(str(l))
    if not quiet:
        for p in pages:
            if p: print('\n'.join(p)); print('-'*26)
        print('='*26)
    return bad
if __name__=='__main__':
    show('MT2LW',['CO2','0']); show('MT2LW',['HNO3','0']); show('MT2LW',['SO4-2']); show('MT2SN',['4','1'],[2])
