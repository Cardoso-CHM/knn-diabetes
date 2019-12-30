import numpy as np

def euc(test_id,train_id): 
    # considere o objeto de teste (data[test_id]) como "a" e o objeto de treino (data[train_id]) como "b"
    a = data[test_id]
    b = data[train_id]
    
    return np.linalg.norm(a-b)

def kNN(n):
    true_positives = 0 #pessoas classificadas diabeticas que realmente sao diabeticas ( classificou 1 e é 1)
    true_negatives = 0 #pessoas classificadas nao diabeticas que realmente nao sao diabeticas (classificou 0 e é 0)
    false_positives = 0#pessoas classificadas diabeticas que nao sao diabeticas (classificou 1 e é 0)
    false_negatives = 0#pessoas classificadas nao diabeticas que sao diabeticas (classificou 0 e é 1)
    
    for x in test_ids:
        aux = np.zeros((len(train_ids),3))#criando matriz de "quantidade de ids de treino" linhas e 3 colunas, a primeira sera a similaridade do cosseno entre o obj de traino e o de teste, a segunda o id do obj de treino e a terceira a classe real do objeto de treino
        for j,y in enumerate(train_ids):
            aux[j][0] = euc(x,y)
            aux[j][1] = y
            aux[j][2] = classes[y]
            
        aux = aux[aux[:,0].argsort()][:n] #aplicando agsort (aux[aux[:,0].argsort()]) e pegando os n prirmeiros objetos ([:n])
        
        if sum(aux[:,2]) > (n - sum(aux[:,2])):# verificando qual a classe mais predominante entre os n vizinhos mais proximos do obj x (obs: n deve ser um numero impar!)
            #se entrar aqui é por que a classe predominante é 1
            if classes[x] == 1:
                true_positives +=1 #classificou certo
            elif classes[x] == 0:
                false_positives +=1#classificou errado
        else:
            #se entrar aqui é por que a classe predominante é 0
            if classes[x] == 0:
                true_negatives +=1#classificou certo
            elif classes[x] == 1:
                false_negatives +=1#classificou errado
    result = np.array([true_positives,true_negatives,false_positives,false_negatives])
    return result

matrix = np.loadtxt("Diabetes-data.txt",delimiter=',') #lendo dados do arquivo txt

data,classes = matrix[:,:-1] , matrix[:, -1] #separando as classes da matriz e colocando num vetor chamado "classes"

min_max = np.matrix([np.min(data,axis = 0),np.max(data,axis = 0)]).astype(int) #pegando o maior e menor valor de cada coluna e colocando numa matriz [2,n] onde n é o numero de atributos

data = np.array((data[:,:] - min_max[0, :])/ (min_max[1,:] - min_max[0,:])) #aplicando tratamento de dados min-max (normalizacao)

#lendo id dos objetos de teste e de treino de arquivo txt
test_ids = np.loadtxt("test-data.txt").astype(int)
train_ids = np.loadtxt("train-data.txt").astype(int)

while True:
    n = input("Digite a quantidade de vizinhos que serão analisados (digite 0 para finalizar o programa): ")
    n = int(n)
    if n == 0:  break
    res = kNN(int(n))
    print("\nTrue Positives:",res[0])
    print("True Negatives:",res[1])
    print("False Positives:",res[2])
    print("False Negatives:",res[3])
    acc =  ((res[0] + res[1])/len(test_ids)) * 100
    sens= res[0]/(res[0] + res[3])
    prec= res[0]/(res[0] + res[2])
    medF = 2*sens*prec/(sens+prec)
    print("\nAccuracy: %.2f" %acc,"%")
    print("Sensitivity: %.2f" %(sens*100) ,"%")
    print("Specificity: %.2f" %((res[1]/(res[1] + res[2]))*100), "%")
    print("Precision: %.2f" %(medF*100), "%")
    print("Measure F: %.2f" %(prec*100), "%")