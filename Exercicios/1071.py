n1 = int(input())
n2 = int(input())
lista = [n1,n2]
lista.sort()
nm, nM = lista
nm += 1
numimp = 0
#while nm<nM:
#    if nm%2!=0:
#        numimp += nm
 #   nm += 1
for x in range(nm+1,nM):
    if nm % 2 != 0:
        numimp += nm
print(numimp)