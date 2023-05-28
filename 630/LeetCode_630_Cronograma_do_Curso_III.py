# ========================================================================================================================
# LeetCode - 630 - Posto_de_gasolina - Nivel Duro
# ========================================================================================================================
# Teoria: Algoritmos Ambiciosos
# Algoritmo utilizado: Algoritmo Interval Scheduling
# ========================================================================================================================
# Para facilitar a correçao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
# ========================================================================================================================

# Você recebe uma matriz courses onde indica que o curso deve ser feito continuamente
# Você começará no dia e não poderá fazer dois ou mais cursos simultaneamente
# Retorna o número máximo de cursos que você pode fazer .

# ========================================================================================================================

from heapq import heappush, heapreplace

class Solution:
    def scheduleCourse(self, curso: List[List[int]]) -> int:
        heap = []  # Heap para armazenar as durações dos cursos em ordem inversa
        dia = 0  # Contador de dias

        # Ordenar os cursos com base no prazo final (deadline) 
        for duracao, deadline in sorted(curso, key=lambda a: (a[-1], a[0])):
            if duracao > deadline:
                continue

            # O objetivo é minimizar a duração total em ordem de prazo final
            if dia + duracao > deadline:
                maior_duracao = -heap[0]

                # Se a duração do curso atual for maior do que a maior duração atual no heap,
                # o curso não pode melhorar a duração total e é descartado
                if duracao > maior_duracao:
                    continue

                # Substituir a maior duração no heap pela duração do curso atual
                heapreplace(heap, -duracao)

                # Ajustar o contador de dias subtraindo a maior duração e adicionando a duração do curso atual
                dia = dia - maior_duracao + duracao
            else:
                # Adicionar a duração do curso atual ao heap e incrementar o contador de dias
                heappush(heap, -duracao)
                dia += duracao

        # Retornar o tamanho do heap, que representa o número máximo de cursos que podem ser feitos sem sobreposição
        return len(heap)  