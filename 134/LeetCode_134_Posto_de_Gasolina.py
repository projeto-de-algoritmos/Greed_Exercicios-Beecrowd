# ========================================================================================================================
# LeetCode - 134 - Posto_de_gasolina - Nivel Médio
# ========================================================================================================================
# Teoria: Algoritmos Ambiciosos
# Algoritmo utilizado: Algoritmo do Caminhoneiro
# ========================================================================================================================
# Para facilitar a correçao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
# ========================================================================================================================

# Dadas duas matrizes inteiras gas(combustível fornecido) e cost(custo para percorrer a distância), retorne 
# o índice do posto de gasolina inicial
# se você puder percorrer o circuito uma vez no sentido horário, caso contrário, retorne -1

# ========================================================================================================================

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        combustivel_restante = 0  # Combustível restante no tanque
        ponto_partida = 0  # Índice do ponto de partida atual
        combustivel_disponivel = 0  # Combustível disponível em todo o percurso
        
        for i in range(len(gas)):
            
            diferenca = gas[i] - cost[i]  # Diferença entre o combustível fornecido e o custo para percorrer a distância
            combustivel_disponivel += diferenca  # Atualizar o combustível disponível em todo o percurso
            combustivel_restante += diferenca  # Atualizar o combustível restante no tanque

            if combustivel_restante < 0:
                ponto_partida = i + 1  # Atualizar o ponto de partida para o próximo índice
                combustivel_restante = 0  # Resetar o combustível restante para zero

        # Se o combustível disponível for maior ou igual a zero, é possível completar o percurso a partir do ponto de partida atual    
        if combustivel_disponivel >= 0:
            return ponto_partida  
        # Caso contrário, não é possível completar o percurso em um único ciclo
        else:
            return -1  


       