algo = input('Digite algo: ')
print(f'Você digitou "{algo}" e eu descobri essas informações acerca disso: ')
print(f'Tipo: {type(algo)}')
print(f'É numérico? {algo.isnumeric()}')
print(f'TUDO MAIÚSCULO? {algo.isupper()}')
print(f'É Decimal? {algo.isdecimal()}')