n_desejado=int(input("Quantos numeros perfeitos voce encontrar: "))
encontrados = 0
numeros_testados = 2 #Começamos do 2 (1 não é perfeito)
print(f"Buscando os {n_desejado} primeiros numeros perfeitos")
while encontrados < n_desejado:
    soma_divisores = 0
    #Encontra os divisores do 'numero_testado'
    for i in range(1, numeros_testados):
        if numeros_testados % i == 0:
            soma_divisores += i

# verificar se a soma é igual ao numero
if soma_divisores == numeros_testados:
    encontrados += 1
    print(f"{encontrados}. numero perfeito encontrado!")

    numeros_testados += 1