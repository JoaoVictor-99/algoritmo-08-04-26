# 1. Definindo os valores iniciais
mesada = 200
gastos = [50, 30, 45, 20, 10]

# 2. Criando o acumulador
total_gasto = 0

# 3. Percorrendo a lista "na mão"
# Para cada 'valor' dentro da lista 'gastos'...
for valor in gastos:
    total_gasto = total_gasto + valor
    # O computador faz: total antigo + novo valor = novo total

# 4. Mostrando o resultado
print("João gastou um total de: R$", total_gasto)

# 5. A lógica da decisão (O balanço)
if total_gasto < mesada:
    sobra = mesada - total_gasto
    print("Boa! Sobrou dinheiro. Você ainda tem R$", sobra)

elif total_gasto > mesada:
    falta = total_gasto - mesada
    print("Cuidado! Você gastou R$", falta, "a mais do que podia.")

else:
    print("Você gastou exatamente o que tinha. Cuidado para não ficar no negativo!"