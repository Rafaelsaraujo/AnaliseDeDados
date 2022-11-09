try:
    teste = int(input('Inserir valor: '))
    print(teste)

except ValueError:
    print('Msg do programador: DEMENTE! Bota um número nessa caceta')

else:
    print('Valor admissível. Código seguirá normalmente')
