from random import randint
nv = 0
while True:
    computador = randint(0,10)
    escolha = str(input(' escolha impar ou par? ')).strip().upper()
    num = int(input('agora jogue um numero'))
    soma = num + computador
    print( f' o resultado foi... {soma}')
    ip= soma%2
    if escolha == 'IMPAR':
        if ip == 0:
            print('esse numero é par')
            print('voce perdeu!!')
            break
        else:
            print('o numero é impar')
            print('voce ganhou!!')
            nv += 1
    if escolha == 'PAR':
        if ip == 0:
            print('esse numero é par')
            print('voce ganhou!!')
            nv += 1
        else:
            print('o numero é impar')
            print('voce perdeu!!')
            break
print(f'voce teve {nv} vitorias antes de perder')