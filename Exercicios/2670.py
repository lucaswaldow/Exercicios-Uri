a1 = int(input())
a2 = int(input())
a3 = int(input())
andar1 = a2*2 + a3*4    #1 andar = 1x0 2x2 3x4
andar2 = a1*2 + a3*2    #2 andar = 1x2 2x0 3x2
andar3 = a1*4 + a2*2    #3 andar = 1x4 2x2 3x0
if andar2>=andar1<=andar3:
    print(andar1)
elif andar1>=andar2<=andar3:
    print(andar2)
elif andar1>=andar3<=andar2:
    print(andar3)