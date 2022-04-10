#Banco de dados
sorteios = ((4,5,30,33,41,52),(9,37,39,41,43,49),(10,11,29,30,36,47),(1,5,6,27,42,59),(1,2,6,16,19,46),(7,13,19,22,40,47),(3,5,20,21,38,56),(4,17,37,38,47,53),(8,43,44,55,56,60),(4,18,21,25,38,57),(15,25,37,38,58,59),(4,16,19,20,27,43),(18,32,47,50,54,56),(2,16,23,27,47,53),(12,33,35,51,52,60),(20,32,34,49,58,60),(6,10,13,19,20,51),(23,27,36,37,42,56),(5,10,12,24,25,60),(11,25,28,30,33,51),(6,33,36,46,49,53),(1,9,31,38,46,56),(17,37,39,51,52,59),(1,8,14,28,33,43),(24,43,50,54,55,56),(10,22,50,53,57,58),(13,17,20,33,44,51),(3,6,22,24,54,60),(3,8,14,43,56,58),(7,14,15,29,38,50),(17,19,28,45,48,56),(5,14,33,36,43,44),(5,17,33,39,42,49),(13,15,17,40,53,57),(4,16,21,23,54,57),(3,13,17,25,29,51),(6,7,22,38,52,60),(10,42,43,45,54,55),(12,16,37,45,52,56),(3,5,8,12,46,47),(12,26,35,38,39,47),(7,11,19,24,33,36),(2,6,17,25,26,58),(14,18,29,38,44,47),(7,30,37,44,53,55),(1,23,24,32,46,60),(3,17,25,35,48,56),(2,5,28,34,47,50),(7,13,33,35,43,55),(6,16,21,44,57,58))

#Função que contém o algoritmo detector de duplicatas
def compara (lista):
    flag = 0
    for i in range(0, len(lista)):
        for j in range(i, len(lista)):
            if i == j:
                pass
            else:
                if lista[i] == lista[j]:
                    print("Os sorteios",i+1,"e",j+1,"são iguais.")
                    flag = 1
    if flag == 0:
        print("Não há sorteios com resultados idênticos até este momento.")

#Função que contém o algoritmo detector de ocorrências
def find_number(inteiro, lista):
    counter = 0
    for i in range(0, len(lista)):
        if inteiro in lista[i]:
            print("O número",inteiro,"aparece no sorteio",i+1,".")
            counter = counter + 1
    print("O número",inteiro,"aparece em",counter,"sorteios.")
 
#Função que imprime os resultados dos sorteios que estão no banco de dados
def resultado(inteiro_1, inteiro_2 ,lista):
    for i in range(inteiro_1,inteiro_2+1):
        print("Resultado do sorteio nº",i+1,lista[i])
  
#Programa principal
print("Digite uma das opções abaixo:\n1) Verificar duplicatas de sorteios.\n2) Verificar a ocorrência de uma determinada dezena.\n3) Resultados da mega-sena em um intervalo de sorteios dado.")
choice = input("Digite a opção desejada: ")
if choice == "1":
    compara(sorteios)
if choice == "2":
    dezena = int(input("Digite a dezena: "))
    find_number(dezena,sorteios)
if choice == "3":
    print("No banco de dados há", len(sorteios),"sorteios. Selecione o intervalo:")
    inferior = int(input("Digite o número do sorteio mais antigo: "))
    superior = int(input("Digite o número do sorteio mais recente: "))
    resultado(inferior-1,superior-1,sorteios)
\\ esse texto está salvo?
    

