"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120"""

numero = int(input('Digite o fatorial que deseja obter: '))
fatorial = 1
i = 1
while i in range(1, numero + 1):
    fatorial = fatorial * i
    i =< fatorial
    print(fatorial, end=' ')