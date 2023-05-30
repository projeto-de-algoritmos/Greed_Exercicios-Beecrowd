# ========================================================================================================================
# Beecrowd - 1086 - O Salao do Clube - Nivel 7
# ========================================================================================================================
# Teoria: Algoritmos Ambiciosos
# Algoritmo utilizado: Algoritmo "Interval Partitioning"
# ========================================================================================================================
# Para facilitar a correçao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
# ========================================================================================================================
import pygame

# ========================================================================================================================
# O VetorHeapTabua serve para ordenar em ordem decrescente as tabuas de madeira disponiveis para cobrir o salao
# ========================================================================================================================
class VetorHeapTabua:
    def __init__(self): 
        self.vetor_heap_tabua = []
        self.vetor_heap_tabua.append(1) 
        
    def inserir_no_heap_tabua(self, comprimento_tabua):
        self.vetor_heap_tabua.append(comprimento_tabua)
        indice_inserido = self.vetor_heap_tabua[0]
        self.vetor_heap_tabua[0] += 1
        self.shift_up_no_heap_tabua(indice_inserido)

    def shift_up_no_heap_tabua(self, indice_shift):
        pai = indice_shift // 2
        if pai == 0:
            return
        elif self.vetor_heap_tabua[indice_shift] > self.vetor_heap_tabua[pai]:
            self.vetor_heap_tabua[indice_shift], self.vetor_heap_tabua[pai] = self.troca_tabua(self.vetor_heap_tabua[indice_shift], self.vetor_heap_tabua[pai])
            indice_shift = pai
            self.shift_up_no_heap_tabua(indice_shift)
        else:
            return

    def troca_tabua(self, origem, destino):
        aux = origem
        origem = destino
        destino = aux
        return origem, destino

    def apagar_do_heap_tabua(self, posicao):
        ultima_posicao_antes = self.vetor_heap_tabua[0] -1
        self.vetor_heap_tabua[posicao], self.vetor_heap_tabua[ultima_posicao_antes] = self.troca_tabua(self.vetor_heap_tabua[posicao], self.vetor_heap_tabua[ultima_posicao_antes])
        self.vetor_heap_tabua.pop(ultima_posicao_antes)
        self.vetor_heap_tabua[0] = self.vetor_heap_tabua[0] - 1
        self.heapify_no_heap_tabua(posicao)

    def heapify_no_heap_tabua(self, indice_heapify):
        if (indice_heapify * 2) > self.vetor_heap_tabua[0]-1:
            return
        filho_esquerdo = indice_heapify * 2
        filho_direito = (indice_heapify * 2) + 1
        if (indice_heapify * 2) + 1 <= self.vetor_heap_tabua[0]-1:
            if self.vetor_heap_tabua[filho_esquerdo] > self.vetor_heap_tabua[filho_direito]:
                maior_dos_dois_filhos = filho_esquerdo
            else:
                maior_dos_dois_filhos = filho_direito
        else:
            maior_dos_dois_filhos = filho_esquerdo
        if (self.vetor_heap_tabua[indice_heapify] < self.vetor_heap_tabua[maior_dos_dois_filhos]):
            self.vetor_heap_tabua[indice_heapify], self.vetor_heap_tabua[maior_dos_dois_filhos] = self.troca_tabua(self.vetor_heap_tabua[indice_heapify], self.vetor_heap_tabua[maior_dos_dois_filhos])
            indice_heapify = maior_dos_dois_filhos
            self.heapify_no_heap_tabua(indice_heapify)
        else:
            return

