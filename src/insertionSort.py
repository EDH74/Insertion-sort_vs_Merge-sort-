import random
import timeit
import statistics

def tracin(mult:int):
    print("=" * mult)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key



random.seed(67)

def execucao(listaExec, cenario=0):
    arr = []
    tempo = {}

    if cenario == 0:
        for i in listaExec:
            for _ in range(i):    
                arr.append(random.randrange(i))
                
            tempo[i] = timeit.timeit(lambda: insertion_sort(arr), number=1)
            arr.clear()
            
            
    elif cenario == 1:
        for i in listaExec:
            for _ in range(i):
                arr.append(random.randrange(i))
            
            arr.sort(reverse=True)
            tempo[i] = timeit.timeit(lambda: insertion_sort(arr), number=1)
            arr.clear()
    
    else:
        raise ValueError("Valor passado no cenario invalido!")
        
        
    return tempo



def relatorioPorCenario(cenarioPassado=0, qntArray=[1000, 2000, 4000, 8000, 16000]):
    #script que gera os dados

    soma = {}

    """
    Caso seja cenario 0 ele gera um Insertion sort com os dados aleatorios
    caso seja Cenario 1 ele gera um Insertion sort com os dados ordenador
    foi seta uma seed como 67 para nao haver interferencia na resposta
    """
    for i in range(4):
        tempos = execucao(qntArray, cenarioPassado)
        
        if i == 0:
            print("Primeira execucao descartada do calculo da mediana")
            for e in tempos.keys():
                soma[e] = []
        
        print(f"Insertion Sort execucao aleatorio: {i+1}")
        for timers in tempos:
            print(f"{timers} | {tempos[timers]}")
            if i > 0:
                soma[timers].append(tempos[timers])
        print()
        
            
    #Relatorio da mediana
    medianaList = {}

    for i in soma:
        medianaList[i] = statistics.median(soma[i])
        

    tracin(50)
    tipo = "mediana lista ordenada no pior caso" if cenarioPassado == 1 else "Mediana lista com entrada aleatoria"
    print(tipo)
    tracin(50)
    print()
    for i in medianaList:
        print(f"{i} | {medianaList[i]}", sep="    ")
