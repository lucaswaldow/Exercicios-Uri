ndex = int(input())
lista = []
for i in range(ndex):
    lista.append(int(input()))
for x in range(ndex):
    if lista[x]==0:
        print('NULL')
    if lista[x]>0:
        if lista[x]%2==0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    if lista[x]<0:
        if lista[x]%2==0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
