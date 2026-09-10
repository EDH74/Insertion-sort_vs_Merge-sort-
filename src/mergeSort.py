import random
import timeit

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




qntArray = [1000, 2000, 4000, 8000, 16000]

arr = []
tempo = {}

for i in qntArray:
    for e in range(i):
        arr.append(random.randrange(i))
    
    tempo[i] = timeit.timeit(lambda: mergeSort(arr.copy()), number=100)
    arr.clear()

print(tempo)

'''
alist = [54,26,500,93,17,77,31,44,55,20, 200]
calls = mergeSort(alist)
print(alist, calls)
'''