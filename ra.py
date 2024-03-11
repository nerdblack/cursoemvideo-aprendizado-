p = int(input('digite o primeiro termo da pa: '))
r = int(input('digite a razão: '))
pa = 0
c = 0
print('com o primeiro termo sendo {} e a razão sendo {}, temos como os primeiros 10 termos: '.format(p, r))
n = p
total=0
mais=10
while mais!=0:
    total=total+mais
    while pa != total:
        print('{} ->'.format(n), end=' ')
        n += r
        pa += 1
    print(' pausa')
    mais=int(input('deseja ver mais quantos termos:'))


