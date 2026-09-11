import random
import timeit
import statistics

random.seed(67)



def tracin(n):
    print("="*n)

def mergeSort(data):
  
    #print "call: " + str(calls)
    #print str(data) + "\n"

    # a 1 element list is the base case, so we stop the recursion
    if len(data) > 1:

        # otherwise, keep splitting the list into two halves
        mid = len(data) // 2
        leftHalf = data[:mid]
        rightHalf = data[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        # setting up our index pointers, one for each half and
        # one for the data that this call is rearranging
        leftIndex=0
        rightIndex=0
        dataIndex=0

        # while there's elements in both left and right halves, that haven't been
        # put back into the data list
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):

            # if the next element in the left half is smaller than that on the right,
            # put that element in the next space within the data list
            if leftHalf[leftIndex] < rightHalf[rightIndex]:
                data[dataIndex]=leftHalf[leftIndex]
                leftIndex=leftIndex+1

            # otherwise put the next element from the right half into the next space
            # in the data list
            else:
                data[dataIndex]=rightHalf[rightIndex]
                rightIndex=rightIndex+1
            dataIndex=dataIndex+1

        # if all the elements from the right half have been used, this ensures
        # the remaining elements from the left make it back into the data list
        while leftIndex < len(leftHalf):
            data[dataIndex]=leftHalf[leftIndex]
            leftIndex=leftIndex+1
            dataIndex=dataIndex+1

        # this does the same as above, but for when the left half is exhausted
        # and there's still unused elements in the right
        while rightIndex < len(rightHalf):
            data[dataIndex]=rightHalf[rightIndex]
            rightIndex=rightIndex+1
            dataIndex=dataIndex+1




def gerarTempoMerge(cenario=0, listaExec=None):
    arr = []
    tempo = {}
 
    if cenario == 0:
        for i in listaExec:
            for _ in range(i):    
                arr.append(random.randrange(i))
                
            tempo[i] = timeit.timeit(lambda: mergeSort(arr), number=1)
            arr.clear()
            
            
    elif cenario == 1:
        for i in listaExec:
            for _ in range(i):
                arr.append(random.randrange(i))
            
            arr.sort(reverse=True)

            tempo[i] = timeit.timeit(lambda: mergeSort(arr), number=1)
            arr.clear()
    
    else:
        raise ValueError("Valor passado no cenario/Lista de Array invalido!")
            
            
    return tempo


def relatorioPorCenario(cenarioPassado=0, qntArray=[1000, 2000, 4000, 8000, 16000]):
    """
    Caso seja cenario 0 ele gera um Insertion sort com os dados aleatorios
    caso seja Cenario 1 ele gera um Insertion sort com os dados ordenador
    foi seta uma seed como 67 para nao haver interferencia na resposta
    """
    

    soma = {}

    tempos = gerarTempoMerge(cenarioPassado, qntArray)
    for i in range(4):
        
        if i == 0:
            for e in tempos.keys():
                soma[e] = []
        
        print(f"Merge Sort execucao aleatorio: {i+1}")
        for timers in tempos:
            print(f"{timers} | {tempos[timers]:.15f}")
            if i > 0:
                soma[timers].append(tempos[timers])
        print()
        
       
        
            
    #Relatorio da mediana
    print()
    medianaList = {}

    for i in soma:
        medianaList[i] = statistics.median(soma[i])
        

    
    tipo = "mediana lista ordenada no pior caso" if cenarioPassado == 1 else "Mediana lista com entrada aleatoria"
    tracin(50)
    print()
    print(tipo)
    print()
    tracin(50)
    for i in medianaList:
        print(f"{i} | {medianaList[i]:.15f}", sep="    ")



'''
alist = [54,26,500,93,17,77,31,44,55,20, 200]
calls = mergeSort(alist)
print(alist, calls)
'''