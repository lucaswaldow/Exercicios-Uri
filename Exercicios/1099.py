nx = int(input())

for x in range(nx):
    smimp = 0
    n1,n2 = map(int,input().split())
    if n2>n1:
        for n in range(n1 + 1, n2):
            if n % 2 != 0:
                smimp += n
    elif n1>n2:
        for n in range(n2 + 1, n1):
            if n % 2 != 0:
                smimp += n
    elif n1==n2:
        smimp = 0
    print(smimp)
