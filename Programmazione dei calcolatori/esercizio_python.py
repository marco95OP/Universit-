a = ['uno', 'due', 'sei', 'due', 'zero', 'nove']
n = len(a)

m = 4

for i in range(m):
    x = input('digita qualcosa: ')
    c = 0
    z = a.index(x)

    for y in a:
        if x == y:
            c += 1
    print(f'La stringa {x} compare {c} volte in posizione {z}')
