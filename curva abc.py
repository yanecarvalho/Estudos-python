def calcular_acuracia_estoque(estoque_físico, estoque_lógico):
    divergencia = estoque_físico - estoque_lógico / estoque_lógico * 100
    acuracia = (estoque_lógico / estoque_físico) * 100
    return acuracia, divergencia


estoque_físico = int(input("Informe o estoque físico: "))
estoque_lógico = int(input("Informe o estoque lógico: "))


acuracia, divergencia = calcular_acuracia_estoque(estoque_físico, estoque_lógico)

# Exibição dos resultados
print("Divergência:", divergencia)
print("Acurácia do estoque:", acuracia, "%")