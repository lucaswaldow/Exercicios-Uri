cmp = 0
for x in range(1,101):
    valor = int(input())
    if valor > cmp:
        mV = valor
        posicao = x
        cmp = valor
print(mV)
print(posicao)