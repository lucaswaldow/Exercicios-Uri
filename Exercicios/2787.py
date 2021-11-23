linha=int(input())
coluna=int(input())
linha = linha%2
coluna = coluna%2


if linha!=0:
    if coluna!=0:
        print('1')
    else:
        print('0')
if linha==0:
    if coluna!=0:
        print('0')
    else:
        print('1')