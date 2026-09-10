import random
import timeit


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

qntArray = [1000, 2000, 4000, 8000, 16000]

arr = []
tempo = {}

for i in qntArray:
    for e in range(i):
        arr.append(random.randrange(i))
    
    tempo[i] = timeit.timeit(lambda: insertion_sort(arr), number=100)
    arr.clear()

print(tempo)
