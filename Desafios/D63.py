print("SEQUENCIA DE FIBONACCI")
n = int(input('Quantos termos você quer mostrar? '))
print(f"gerando sequência de fibonacci para {n} termos")
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
cont=3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    cont += 1
    t1 = t2
    t2 = t3
print('fim') 