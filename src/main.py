import asyncio
import insertionSort
import mergeSort

largeArray = [10000, 20000, 40000, 80000, 160000]  #Esse array demora para dedeu
defaulArray = [1000, 2000, 4000, 8000, 16000]  #Array Usado para gerar os relatórios, pois é mais rápido e não trava o programa


#Funções assíncronas para isolar cada bloco de relatório
async def gerar_relatorio_insertion():
    print()
    print()
    print()
    print()
    print("\n" + "="*50)
    print("Relatório Insertion Sort")
    
    insertionSort.tracin(50)
    print("Relatório com entrada ordenada no pior caso")
    insertionSort.tracin(50)
    # Roda a função síncrona em uma thread separada sem travar o loop de eventos
    await asyncio.to_thread(insertionSort.relatorioPorCenario, 1, defaulArray)

    insertionSort.tracin(50)
    print("Relatório com entrada aleatória")
    insertionSort.tracin(50)
    await asyncio.to_thread(insertionSort.relatorioPorCenario, 0, defaulArray)


async def gerar_relatorio_merge():
    print()
    print()
    print()
    print()
    print("\n" + "="*50)
    print("Relatório Merge Sort")
    
    mergeSort.tracin(50)
    print("Relatório com entrada ordenada no pior caso")
    mergeSort.tracin(50)
    await asyncio.to_thread(mergeSort.relatorioPorCenario, 1, defaulArray)

    mergeSort.tracin(50)
    print("Relatório com entrada aleatória")
    mergeSort.tracin(50)
    await asyncio.to_thread(mergeSort.relatorioPorCenario, 0, defaulArray)



async def main():
    print('\033c', end='')
    await gerar_relatorio_merge()
    await gerar_relatorio_insertion()

 

#Ponto de entrada do programa
if __name__ == "__main__":
    asyncio.run(main())