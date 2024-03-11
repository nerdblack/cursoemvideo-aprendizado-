n=int(input('digite um numero: '))
c=n
fatorial=1
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c>1 else '=', end=' ')
    fatorial *= c
    if c==1:
        print(fatorial)
    c-=1