idade = homem = mm = 0
while True:
    sexo = input('qual o sexo da pessoa? [H/M] H -> HOMEM M -> MULHER ').strip().upper()
    id = int(input('e qual a idade? '))
    if id >= 18:
        idade += 1
    if sexo in 'hH':
        homem += 1
    else:
        if id < 20:
            mm += 1
    cont = input('deseja continuar? [S/N]').strip().upper()
    if cont in 'sS':
        print('-'*20, ' cadastre uma nova pessoa', '-'*20)
    else:
        break
print(f'foram registrados {idade} pessoas maiores de 18 anos')
print(f'foram cadastrados {homem} homens.')
print(f'foram registradas {mm} mulheres menores que 20 anos')