# ========================================================================================================================
# O VetorHeapFileira serve para ordenar em ordem crescente a soma total das tabuas de madeira colocadas em cada fileira
# Para que o desenho do salao fique harmonioso na tela de resultados, ordenou-se pela soma dos comprimentos, depois pela
# quantidade de tabuas na fileira e depois pelo numero da fileira que as tabuas se encontram
#        vetor_heap_fileira[0] -> soma dos comprimentos das tabuas
#        vetor_heap_fileira[1] -> numero da fileira que as tabuas se encontram
#        vetor_heap_fileira[2] -> quantidade de tabuas da fileira
# ========================================================================================================================
class VetorHeapFileira:
    def __init__(self): 
        self.vetor_heap_fileira = []
        self.vetor_heap_fileira.append([0, 1, 0])
        
    def inserir_no_heap_fileira(self, comprimento_total, fileira, qtde_tabuas):
        self.vetor_heap_fileira.append([comprimento_total, fileira, qtde_tabuas])
        indice_inserido = self.vetor_heap_fileira[0][1]
        self.vetor_heap_fileira[0][1] += 1
        self.shift_up_no_heap_fileira(indice_inserido)

    def shift_up_no_heap_fileira(self, indice_shift):
        pai = indice_shift // 2
        if pai == 0:
           return
        elif (self.vetor_heap_fileira[indice_shift][0] < self.vetor_heap_fileira[pai][0] 
              or (self.vetor_heap_fileira[indice_shift][0] == self.vetor_heap_fileira[pai][0]
                  and self.vetor_heap_fileira[indice_shift][2] < self.vetor_heap_fileira[pai][2])
                    or (self.vetor_heap_fileira[indice_shift][0] == self.vetor_heap_fileira[pai][0]
                        and self.vetor_heap_fileira[indice_shift][2] == self.vetor_heap_fileira[pai][2]
                        and self.vetor_heap_fileira[indice_shift][1] < self.vetor_heap_fileira[pai][1])):
            self.vetor_heap_fileira[indice_shift], self.vetor_heap_fileira[pai] = self.troca_fileira(self.vetor_heap_fileira[indice_shift], self.vetor_heap_fileira[pai])
            indice_shift = pai
            self.shift_up_no_heap_fileira(indice_shift)
        else:
            return

    def troca_fileira(self, origem, destino):
        aux = origem
        origem = destino
        destino = aux
        return origem, destino

    def heapify_no_heap_fileira(self, indice_heapify):
        if (indice_heapify * 2) > self.vetor_heap_fileira[0][1]-1:
            return
        filho_esquerdo = indice_heapify * 2
        filho_direito = (indice_heapify * 2) + 1
        if (indice_heapify * 2) + 1 <= self.vetor_heap_fileira[0][1]-1:
            if (self.vetor_heap_fileira[filho_esquerdo] < self.vetor_heap_fileira[filho_direito]
                or (self.vetor_heap_fileira[filho_esquerdo][0] == self.vetor_heap_fileira[filho_direito][0]
                    and self.vetor_heap_fileira[filho_esquerdo][2] < self.vetor_heap_fileira[filho_direito][2])
                        or (self.vetor_heap_fileira[filho_esquerdo][0] == self.vetor_heap_fileira[filho_direito][0]
                            and self.vetor_heap_fileira[filho_esquerdo][2] == self.vetor_heap_fileira[filho_direito][2]
                            and self.vetor_heap_fileira[filho_esquerdo][1] < self.vetor_heap_fileira[filho_direito][1])):
                menor_dos_dois_filhos = filho_esquerdo
            else:
                menor_dos_dois_filhos = filho_direito
        else:
            menor_dos_dois_filhos = filho_esquerdo
        if (self.vetor_heap_fileira[indice_heapify][0] > self.vetor_heap_fileira[menor_dos_dois_filhos][0]
            or (self.vetor_heap_fileira[indice_heapify][0] == self.vetor_heap_fileira[menor_dos_dois_filhos][0]
                and self.vetor_heap_fileira[indice_heapify][2] > self.vetor_heap_fileira[menor_dos_dois_filhos][2])
                    or (self.vetor_heap_fileira[indice_heapify][0] == self.vetor_heap_fileira[menor_dos_dois_filhos][0]
                        and self.vetor_heap_fileira[indice_heapify][2] == self.vetor_heap_fileira[menor_dos_dois_filhos][2]
                        and self.vetor_heap_fileira[indice_heapify][1] > self.vetor_heap_fileira[menor_dos_dois_filhos][1])):
            #print(f'precisa de heapify sim: troca posicao={indice_heapify} (valor:{self.vetor_heap_fileira[indice_heapify]}) o menor dos filhos posicao={menor_dos_dois_filhos} (valor={self.vetor_heap_fileira[menor_dos_dois_filhos]})')
            self.vetor_heap_fileira[indice_heapify], self.vetor_heap_fileira[menor_dos_dois_filhos] = self.troca_fileira(self.vetor_heap_fileira[indice_heapify], self.vetor_heap_fileira[menor_dos_dois_filhos])
            indice_heapify = menor_dos_dois_filhos
            self.heapify_no_heap_fileira(indice_heapify)
        else:
            #print(f'nao precisa de heapify - valor:{self.vetor_heap_fileira[indice_heapify]} <= valor={self.vetor_heap_fileira[menor_dos_dois_filhos]}')
            return
        #self.imprimir_heap_fileira()

