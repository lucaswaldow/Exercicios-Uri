refa,refb,refc=map(int,input().split())
ea,eb,ec=map(int,input().split())
qnta=0
qntb=0
qntc=0
if refa<ea:
    qnta = ea-refa
if refb<eb:
    qntb = eb-refb
if refc<ec:
    qntc = ec-refc
print(qnta+qntb+qntc)