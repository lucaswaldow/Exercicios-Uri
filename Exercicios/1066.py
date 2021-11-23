'''a = []
for i in range(5):
    n = int(input())
    a.append(int(n))'''
qntpar = 0
qntimp = 0
qntp = 0
qntn = 0
for x in range(5):
    num = int(input())
    if num%2==0:
        qntpar += 1
    if num%2!=0:
        qntimp += 1
    if num>0:
        qntp += 1
    if num<0:
        qntn += 1
print(f'{qntpar} valor(es) par(es)')
print(f'{qntimp} valor(es) impar(es)')
print(f'{qntp} valor(es) positivo(s)')
print(f'{qntn} valor(es) negativo(s)')