'''a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
x = a,b,c,d,e,f'''
qntp = 0
for x in range(1,7):
    num = float(input())
    if num>0:
        qntp += 1

print(f'{qntp} valores positivos')