ndex = int(input())
qntin = 0
qntout = 0
for i in range(ndex):
    num = int(input())
    if 10<=num<=20:
        qntin += 1
    else:
        qntout += 1
print(f'{qntin} in')
print(f'{qntout} out')