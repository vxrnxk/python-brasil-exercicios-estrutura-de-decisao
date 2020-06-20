# Lista 02 - Exercício 04
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ("a", "e", "i", "o", "u")
letra = input("Digite uma letra: ").lower()

if letra in vogais:
    print("É vogal")

else:
    print("É consoante")
