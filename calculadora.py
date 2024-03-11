n1=int(input('digite um valor: '))
n2=int(input('digite mais um valor: '))
while True:
    print('-='*30)
    print('OPERAÇÕES:\n[1]  SOMA\n[2]  SUBTRAÇÃO\n[3]  MULTIPLICAÇÃO\n[4]  DIVISÃO\n[5]  NOVOS VALORES\n[6]  SAIR')
    esc = int(input('escolha uma operação: '))
    if esc == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}\n')
    elif esc == 2:
        sub = n1 - n2
        print(f'{n1} - {n2} = {sub}\n')
    elif esc == 3:
        mult = n1 * n2
        print(f'{n1} x {n2} = {mult}\n')
    elif esc == 4:
        div = n1 / n2
        print(f' {n1} / {n2} = {div:.2f}\n')
    elif esc == 5:
        n1 = int(input('digite um valor: '))
        n2 = int(input('digite mais um valor: '))
        print('novos valores foram adicionados \n')
    else:
        print('fim do programa')
        break