def popular_conjunto_S(comprimento_fileira):
    tabuas = VetorHeapTabua()
    for tabua in todas_tabuas:
        tabuas.inserir_no_heap_tabua(int(tabua))
    comprimento_da_ultima_inserida = VetorHeapFileira()
    conjunto_S = [[]]
    # ===============================================================
    # salao com dimensoes M x N
    # ===============================================================
    # inicializa o conjunto solucao com a primeiro tabua que cabe
    while len(tabuas.vetor_heap_tabua) > 1:
        # se cabe insere a primeira
        if tabuas.vetor_heap_tabua[1] <= comprimento_fileira:
            conjunto_S[0].append(tabuas.vetor_heap_tabua[1])
            # salva em uma variavel o comprimento da tabua inserida
            comprimento_da_ultima_inserida.inserir_no_heap_fileira(tabuas.vetor_heap_tabua[1], 0, 1)
            tabuas.apagar_do_heap_tabua(1)
            break
        # se nao cabe descarta
        else:
            tabuas.apagar_do_heap_tabua(1)
    # repete para todos as tabuas verificando compatibilidade
    cont_fileiras = 0
    while len(tabuas.vetor_heap_tabua) > 1:
        achou_compativel = False
        if tabuas.vetor_heap_tabua[1] + comprimento_da_ultima_inserida.vetor_heap_fileira[1][0] <= comprimento_fileira: 
            fileira = comprimento_da_ultima_inserida.vetor_heap_fileira[1][1]
            conjunto_S[fileira].append(tabuas.vetor_heap_tabua[1])
            comprimento_da_ultima_inserida.vetor_heap_fileira[1][0] = comprimento_da_ultima_inserida.vetor_heap_fileira[1][0] + tabuas.vetor_heap_tabua[1]
            comprimento_da_ultima_inserida.vetor_heap_fileira[1][2] += 1
            achou_compativel = True
            comprimento_da_ultima_inserida.heapify_no_heap_fileira(1)
        if  not achou_compativel:
            cont_fileiras = cont_fileiras + 1
            conjunto_S.append([])
            conjunto_S[cont_fileiras].append(tabuas.vetor_heap_tabua[1])
            comprimento_da_ultima_inserida.inserir_no_heap_fileira(tabuas.vetor_heap_tabua[1], cont_fileiras, 1)
        tabuas.apagar_do_heap_tabua(1)
            
    conjunto_S_so_fileira_completa = []
    for fileira in conjunto_S:
        if sum(fileira) == comprimento_fileira:
            conjunto_S_so_fileira_completa.append(fileira)

    return conjunto_S_so_fileira_completa

