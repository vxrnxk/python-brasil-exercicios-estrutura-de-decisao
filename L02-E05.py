# Lista 02 - Exercício 05
'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
a) A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
b) A mensagem "Reprovado", se a média for menor do que sete;
c) A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

primeira_nota = int(input("Digite a primeira nota: "))
segunda_nota = int(input("Digite a segunda nota: "))

media = (primeira_nota + segunda_nota) / 2

if media >= 7:
    if media == 10:
        print("APROVADO COM DISTINÇÃO")
    else:
        print("APROVADO")

if media < 7:
    print("REPROVADO")

print(f"COM MÉDIA: { media }")
