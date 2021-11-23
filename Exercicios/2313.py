valores=list(map(int,input().split()))
valores.sort()
valores.reverse()
a, b, c = valores
if a>=(b+c):
    print('Invalido')
else:

    if a == b != c or b == c != a or a == c != b:
        print('Valido-Isoceles')
    elif a==b and b==c:
        print('Valido-Equilatero')
    else:
        print('Valido-Escaleno')
    if a**2==(b**2+c**2):
        sn='S'
    else:
        sn='N'
    print(f'Retangulo: {sn}')
