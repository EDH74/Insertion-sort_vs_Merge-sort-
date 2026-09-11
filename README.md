# Análise de Desempenho: Insertion Sort vs Merge Sort

Este projeto realiza uma análise comparativa de desempenho entre os algoritmos de ordenação **Insertion Sort** e **Merge Sort**. O objetivo é medir e comparar o tempo que cada algoritmo leva para ordenar listas de diferentes tamanhos, simulando cenários práticos de uso.

## 🚀 Funcionalidades

O projeto avalia o tempo de execução de arrays com tamanhos variando de 1.000 a 16.000 elementos[cite: 2]. A análise é dividida em dois cenários principais para cada algoritmo:
*   **Cenário Aleatório:** Ordenação de listas geradas com números aleatórios[cite: 1, 3].
*   **Cenário de Pior Caso:** Ordenação de listas que foram previamente ordenadas em ordem decrescente[cite: 1, 3].

Além disso, o código implementa as seguintes técnicas para garantir relatórios precisos:
*   Uso da biblioteca `timeit` para a medição precisa do tempo de cada ordenação[cite: 1, 3].
*   Múltiplas execuções, onde a primeira execução é descartada do cálculo final, e o resultado é apresentado através da **mediana** dos tempos utilizando a biblioteca `statistics`[cite: 1, 3].
*   Uso de uma semente fixa (`random.seed(67)`) para garantir que os dados aleatórios gerados sejam sempre os mesmos, permitindo a reprodutibilidade exata dos testes[cite: 1, 3].
*   Arquitetura assíncrona utilizando `asyncio.to_thread` para que os relatórios rodem em threads separadas, não travando a execução principal do programa[cite: 2].

## 📂 Estrutura dos Arquivos

*   **`main.py`**: É o ponto de entrada principal do programa[cite: 2]. Ele coordena as execuções assíncronas chamando os relatórios tanto do Insertion Sort quanto do Merge Sort[cite: 2].
*   **`insertionSort.py`**: Contém a lógica de ordenação e geração de relatórios específicos para o algoritmo Insertion Sort[cite: 1].
*   **`mergeSort.py`**: Contém a implementação do algoritmo Merge Sort, utilizando o método de divisão e conquista, além de formatar a saída dos tempos com 15 casas decimais de precisão[cite: 3].

## 🛠️ Como Executar

Certifique-se de ter o Python instalado em sua máquina. Para rodar a análise, basta executar o arquivo principal no seu terminal:

```bash
python main.py
```

No proprio _main.py_ pode ser alterado usando o array que desejar