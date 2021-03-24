sexo = str(input('Informe seu sexo: [M/F] '))
while sexo not in 'MmFf':
    sexo = str(input('Datdos inválidos. Por favor, Informe seu sexo: [M/F] ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sexo))