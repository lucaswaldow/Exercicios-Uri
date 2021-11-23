i = 0
j = 1
while i <= 2:
    valorInt = i-int(i)
    if valorInt == 0:
        for x in range(3):
            print(f'I={int(i)} J={int(j)}')
            j += 1
    else:
        for x in range(3):
            print(f'I={i:.1f} J={j:.1f}')
            j += 1
    i = round(i,1)+0.2
    j = 1 + i