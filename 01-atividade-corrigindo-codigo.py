"""
1. A quantidade de números pares e ímpares.
2. A quantidade de números positivos e negativos.
3. A quantidade de números inseridos.
4. O maior e o menor número.
5. A média de números pares.
6. A média de números ímpares.
7. A média de todos os números inseridos.
8. Mostrar os números lidos na ordem inversa.

"""
import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
lista_numeros = []

# Variáveis para armazenar os números
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numeros.append(numero)

# Processando cada número
def verificar_pares_impares(a):
    lista_pares = []
    lista_impares = []
    for numero in a:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)
    return lista_pares, lista_impares

def verificar_positivos_negativos(a):
    lista_positivos = []
    lista_negativos = []
    for numero in a:
        if numero > 0:
            lista_positivos.append(numero)
        else:
            lista_negativos.append(numero)   
    return lista_positivos, lista_negativos

def calcular_media(a):
    quantidade_de_numeros = len(a)

    if quantidade_de_numeros != 0:
        soma = sum(a)
        media = soma / quantidade_de_numeros
        return media
    else:
        return 0
         
lista_pares, lista_impares = verificar_pares_impares(lista_numeros)
lista_positivos, lista_negativos = verificar_positivos_negativos(lista_numeros)        
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)
quantidade_pares = len(lista_pares) 
quantidade_impares = len(lista_impares)
quantidade_positivos = len(lista_positivos)
quantidade_negativos = len(lista_negativos)
media_total = calcular_media(lista_numeros)
media_dos_pares = calcular_media(lista_pares)
media_dos_impares = calcular_media(lista_impares)

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de números inseridos: {QUANTIDADE_NUMEROS}")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_dos_pares:.2f}")
print(f"Média dos números ímpares: {media_dos_impares:.2f}")
print(f"Média de todos os números: {media_total:.2f}")
for i, numero in enumerate(reversed(lista_numeros)):
    print(f"{len(lista_numeros) - i}º número inserido: {numero}")