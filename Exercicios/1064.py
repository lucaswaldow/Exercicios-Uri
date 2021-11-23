nump = 0
qntp = 0
for x in range(1,7):
    num = float(input())
    if num>0:
        nump += num
        qntp += 1
media = nump/qntp
print(f'{qntp} valores positivos')
print(f'{media:.1f}')