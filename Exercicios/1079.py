n = int(input())
for i in range(n):
    nt1, nt2, nt3 = map(float,input().split())
    nota = (nt1*2+nt2*3+nt3*5)/(2+3+5)
    print(f'{nota:.1f}')