if __name__ == "__main__":

    # ====================================================================================================================
    # Entrada
    # ====================================================================================================================
    # A entrada contem varios casos de teste. A primeira linha de um caso de teste contem dois inteiros M e N
    # indicando as dimensoes, em metros, do salao (1 ≤ N,M ≤ 104). A segunda linha contem um inteiro L, 
    # representando a largura das tabuas, em centimetros(1 ≤ L ≤ 100). A terceira linha contem um inteiro, 
    # K, indicando o numero de tabuas doadas (1 ≤ K ≤ 105). A quarta linha contem K inteiros Xi, separados 
    # por um espaço, cada um representando o comprimento, em metros, de uma tabua (1 ≤ Xi ≤ 104 para 1 ≤ i ≤ K). 
    # O final da entrada e indicado por uma linha que contem apenas dois zeros, separados por um espaço em branco.      
    # ====================================================================================================================
    M, N = input().split()

    M_largura_sala = int(M)
    N_comprimento_sala = int(N)
    L = input() 
    L_largura_tabuas = int(L)
    K = input()
    K_qtde_tabuas = int(K)
    todas_tabuas = input().split()

    flag_larg_da_no_comprimento = True
    flag_larg_da_na_largura = True

    todas_fileiras_no_comprimento = []
    if ((N_comprimento_sala * 100) % L_largura_tabuas == 0) and K_qtde_tabuas >= (N_comprimento_sala * 100) / L_largura_tabuas:    
        qtdd_fileiras_no_comprimento = (N_comprimento_sala * 100) / L_largura_tabuas
        todas_fileiras_no_comprimento = popular_conjunto_S( M_largura_sala)
    else:
        flag_larg_da_no_comprimento = False

    todas_fileiras_na_largura = []
    if (M_largura_sala * 100) % L_largura_tabuas == 0 and K_qtde_tabuas >= (M_largura_sala * 100) / L_largura_tabuas:
        qtdd_fileiras_na_largura = (M_largura_sala * 100) / L_largura_tabuas
        todas_fileiras_na_largura = popular_conjunto_S( N_comprimento_sala)
    else:
        flag_larg_da_na_largura = False
        
    if flag_larg_da_na_largura or flag_larg_da_no_comprimento:
        soma_tabuas_na_largura = 0
        if len(todas_fileiras_na_largura) == qtdd_fileiras_na_largura:
            for fileira in todas_fileiras_na_largura:
                soma_tabuas_na_largura += len(fileira)

        soma_tabuas_no_comprimento = 0
        if len(todas_fileiras_no_comprimento) == qtdd_fileiras_no_comprimento:
            for fileira in todas_fileiras_no_comprimento:
                soma_tabuas_no_comprimento += len(fileira)

       # Define o texto do resultado a ser exibido
        if soma_tabuas_no_comprimento == 0 and soma_tabuas_na_largura == 0:
            texto_resultado = ('Impossivel cobrir todo o piso do salao')
        elif soma_tabuas_no_comprimento == 0:
            texto_resultado = 'E possivel cobrir todo o piso do salao com ' + str(soma_tabuas_na_largura) + ' tabuas'
        elif soma_tabuas_na_largura == 0:
            texto_resultado = 'E possivel cobrir todo o piso do salao com ' + str(soma_tabuas_no_comprimento) + ' tabuas'
        else: 
            texto_resultado = 'E possivel cobrir todo o piso do salao com ' + str(min(soma_tabuas_no_comprimento, soma_tabuas_na_largura)) + ' tabuas'
    else:
        texto_resultado = 'Impossivel cobrir todo o piso do salao'
    
    pygame.init()               # Inicializa o pygame
    largura_tela = 800          # Define as dimensoes da tela
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))     # Cria a tela
    
    cor_preta = (0, 0, 0)               # Define a cor do texto
    fonte = pygame.font.Font(None, 36)  # Define a fonte e o tamanho do texto

    texto_tabuas_1 = f'Com as seguintes tabuas de {L_largura_tabuas} cm de largura'
    superficie_texto_tabuas_1 = fonte.render(texto_tabuas_1, True, cor_preta)   # Cria a superficie contendo o texto        
    posicao_x_texto_tabuas_1 = 100               # Define a posiçao do texto na tela
    posicao_y_texto_tabuas_1 = 30

    texto_tabuas_2 = f'Para uma sala de dimensoes:'
    superficie_texto_tabuas_2 = fonte.render(texto_tabuas_2, True, cor_preta)         
    posicao_x_texto_tabuas_2 = 100               
    posicao_y_texto_tabuas_2 = 330
                                        
    texto_dimensao_1 = f'{M_largura_sala} x {N_comprimento_sala}'
    superficie_texto_dimensao_1 = fonte.render(texto_dimensao_1, True, cor_preta)         
    posicao_x_texto_dimensao_1 = 200               
    posicao_y_texto_dimensao_1 = 360

    texto_dimensao_2 = f'{N_comprimento_sala} x {M_largura_sala}'
    superficie_texto_dimensao_2 = fonte.render(texto_dimensao_2, True, cor_preta)         
    posicao_x_texto_dimensao_2 = 450               
    posicao_y_texto_dimensao_2 = 360
    
    superficie_texto_resultado = fonte.render(texto_resultado, True, cor_preta)         
    posicao_x_texto_resultado = 100               
    posicao_y_texto_resultado = 540
    
    cor_vermelha = (255, 0, 0)     # Define a cor das tabuas 
    largura_tabuas = 200
    altura_tabuas = L_largura_tabuas/5

    # Loop principal do jogo
    executando = True
    while executando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False
        tela.fill((255, 255, 230))  # Preenche a tela com uma cor de fundo (amarelo claro)
        
        # desenha as tabuas disponiveis na tela
        posicao_x_tabuas = 100             # Define as coordenadas das tabuas
        posicao_y_tabuas = 60
        for largura_tabuas in todas_tabuas:
            # Desenha cada tabua na tela
            pygame.draw.rect(tela, cor_vermelha, 
                        (posicao_x_tabuas, posicao_y_tabuas, (int(largura_tabuas)*20), altura_tabuas))  
            # Desenha a borda de cada tabua na tela
            pygame.draw.rect(tela, cor_preta, 
                        (posicao_x_tabuas, posicao_y_tabuas, (int(largura_tabuas)*20), altura_tabuas), 2)
            posicao_x_tabuas = 100             
            posicao_y_tabuas =  posicao_y_tabuas + (L_largura_tabuas/5) + 5            

        # desenha o salao comprimento x largura
        posicao_x_tabuas = 200
        posicao_y_tabuas = 390
        for fileira in todas_fileiras_no_comprimento:
            for tamanho_tabua in fileira:
                # Desenha cada tabua na tela
                pygame.draw.rect(tela, cor_vermelha, 
                            (posicao_x_tabuas, posicao_y_tabuas, (tamanho_tabua*20), altura_tabuas))  
                # Desenha a borda de cada tabua na tela
                pygame.draw.rect(tela, cor_preta, 
                            (posicao_x_tabuas, posicao_y_tabuas, (tamanho_tabua)*20, altura_tabuas), 2)
                posicao_x_tabuas =  posicao_x_tabuas + ((tamanho_tabua)*20)             
            posicao_x_tabuas = 200
            posicao_y_tabuas = posicao_y_tabuas + (L_largura_tabuas/5)            

        posicao_x_tabuas = 450
        posicao_y_tabuas = 390

        # desenha o salao largura x comprimento
        for fileira in todas_fileiras_na_largura:
            for tamanho_tabua in fileira:
                # Desenha cada tabua na tela
                pygame.draw.rect(tela, cor_vermelha, 
                            (posicao_x_tabuas, posicao_y_tabuas, (tamanho_tabua*20), altura_tabuas))  # Desenha o retangulo na tela
                # Desenha a borda de cada tabua na tela
                pygame.draw.rect(tela, cor_preta, 
                            (posicao_x_tabuas, posicao_y_tabuas, (tamanho_tabua)*20, altura_tabuas), 2)
                posicao_x_tabuas =  posicao_x_tabuas + ((tamanho_tabua)*20)             
            posicao_x_tabuas = 450
            posicao_y_tabuas = posicao_y_tabuas + (L_largura_tabuas/5)            

        # Desenha as superficies que contem cada texto na tela
        tela.blit(superficie_texto_resultado, (posicao_x_texto_resultado, posicao_y_texto_resultado))     
        tela.blit(superficie_texto_tabuas_1, (posicao_x_texto_tabuas_1, posicao_y_texto_tabuas_1))     
        tela.blit(superficie_texto_tabuas_2, (posicao_x_texto_tabuas_2, posicao_y_texto_tabuas_2))     
        tela.blit(superficie_texto_dimensao_1, (posicao_x_texto_dimensao_1, posicao_y_texto_dimensao_1))
        tela.blit(superficie_texto_dimensao_2, (posicao_x_texto_dimensao_2, posicao_y_texto_dimensao_2))

        pygame.display.flip()   # Atualiza a tela

    pygame.quit()       # Finaliza o pygame
