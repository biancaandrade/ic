import numpy as np
import random

NUM_ENTRADAS = 3
TAXA_APRENDIZAGEM = 0.01
NUM_TREINAMENTOS = 5
MAX_EPOCAS = 10000

# Função degrau bipolar
def sinal(u):
    return 1.0 if u >= -5 else -1.0

# Função para exibir os pesos
def exibir_pesos(pesos):
    print("Pesos:", pesos, "\n")

# Função para validar o modelo
def validar_modelo(pesos, conjunto_validação):
    print("<< Executando Classificação >>")
    
    for amostra in range(len(conjunto_validação)):
        u = 0.0

        # Cálculo do potencial de ativação
        for entrada in range(NUM_ENTRADAS):
            u += pesos[entrada] * conjunto_validação[amostra][entrada]

        u -= pesos[0]  # o bias está na posição pesos[0]

        # Função de ativação
        y = sinal(u)
        print(f"Amostra {amostra + 1}: Saída = {y:.6f}")

# Carregar os conjuntos de treinamento e validação
conjunto_treinamento = np.loadtxt('dados/conjunto_treinamento.txt', dtype=float)
conjunto_validação = np.loadtxt('dados/conjunto_validação.txt', dtype=float)

# Loop para executar cinco treinamentos
for treinamento in range(1, NUM_TREINAMENTOS + 1):
    print(f"\nTreinamento {treinamento}:\n")

    # Inicialização do vetor de pesos com valores aleatórios entre 0 e 1
    pesos = np.random.rand(NUM_ENTRADAS + 1)

    print("Treinamento iniciado")
    exibir_pesos(pesos)
    epoca = 0

    # Loop sobre as épocas
    while epoca < MAX_EPOCAS:
        erro = False

        # Loop sobre as amostras de treinamento
        for amostra in range(len(conjunto_treinamento)):
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
            print("Convergência alcançada. Parando o treinamento.")
            break

    # Exibir resultados do treinamento
    print(f"Treinamento concluído em {epoca} épocas.")
    exibir_pesos(pesos)

    # Validar o modelo usando amostras de validação
    validar_modelo(pesos, conjunto_validação)
