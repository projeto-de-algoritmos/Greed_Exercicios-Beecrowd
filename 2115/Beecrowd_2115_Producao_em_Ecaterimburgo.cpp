// ========================================================================================================================
// Beecrowd - 2115 - Produção em Ecaterimburgo - Nivel 6
// ========================================================================================================================
// Teoria: Algoritmos Ambiciosos
// Algoritmo utilizado: Algoritmo "Scheduling to Minimize Lateness"
// ========================================================================================================================
// Para facilitar a correçao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
// ========================================================================================================================
#include <iostream>
#include <vector>
#include <algorithm>

struct Tarefas {
    int tempo_que_esta_disponivel;
    int tempo_de_processamento;
};

bool compara_tarefas(const Tarefas& tarefa1, const Tarefas& tarefa2) {
    return (tarefa1.tempo_que_esta_disponivel < tarefa2.tempo_que_esta_disponivel);
}

// ========================================================================================================================
// Os pedidos de ferramentas chegam na fabrica de forma continua, isto e, no inicio do dia nem todos 
// os pedidos podem ser processados, pois estes estarao disponiveis ao longo do dia. O gerente acha 
// que os funcionarios nao estao escolhendo bem a ordem na qual os pedidos sao atendidos e quer analisar
// as sequencias de pedidos de dias anteriores. Dessa forma, ele pede que voce determine, para um dado dia, 
// o menor instante possivel em que todos os pedidos estariam finalizados.
// ========================================================================================================================
int main() {

    // ====================================================================================================================
    // Entrada
    // ====================================================================================================================
    // A entrada e composta por diversas instancias e termina com final de arquivo (EOF).
    // Cada instancia começa com o numero N (1 ≤ N ≤ 10) de tarefas que serao processadas no dia. 
    int N_tarefas;
    while (std::cin >> N_tarefas) {
        std::vector<Tarefas> vetor_tarefas(N_tarefas);
        // As N linhas seguintes tem o tempo d em que a tarefa estara disponivel e o tempo p de processamento da tarefa 
        // na maquina (1 ≤ d, p ≤ 10). O inicio do processamento se da no instante 1.
        for (int i = 0; i < N_tarefas; i++) {
            std::cin >> vetor_tarefas[i].tempo_que_esta_disponivel >> vetor_tarefas[i].tempo_de_processamento;
        }
        // ordenando pelo tempo quea tarefa esta disponivel - ordem crescente
        std::sort(vetor_tarefas.begin(), vetor_tarefas.end(), compara_tarefas);
        
        // ================================================================================================================
        // Solucao
        // ================================================================================================================
        // usando o algoritmo para minimizar atrasos e ordenando as tarefas pelo tempo de termino e preciso apenas 
        // contabilizar o tempo que o sistema fica ocioso, esperando que a proxima tarefa esteja disponivel
        int tempo_de_termino = vetor_tarefas[0].tempo_que_esta_disponivel + vetor_tarefas[0].tempo_de_processamento;
        for (int i = 1; i < N_tarefas; i++) {
            if (vetor_tarefas[i].tempo_que_esta_disponivel >= tempo_de_termino) {
                tempo_de_termino = vetor_tarefas[i].tempo_que_esta_disponivel + vetor_tarefas[i].tempo_de_processamento;
            } else {
                tempo_de_termino += vetor_tarefas[i].tempo_de_processamento;
            }
        }
        
        // ================================================================================================================
        // Saida
        // ================================================================================================================
        // Para cada instancia seu programa devera imprimir o menor instante em que a tarefa que for processada por
        // ultimo terminara seu processamento.
        std::cout << tempo_de_termino << std::endl;
    }
    
    return 0;
}
