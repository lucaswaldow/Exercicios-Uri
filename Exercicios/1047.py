hi, mi, hf, mf = map(int, input().split())
if hi == hf:
    if mi==mf:
        hrs = 24
        min = 0
    elif mi<mf:
        min = mf-mi
        hrs = 0
    elif mi>mf:
        min = (60-mi)+mf
        hrs = 23
if hi < hf:
    hrs = hf - hi
    if mi<mf:
        min = mf-mi
    if mi>mf:
        hrs -= 1
        min = (60- mi)+mf
    if mi==mf:
        min = 0
if hi>hf:
    hrs = (24 - hi) + hf
    if mi==mf:
        min = 0
    if mi<mf:
        min = mf-mi
    if mi>mf:
        hrs -= 1
        min = (60- mi)+mf

print(f'O JOGO DUROU {hrs} HORA(S) E {min} MINUTO(S)')