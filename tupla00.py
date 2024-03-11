#npe= numero por extenso [0 ate 20]
n=''
npe = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis','sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
print('-'*30, ' BEM VINDO AO POR EXTENSO ', '-'*30)
while True:
    c=int(input('digite um numero de zero a 20: '))
    if 0 <= c <= 20:
        print(f'o numero {c} por extenso se inscreve {npe[c]}')
        i = str(input('deseja continuar:[S/N]->  ')).strip().upper()
        if i in 'Nn':
            break
        else:
            print('-'*10, ' continuando', '-'*10)

print('fim do programa')
