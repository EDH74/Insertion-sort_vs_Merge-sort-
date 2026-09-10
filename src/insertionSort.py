import random
import timeit
import statistics

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key




def execucao(listaExec):
    arr = []
    tempo = {}
    random.seed(67)

    for i in qntArray:
        for e in range(i):
            arr.append(random.randrange(i))
        
        tempo[i] = timeit.timeit(lambda: insertion_sort(arr), number=3)
        arr.clear()
        
        
    return tempo


qntArray = [1000, 2000, 4000, 8000, 16000]

soma = {}

for i in range(4):
    tempos = execucao(qntArray)
    
    if i == 0:
        print("Primeira execucao descartada do calculo da mediana")
        for i in tempos.keys():
            soma[i] = []
    
    print(f"Insertion Sort execucao {i+1}")
    for timers in tempos:
        print(f"{timers} | {tempos[timers]}")
        if i > 1:
            soma[timers].append(tempos[timers])
    print()
    
        
print("=" *30)


medianaList = []

for i in soma:
    medianaList.append(statistics.median(soma[i])) 
    
print(medianaList)


