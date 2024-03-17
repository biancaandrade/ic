import numpy as np
import random

NUM_AMOSTRAS = 30
NUM_ENTRADAS = 3
TAXA_APRENDIZAGEM = 0.01
NUM_TREINAMENTOS = 5
MAX_EPOCAS = 10000

conjunto_treinamento = np.loadtxt('dados/conjunto_treinamento.txt', dtype=float)
conjunto_validacao = np.loadtxt('dados/conjunto_validação.txt', dtype=float)
#print(conjunto_treinamento)
#print(conjunto_validacao)

