renda = float(input())

if renda <= 2000.00:
    ip = 0
    print('Isento')

if 2000.00 < renda <= 3000.00:
    rnd8 = renda - 2000.00
    ip = rnd8 * 0.08

if 3000.00 < renda <= 4500.00:
    ip8 = 0.08 * 1000.00
    rnd18 = renda - 3000.00
    ip = rnd18 * 0.18 + ip8

if renda > 4500.00:
    ip8 = 0.08 * 1000.00
    ip18 = 0.18 * 1500.00
    r28 = renda - 4500.00
    ip = ip18 + ip8 + r28 * 0.28

if renda > 2000.00:
    ip = float(ip)
    print(f'R$ {ip:.2f}')