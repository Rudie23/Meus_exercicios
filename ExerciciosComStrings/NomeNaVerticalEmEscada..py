"""
Nome na vertical em escada.
Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

s = 'FULANO'
tamanho = len(s)

for linha in range(tamanho):
    print(s[:linha + 1])
