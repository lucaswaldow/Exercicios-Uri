nexp = int(input())
ttcob,qntcl,qntrt,qntsp = [0,0,0,0]
for x in range(nexp):
    qnt,tipo = input().split()
    qnt = int(qnt)
    ttcob += qnt
    if tipo=='C':
        qntcl += qnt
    if tipo=='R':
        qntrt += qnt
    if tipo=='S':
        qntsp += qnt
pqntcl = (qntcl*100)/ttcob
pqntrt = (qntrt*100)/ttcob
pqntsp = (qntsp*100)/ttcob
print(f'Total: {ttcob} cobaias')
print(f'Total de coelhos: {qntcl}')
print(f'Total de ratos: {qntrt}')
print(f'Total de sapos: {qntsp}')
print(f'Percentual de coelhos: {pqntcl:.2f} %')
print(f'Percentual de ratos: {pqntrt:.2f} %')
print(f'Percentual de sapos: {pqntsp:.2f} %')