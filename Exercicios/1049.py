tp1 = input()
tp2 = input()
tp3 = input()
if tp1 == 'vertebrado':
    if tp2 == 'ave':
        if tp3 == 'carnivoro':
            print('aguia')
        elif tp3 == 'onivoro':
            print('pomba')
    elif tp2 == 'mamifero':
        if tp3 == 'onivoro':
            print('homem')
        elif tp3 == 'herbivoro':
            print('vaca')
elif tp1 == 'invertebrado':
    if tp2 == 'inseto':
        if tp3 == 'hematofago':
            print('pulga')
        elif tp3 == 'herbivoro':
            print('lagarta')
    elif tp2 == 'anelideo':
        if tp3 == 'hematofago':
            print('sanguessuga')
        elif tp3 == 'onivoro':
            print('minhoca')
