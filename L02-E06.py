# Lista 02 - Exercício 06
# Faça um Programa que leia três números e mostre o maior deles.

primeiro_numero = int(input("Digite o primeiro número "))
segundo_numero = int(input("Digite o segundo número "))
terceiro_numero = int(input("Digite o terceiro número "))
maior_numero = 0

if primeiro_numero > segundo_numero:
    if primeiro_numero > terceiro_numero:
        maior_numero = primeiro_numero

    if primeiro_numero < terceiro_numero:
        maior_numero = terceiro_numero

if segundo_numero > primeiro_numero:
    if segundo_numero > terceiro_numero:
        maior = segundo_numero

    if segundo_numero < terceiro_numero:
        maior_numero = terceiro_numero

print(f"O Maior número de [{ primeiro_numero }, { segundo_numero }, { terceiro_numero }] é: { maior_numero }")
