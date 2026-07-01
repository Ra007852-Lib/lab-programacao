#Exercicio Filtro Notas
#deve guardar informação num vetor quando a atividade envolve vetores

notas = []
for i in range(5):
    nota = float(input(f"Digite a nota do aluno{i+1}")) #i+1 é necessario para não contar o numero 0
    notas.append(nota)

menor_nota = min(notas) #min serve para descobrir qual o menor valor
notas.remove(menor_nota) #remove remove o elemento de notas
print(f"A menor nota removida foi: {menor_nota}")

print(f"Notas que restaram no sistema: {notas}")
