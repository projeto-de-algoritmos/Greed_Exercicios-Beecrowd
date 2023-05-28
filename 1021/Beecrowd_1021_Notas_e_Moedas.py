# ========================================================================================================================
# Beecrowd - 1021 - Notas e Moedas - Nivel 6
# ========================================================================================================================
# Teoria: Algoritmos Ambiciosos
# Algoritmo utilizado: Algoritmo das moedas
# ========================================================================================================================
# Para facilitar a correçao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
# ========================================================================================================================
    
if __name__ == "__main__":

    # ====================================================================================================================
    # As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possiveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
    # ====================================================================================================================
    tipos_notas = [10000, 5000, 2000, 1000, 500, 200]   # as notas foram multiplicadas por 100 para facilitar os calculos
    tipos_moedas = [100, 50, 25, 10, 5, 1]              # as moedas tambem

    # ====================================================================================================================
    # Entrada
    # ====================================================================================================================
    # Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetario. 
    # O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
    # A seguir, calcule o menor numero de notas e moedas possiveis no qual o valor pode ser decomposto. 
    # ====================================================================================================================
    N_valor = float(input())
    N_valor = int(N_valor * 100)
    
    # ====================================================================================================================
    # Saida
    # ====================================================================================================================
    # A seguir mostre a relaçao de notas necessarias.
    # Imprima a quantidade minima de notas e moedas necessarias para trocar o valor inicial, conforme exemplo fornecido.
    # Obs: Utilize ponto (.) para separar a parte decimal.
    # ====================================================================================================================
    print('NOTAS:')
    for nota in tipos_notas:
        conta_nota = 0
        while nota <= N_valor:
            N_valor = N_valor - nota
            conta_nota = conta_nota + 1
        print('{} nota(s) de R$ {:.2f}'.format(conta_nota, nota/100.0))
    
    print('MOEDAS:')
    for moeda in tipos_moedas:
        conta_moeda = 0
        while moeda <= N_valor:
            N_valor = N_valor - moeda
            conta_moeda = conta_moeda + 1
        print('{} moeda(s) de R$ {:.2f}'.format(conta_moeda, moeda/100.0))

# ========================================================================================================================