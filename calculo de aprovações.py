cabecalho = "Cálculo de aprovações e reprovações"

nome = (input("Digite o nome do aluno: "))
turma = int(input("Digite o número da turma: "))
qtde_faltas = float(input("Digite a quantidade de faltas do aluno: "))
nota_teste = float(input("Digite a nota do teste: "))
nota_prova = float(input("Digite a nota da prova: "))
media = (nota_prova + nota_teste) /2

if qtde_faltas <= 5 and media >= 7:
    print("Aluno aprovado!")

elif qtde_faltas <=6 and media <= 6:
    print("Aluno precisa fazer recuperação!")

else:
    print("Aluno reprovado!")

