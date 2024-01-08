#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_AMOSTRAS 30
#define NUM_ENTRADAS 3
#define TAXA_APRENDIZAGEM 0.01
#define NUM_TREINAMENTOS 5
#define MAX_EPOCAS 10000

// Função degrau bipolar, ajustei para u>=-5 para melhorar a convergência, com u>=0 as épocas chegavam ao limite 
float sinal(double u) {
    return (u >= -5) ? 1.0 : -1.0;
}

// Função para exibir os pesos
void exibirPesos(double pesos[]) {
    printf("Pesos: ");
    for (int i = 0; i <= NUM_ENTRADAS; i++) {
        printf("%lf ", pesos[i]);
    }
    printf("\n\n");
}

// Função para validar o modelo
void validarModelo(double pesos[], float amostras_validacao[][NUM_ENTRADAS]) {
    printf("<< Executando Classificação >>\n");
    
    for (int amostra = 0; amostra < 10; amostra++) {
        double u = 0.0;

        // Cálculo do potencial de ativação
        for (int entrada = 0; entrada < NUM_ENTRADAS; entrada++) {
            u += pesos[entrada] * amostras_validacao[amostra][entrada];
        }

        u -= pesos[0];  // o bias está na posição pesos[0]

        //função de ativação
        float y = sinal(u);
        printf("Amostra %d: Saída = %.6f\n", amostra + 1, y);
    }
}


int main() {
    float conjunto_treinamento[NUM_AMOSTRAS][NUM_ENTRADAS + 1] = {
        {-0.6508, 0.1097, 4.0009, -1},
        {-1.4492, 0.8896, 4.4005, -1},
        {2.0850, 0.6876, 12.0710, -1},
        {0.2626, 1.1476, 7.7985, 1},
        {0.6418, 1.0234, 7.0427, 1},
        {0.2569, 0.6730, 8.3265, -1},
        {1.1155, 0.6043, 7.4446, 1},
        {0.0914, 0.3399, 7.0677, -1},
        {0.0121, 0.5256, 4.6316, 1},
        {-0.0429, 0.4660, 5.4323, 1},
        {0.4340, 0.6870, 8.2287, -1},
        {0.2735, 1.0287, 7.1934, 1},
        {0.4839, 0.4851, 7.4850, -1},
        {0.4089, -0.1267, 5.5019, -1},
        {1.4391, 0.1614, 8.5843, -1},
        {-0.9115, -0.1973, 2.1962, -1},
        {0.3654, 1.0475, 7.4858, 1},
        {0.2144, 0.7515, 7.1699, 1},
        {0.2013, 1.0014, 6.5489, 1},
        {0.6483, 0.2183, 5.8991, 1},
        {-0.1147, 0.2242, 7.2435, -1},
        {-0.7970, 0.8795, 3.8762, 1},
        {-1.0625, 0.6366, 2.4707, 1},
        {0.5307, 0.1285, 5.6883, 1},
        {-1.2200, 0.7777, 1.7252, 1},
        {0.3957, 0.1076, 5.6623, -1},
        {-0.1013, 0.5989, 7.1812, -1},
        {2.4482, 0.9455, 11.2095, 1},
        {2.0149, 0.6192, 10.9263, -1},
        {0.2012, 0.2611, 5.4631, 1}
    };

    float amostras_validacao[10][NUM_ENTRADAS] = {
        {-0.3665, 0.0620, 5.9891},
        {-0.7842, 1.1267, 5.5912},
        {0.3012, 0.5611, 5.8234},
        {0.7757, 1.0648, 8.0677},
        {0.1570, 0.8028, 6.3040},
        {-0.7014, 1.0316, 3.6005},
        {0.3748, 0.1536, 6.1537},
        {-0.6920, 0.9404, 4.4058},
        {-1.3970, 0.7141, 4.9263},
        {-1.8842, 0.2805, 1.2548}
    };

    long long int epoca;
    double pesos[NUM_ENTRADAS + 1];
    double y;
    int amostra;
    double u; 

    // Loop para executar cinco treinamentos
    for (int treinamento = 1; treinamento <= NUM_TREINAMENTOS; treinamento++) {
        printf("\nTreinamento %d:\n", treinamento);

        // Inicialização do gerador de números aleatórios
        srand(time(NULL) + treinamento);

        // Inicialização do vetor de pesos com valores aleatórios entre 0 e 1
        for (int i = 0; i <= NUM_ENTRADAS; i++) {
            pesos[i] = ((double)rand() / RAND_MAX);
        }
        printf("Treinamento iniciado\n");
        exibirPesos(pesos);
        epoca = 0;

        // Loop sobre as amostras de treinamento
        while (epoca < MAX_EPOCAS) {
            int erro = 0;

            for (amostra = 0; amostra < NUM_AMOSTRAS; amostra++) {
                u = 0.0;

                // Cálculo do potencial de ativação
                for (int entrada = 0; entrada < NUM_ENTRADAS; entrada++) {
                    u += pesos[entrada] * conjunto_treinamento[amostra][entrada];
                }

                u -= pesos[0];  // Ajuste para incluir o bias

                // Aplicação da função de ativação
                y = sinal(u);

                // Verificação do erro
                if (y != conjunto_treinamento[amostra][NUM_ENTRADAS]) {
                    // Atualização dos pesos
                    for (int entrada = 0; entrada < NUM_ENTRADAS; entrada++) {
                        pesos[entrada] += TAXA_APRENDIZAGEM * (conjunto_treinamento[amostra][NUM_ENTRADAS] - y) * conjunto_treinamento[amostra][entrada];
                    }

                    // Atualização do bias separadamente
                    pesos[0] += TAXA_APRENDIZAGEM * (conjunto_treinamento[amostra][NUM_ENTRADAS] - y);

                    erro = 1;
                    //amostra--;
                }
            }

            epoca++;

            // Verificar convergência
            if (!erro) {
                printf("Convergência alcançada. Parando o treinamento.\n");
                break;
            }
        }

        // Exibir resultados do treinamento
        printf("Treinamento concluído em %lld épocas.\n", epoca);
        exibirPesos(pesos);

        // Validar o modelo usando amostras de validação
        validarModelo(pesos, amostras_validacao);
    }

    return 0;
}

