import matplotlib.pyplot as plt

# Dados do eixo X (Tamanhos do array)
tamanhos = [1000, 2000, 4000, 8000, 16000]

# Dados do eixo Y (Tempos extraídos do seu terminal)
merge_pior = [0.0009, 0.0025, 0.0050, 0.0102, 0.0250]
merge_aleatorio = [0.0015, 0.0024, 0.0055, 0.0120, 0.0277]

insertion_pior = [0.0294, 0.1186, 0.4977, 2.0613, 8.8026]
insertion_aleatorio = [0.0150, 0.0591, 0.2479, 0.9927, 4.0643]

# Configurando o gráfico
plt.figure(figsize=(10, 6))

plt.plot(tamanhos, insertion_pior, label='Insertion Sort (Pior Caso)', marker='o', color='red', linestyle='--')
plt.plot(tamanhos, insertion_aleatorio, label='Insertion Sort (Aleatório)', marker='o', color='orange')

plt.plot(tamanhos, merge_aleatorio, label='Merge Sort (Aleatório)', marker='s', color='blue')
plt.plot(tamanhos, merge_pior, label='Merge Sort (Pior Caso)', marker='s', color='cyan', linestyle='--')

plt.title('Comparação de Desempenho: Insertion Sort vs Merge Sort')
plt.xlabel('Tamanho do Array (N)')
plt.ylabel('Tempo em Segundos (Mediana)')
plt.legend()
plt.grid(True)
plt.yscale('log')

# SALVA A IMAGEM DIRETO NA SUA PASTA
plt.savefig('grafico_comparativo.png', dpi=300, bbox_inches='tight')
print("Tudo certo! Imagem 'grafico_comparativo.png' salva com sucesso na sua pasta.")

#Essa parte eu fiz com IA
