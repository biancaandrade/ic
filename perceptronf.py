from random import random

def degrau_bipolar(valor):
    return 1 if valor > 0 else -1

def regra_aprendizado_hebb(peso, taxa_aprendizado, atividade_entrada, atividade_saida):
    return peso + taxa_aprendizado * atividade_entrada * atividade_saida

class Perceptron:
    def __init__(self, numero_entradas, taxa_aprendizado, max_epocas):
        self.pesos = [random() for _ in range(numero_entradas + 1)]
        self.epocas = 0
        self.taxa_aprendizado = taxa_aprendizado
        self.max_epocas = max_epocas

    def obter_pesos(self):
        return self.pesos

    def obter_epocas(self):
        return self.epocas

    def maximo_de_epocas_atingido(self):
        return self.epocas >= self.max_epocas

    def treinar(self, dados_entrada, saidas_esperadas):
        erro = True
        while not self.epocas >= self.max_epocas and erro:
            erro = False
            for (entrada, saida_esperada) in zip(dados_entrada, saidas_esperadas):
                erro |= self.atualizar_pesos(entrada, saida_esperada)
            self.epocas += 1
    #calcula a saída de um único conjunto de dados
    def calcular(self, entrada):
        #gera meu resultado intermediário que vai para o combinador
        produtos = [entrada * peso for (entrada, peso) in zip([-1] + entrada, self.pesos)] 
        resultado_intermediario = sum(produtos)
        return degrau_bipolar(resultado_intermediario) #retorna o resultado da função de ativação

    #itera sobre a matriz passando por cada conjunto
    def calcular_todos(self, dados_entrada):
        return [self.calcular(d) for d in dados_entrada]

    def atualizar_pesos(self, entrada, saida_esperada):
        atividade_atual = self.calcular(entrada) #retornará -1 ou 1
        if atividade_atual == saida_esperada:
            return False
        self.pesos = [regra_aprendizado_hebb(p, self.taxa_aprendizado, x, saida_esperada) for (p, x) in zip(self.pesos, [-1] + entrada)]
        return True

#bloco para separar entradas das saídas
    
def parse_para_treinamento(filename): 
    entradas = []
    saidas_esperadas = []
    with open(filename) as f:
        for line in f:
            args, saida_esperada = parse_linha(line)
            entradas.append(args)
            saidas_esperadas.append(saida_esperada)
    return entradas, saidas_esperadas

def parse_linha(linha):
    partes = linha.split()
    args = [float(p) for p in partes[:-1]]
    saida_esperada = int(float(partes[-1]))
    return args, saida_esperada

def parse_entrada(filename):
    entradas = []
    with open(filename) as f:
        for line in f:
            args = [float(p) for p in line.split()]
            entradas.append(args)
    return entradas

#fim do bloco de separação
def calcular_taxa_acerto(saidas_esperadas, resultados):
    corretos = sum(1 for e, r in zip(saidas_esperadas, resultados) if e == r)
    return (corretos * 100) / len(resultados)

# fase de treinamento
for i in range(1, 6):

    print(f'\n<< Treinamento {i} >>')
    perceptron = Perceptron(3, 0.01, 1000)
    dados_entrada, saidas_esperadas = parse_para_treinamento('dados/conjunto_treinamento.txt')

    print('Pesos pré-treinamento:', perceptron.obter_pesos())
    #resultados_originais = perceptron.calcular_todos(dados_entrada)
    perceptron.treinar(dados_entrada, saidas_esperadas) #itera até que erro = false ou estoure o nº de épocas

    print('Treinamento executado')
    print('Pesos pós-treinamento:', perceptron.obter_pesos())
    print('Número de Épocas:', perceptron.obter_epocas())

    novos_resultados = perceptron.calcular_todos(dados_entrada) #Retorna o -1 ou 1 
    print('Taxa de acerto:', '{:.2f}%'.format(calcular_taxa_acerto(saidas_esperadas, novos_resultados)))

# fase de operação
    
    print('<< Executando Classificação >>')
    entradas = parse_entrada('dados/conjunto_validação.txt')
    resultados = perceptron.calcular_todos(entradas)
    for j, resultado in enumerate(resultados, 1):
        print(f'Amostra {j}: Saída = {resultado}')
