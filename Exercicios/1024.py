qntvezes = int(input())
qnt = qntvezes
while qnt>0 :
    qnt -= 1
    frase = input()
    temp = ''
    for l in frase:
        if l.isalpha():
            temp += chr(ord(l) +3)
        else:
            temp += l
    temp = temp[::-1]
    metade = int(len(temp)/2)
    cryp = temp[:metade]
    for i in temp[metade:]:
        cryp += chr(ord(i) - 1)
    print(cryp)