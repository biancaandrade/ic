# Perceptron - Projeto prático

Pela análise de um processo de destilação fracionada de petróleo observou-se que determinado óleo poderia ser classificado em duas classes de pureza {P1 e P2} a partir da medição de três grandezas {x1, x2, x3}, que representam algumas de suas propriedades físico-químicas. A equipe de engenheiros e cientistas pretende usar urna rede Perceptron para executar a classificação automática das duas classes. Assim, baseado nas informações coletadas do processo, formou-se o conjunto de treinamento apresentado no apêndice I, tomando por convenção o valor -1 para óleo pertencente à classe P1 e o valor 1 para óleo pertencente à classe P2. Para tanto, o neurônio constituinte do Perceptron terá então três entradas e uma saída conforme ilustrado na figura abaixo.

**Figura 1: Arquitetura do Perceptron para o projeto prático**

## Exercício

Utilizando o algoritmo supervisionado de Hebb (regra de Hebb) para classificação de padrões, e
assumindo-se a taxa de aprendizagem como 0,01, faça as seguintes atividades:

1) Execute cinco treinamentos para a rede Perceptron, iniciando o vetor de pesos {w} em cada
treinamento com valores aleatórios entre zero e um. Se for o caso, reinicie o gerador de
números aleatórios em cada treinamento de tal forma que os elementos do vetor de pesos
iniciais não sejam os mesmos. O conjunto de treinamento encontra-se no [anexo](anexo).

2) Registre os resultados dos cinco treinamentos na tabela apresentada a seguir



**Tabela 1 - Resultados dos treinamentos do Perceptron**

3) Após o treinamento do Perceptron, coloque este em operação, aplicando-o na classificação
automática das amostras de óleo da tabela 1.2, indicando ainda nesta tabela aqueles
resultados das saídas (Classes) referentes aos cinco processos de treinamento realizados no
item 1.

**Tabela 1.2 — Amostras de óleo para validar a rede Perceptron**
