import pandas as pd


def criarPlanilha():

    dados = {
        "Tamanhos da Lista" : [1000, 2000, 4000, 8000, 16000],
        "Merge Sort - Pior Caso": [0.001030, 0.002088, 0.004885, 0.013063, 0.026871],
        "Merge Sort - Aleatorio": [0.001231, 0.002625, 0.007940, 0.015951, 0.035368],
        "Insertion Sort - Pior Caso": [0.031937, 0.134901, 0.540226, 2.197111, 9.746035],
        "Insertion Sort - Aleatorio": [0.016562, 0.066819, 0.266424, 1.079927, 4.452841]
    }

    criarPlanilha = pd.DataFrame(dados)
    
    nomeArquivo = "relatorio.xlsx"
    criarPlanilha.to_excel(nomeArquivo, index=False)
    
    print(f"Planilha '{nomeArquivo}' criada com sucesso!")
    

criarPlanilha()

    
    