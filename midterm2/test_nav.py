import re
from tiinterp import run, Env, Halt
progs={n:open('src/%s.txt'%n,encoding='utf-8').read().rstrip('\n').replace('Pause ','Pause') for n in ['MT2LW','MT2G','MT2SN','MIDTERM2','MT2H']}
src=progs['MIDTERM2']
labels=set(re.findall(r'^Lbl (\S+)$',src,re.M))
for t in re.findall(r'^Goto (\S+)$',src,re.M): assert t in labels,t
for m in re.findall(r'^Menu\((.*)\)$',src,re.M):
    from tiinterp import split_args
    a=split_args(m)
    for t in a[2::2]: assert t in labels,t
print('labels ok', len(labels))
# crawl every option of every menu then BACK and QUIT
n=0;wide=0
for i in range(1,8):
    for j in range(1,8):
        scr=[]
        try: run(progs,'MIDTERM2',Env(),[],[i,j,6,6,7,7,7],scr)
        except Halt: pass
        except IndexError as e:  # inputs needed (solvers)
            pass
        wide+=sum(1 for l in scr if str(l).startswith('!!'))
        n+=1
print('crawled',n,'wide lines',wide)
# SN tool every valid combo
for S in range(2,7):
    for L in range(0,S):
        scr=[]
        try: run(progs,'MT2SN',Env(),[str(S),str(L)],[2],scr)
        except Halt: pass
        assert not any('?' == l for l in scr), (S,L)
        if S==4 and L==1: print('\n'.join(x for x in scr if x not in('----',)))
scr=[]
run(progs,'MT2SN',Env(),['7','0','4','4','3','1'],[2],scr); print([l for l in scr if 'USE' in str(l)][:2], scr[-12:-9])
