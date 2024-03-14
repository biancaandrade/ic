import random

NUM_AMOSTRAS = 30
NUM_ENTRADAS = 3
TAXA_APRENDIZAGEM = 0.01
NUM_TREINAMENTOS = 5
MAX_EPOCAS = 10000

# Função degrau bipolar, ajustei para u>=-5 para melhorar a convergência, com u>=0 as épocas chegavam ao limite 
def sinal(u):
    return 1.0 if u >= -5 else -1.0

# Função para exibir os pesos
def exibir_pesos(pesos):
    print("Pesos:", end=" ")
    for peso in pesos:
        print(peso, end=" ")
    print("\n")

# Função para validar o modelo
def validar_modelo(pesos, amostras_validacao):
    print("<< Executando Classificação >>")
    for amostra in range(10):
        u = 0.0

        # Cálculo do potencial de ativação
        for entrada in range(NUM_ENTRADAS):
            u += pesos[entrada] * amostras_validacao[amostra][entrada]

        u -= pesos[0]  # o bias está na posição pesos[0]

        # Função de ativação
        y = sinal(u)
        print(f"Amostra {amostra + 1}: Saída = {y}")

if __name__ == "__main__":
    conjunto_treinamento = [
        [-0.6508, 0.1097, 4.0009, -1],
        [-1.4492, 0.8896, 4.4005, -1],
        [2.0850, 0.6876, 12.0710, -1],
        [0.2626, 1.1476, 7.7985, 1],
        [0.6418, 1.0234, 7.0427, 1],
        [0.2569, 0.6730, 8.3265, -1],
        [1.1155, 0.6043, 7.4446, 1],
        [0.0914, 0.3399, 7.0677, -1],
        [0.0121, 0.5256, 4.6316, 1],
        [-0.0429, 0.4660, 5.4323, 1],
        [0.4340, 0.6870, 8.2287, -1],
        [0.2735, 1.0287, 7.1934, 1],
        [0.4839, 0.4851, 7.4850, -1],
        [0.4089, -0.1267, 5.5019, -1],
        [1.4391, 0.1614, 8.5843, -1],
        [-0.9115, -0.1973, 2.1962, -1],
        [0.3654, 1.0475, 7.4858, 1],
        [0.2144, 0.7515, 7.1699, 1],
        [0.2013, 1.0014, 6.5489, 1],
        [0.6483, 0.2183, 5.8991, 1],
        [-0.1147, 0.2242, 7.2435, -1],
        [-0.7970, 0.8795, 3.8762, 1],
        [-1.0625, 0.6366, 2.4707, 1],
        [0.5307, 0.1285, 5.6883, 1],
        [-1.2200, 0.7777, 1.7252, 1],
        [0.3957, 0.1076, 5.6623, -1],
        [-0.1013, 0.5989, 7.1812, -1],
        [2.4482, 0.9455, 11.2095, 1],
        [2.0149, 0.6192, 10.9263, -1],
        [0.2012, 0.2611, 5.4631, 1]
    ]

    amostras_validacao = [
        [-0.3665, 0.0620, 5.9891],
        [-0.7842, 1.1267, 5.5912],
        [0.3012, 0.5611, 5.8234],
        [0.7757, 1.0648, 8.0677],
        [0.1570, 0.8028, 6.3040],
        [-0.7014, 1.0316, 3.6005],
        [0.3748, 0.1536, 6.1537],
        [-0.6920, 0.9404, 4.4058],
        [-1.3970, 0.7141, 4.9263],
        [-1.8842, 0.2805, 1.2548]
    ]

    for treinamento in range(1, NUM_TREINAMENTOS + 1):
        print(f"\nTreinamento {treinamento}:\n")
        
        # Inicialização do vetor de pesos com valores aleatórios entre 0 e 1
        pesos = [random.random() for _ in range(NUM_ENTRADAS + 1)]
        
        print("Treinamento iniciado")
        exibir_pesos(pesos)
        epoca = 0

        # Loop sobre as amostras de treinamento
        while epoca < MAX_EPOCAS:
            erro = False

            for amostra in range(NUM_AMOSTRAS):
                u = 0.0

                # Cálculo do potencial de ativação
                for entrada in range(NUM_ENTRADAS):
                    u += pesos[entrada] * conjunto_treinamento[amostra][entrada]

                u -= pesos[0]  # Ajuste para incluir o bias

                # Aplicação da função de ativação
                y = sinal(u)

                # Verificação do erro
                if y != conjunto_treinamento[amostra][-1]:
                    # Atualização dos pesos
                    for entrada in range(NUM_ENTRADAS):
                        pesos[entrada] += TAXA_APRENDIZAGEM * (conjunto_treinamento[amostra][-1] - y) * conjunto_treinamento[amostra][entrada]

                    # Atualização do bias separadamente
                    pesos[0] += TAXA_APRENDIZAGEM * (conjunto_treinamento[amostra][-1] - y)
                    erro = True

            epoca += 1

            # Verificar convergência
            if not erro:
                print("Convergência alcançada. Parando o treinamento.\n")
                break

        # Exibir resultados do treinamento
        print(f"Treinamento concluído em {epoca} épocas.\n")
        exibir_pesos(pesos)

        # Validar o modelo usando amostras de validação
        validar_modelo(pesos, amostras_validacao)
