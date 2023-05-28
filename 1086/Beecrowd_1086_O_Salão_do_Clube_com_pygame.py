

import pygame


class VetorHeapTabua:
    def __init__(self): 
        self.vetor_heap_tabua = []
        self.vetor_heap_tabua.append(1) 
        
    def imprimir_heap_tabua(self):
        if len(self.vetor_heap_tabua) == 1:
            print("heap tabua vazio")
        else:
            for i in range(1, self.vetor_heap_tabua[0]):
                print(f'{self.vetor_heap_tabua[i]}', end=' - ')
            print()

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

class VetorHeapFileira:
    def __init__(self): 
        self.vetor_heap_fileira = []
        # vetor_heap_fileira[0] = soma dos comprimentos das tabuas
        # vetor_heap_fileira[1] = numero da fileira que as tabuas se encontram
        # vetor_heap_fileira[2] = quantidade de tabuas da fileira
        self.vetor_heap_fileira.append([0, 1, 0])
        
    def imprimir_heap_fileira(self):
        if len(self.vetor_heap_fileira) == 0:
            print("heap fileira vazio")
        else:
            print('[comprim.total da fileira, numero da fileira, qtde de tabuas da fileira]')
            for i in range(1, self.vetor_heap_fileira[0][1]):
                print(f'[{self.vetor_heap_fileira[i][0]}, {self.vetor_heap_fileira[i][1]}, {self.vetor_heap_fileira[i][2]}]', end=' - ')
            print()

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
        #print('\n=========== heapify_no_heap ==========')
        if (indice_heapify * 2) > self.vetor_heap_fileira[0][1]-1:
            #print('nao precisa de heapify - ja esta no ultimo nivel')
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
    #print('------------heap tabua inicial-------------')
    #tabuas.imprimir_heap_tabua()
    #print('-------------------------------')
    comprimento_da_ultima_inserida = VetorHeapFileira()
    #print(f'qtde fileiras: {qtde_fileiras_possiveis} x comprimento fileira: {comprimento_fileira}')
    # matriz de solucoes
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
            #print('------------heap tabua apos tirar primeira tabua -------------')
            #tabuas.imprimir_heap_tabua()
            break
        # se nao cabe descarta
        else:
            tabuas.apagar_do_heap_tabua(1)
    # repete para todos os aulas verificando compatibilidade
    cont_fileiras = 0
    while len(tabuas.vetor_heap_tabua) > 1:
        achou_compativel = False
        if tabuas.vetor_heap_tabua[1] + comprimento_da_ultima_inserida.vetor_heap_fileira[1][0] <= comprimento_fileira: 
            fileira = comprimento_da_ultima_inserida.vetor_heap_fileira[1][1]
            conjunto_S[fileira].append(tabuas.vetor_heap_tabua[1])
            comprimento_da_ultima_inserida.vetor_heap_fileira[1][0] = comprimento_da_ultima_inserida.vetor_heap_fileira[1][0] + tabuas.vetor_heap_tabua[1]
            comprimento_da_ultima_inserida.vetor_heap_fileira[1][2] += 1
            #comprimento_da_ultima_inserida.imprimir_heap_fileira()
            achou_compativel = True
            comprimento_da_ultima_inserida.heapify_no_heap_fileira(1)
            '''
            print(f'--------------- inseriu na fileira {fileira} ---------------')
            print('fileiras', end=": ")
            comprimento_da_ultima_inserida.imprimir_heap_fileira()
            print('tabuas', end=": ")
            tabuas.imprimir_heap_tabua()
            print(len(tabuas.vetor_heap_tabua))
            '''
        if  not achou_compativel:
            cont_fileiras = cont_fileiras + 1
            conjunto_S.append([])
            conjunto_S[cont_fileiras].append(tabuas.vetor_heap_tabua[1])
            comprimento_da_ultima_inserida.inserir_no_heap_fileira(tabuas.vetor_heap_tabua[1], cont_fileiras, 1)
            '''
            print('--------------- abriu nova fileira ---------------')
            print('fileiras', end=": ")
            comprimento_da_ultima_inserida.imprimir_heap_fileira()
            print('tabuas', end=": ")
            tabuas.imprimir_heap_tabua()
            '''
        tabuas.apagar_do_heap_tabua(1)
            
    #print(conjunto_S)
    conjunto_S_so_fileira_completa = []
    for fileira in conjunto_S:
        if sum(fileira) == comprimento_fileira:
            conjunto_S_so_fileira_completa.append(fileira)

    #tabuas.imprimir_heap_tabua()
    #print(conjunto_S_so_fileira_completa)
    #tabuas.imprimir_heap()
    return conjunto_S_so_fileira_completa

if __name__ == "__main__":

    # =====================================================
    # Entrada
    # =====================================================
    # A entrada contém vários casos de teste. A primeira linha de um caso de teste contém dois inteiros M e N
    # indicando as dimensões, em metros, do salão (1 ≤ N,M ≤ 104). A segunda linha contém um inteiro L, 
    # representando a largura das tábuas, em centímetros(1 ≤ L ≤ 100). A terceira linha contém um inteiro, 
    # K, indicando o número de tábuas doadas (1 ≤ K ≤ 105). A quarta linha contém K inteiros Xi, separados 
    # por um espaço, cada um representando o comprimento, em metros, de uma tábua (1 ≤ Xi ≤ 104 para 1 ≤ i ≤ K). 
    # O final da entrada é indicado por uma linha que contém apenas dois zeros, separados por um espaço em branco.      
    # =====================================================
    # J - quantidade de aulas
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

    if ((N_comprimento_sala * 100) % L_largura_tabuas == 0) and K_qtde_tabuas >= (N_comprimento_sala * 100) / L_largura_tabuas:    
        qtdd_fileiras_no_comprimento = (N_comprimento_sala * 100) / L_largura_tabuas
        todas_fileiras_no_comprimento = popular_conjunto_S( M_largura_sala)
    else:
        flag_larg_da_no_comprimento = False
        #print(f'impossivel pela largura da tabua no comprimento {N_comprimento_sala} - qtde fileiras: {(N_comprimento_sala * 100) / L_largura_tabuas :.2f}')

    if (M_largura_sala * 100) % L_largura_tabuas == 0 and K_qtde_tabuas >= (M_largura_sala * 100) / L_largura_tabuas:
        qtdd_fileiras_na_largura = (M_largura_sala * 100) / L_largura_tabuas
        todas_fileiras_na_largura = popular_conjunto_S( N_comprimento_sala)
    else:
        flag_larg_da_na_largura = False
        #print(f'impossivel pela largura da tabua na largura da sala {M_largura_sala} - qtde fileiras: {(M_largura_sala * 100) / L_largura_tabuas :.2f}')
        
    #print('----------------------------------------------------')
    if flag_larg_da_na_largura or flag_larg_da_no_comprimento:
        soma_tabuas_na_largura = 0
        if len(todas_fileiras_na_largura) == qtdd_fileiras_na_largura:
            #print('ok na largura')
            #print(todas_fileiras_na_largura)
            for fileira in todas_fileiras_na_largura:
                soma_tabuas_na_largura += len(fileira)
        '''
        elif len(todas_fileiras_na_largura) < qtdd_fileiras_na_largura:
            print('impossivel na largura')
        else:
            print(f'qdte fileiras na largura: {len(todas_fileiras_na_largura)}')
        '''
        soma_tabuas_no_comprimento = 0
        if len(todas_fileiras_no_comprimento) == qtdd_fileiras_no_comprimento:
            #print('ok no comprimento')
            #print(todas_fileiras_no_comprimento)
            for fileira in todas_fileiras_no_comprimento:
                soma_tabuas_no_comprimento += len(fileira)
        '''
        elif len(todas_fileiras_no_comprimento) < qtdd_fileiras_no_comprimento:
            print('impossivel no comprimento')
        else:
            print(f'qdte fileiras no comprimento: {len(todas_fileiras_no_comprimento)}')
        ''' 
        # Define o texto do resultado a ser exibido
        if soma_tabuas_no_comprimento == 0 and soma_tabuas_na_largura == 0:
            texto_resultado = ('Impossível cobrir todo o piso do salão')
        elif soma_tabuas_no_comprimento == 0:
            texto_resultado = 'É possível cobrir todo o piso do salão com ' + str(soma_tabuas_na_largura) + ' tábuas'
        elif soma_tabuas_na_largura == 0:
            texto_resultado = 'É possível cobrir todo o piso do salão com ' + str(soma_tabuas_no_comprimento) + ' tábuas'
        else: 
            texto_resultado = 'É possível cobrir todo o piso do salão com ' + str(min(soma_tabuas_no_comprimento, soma_tabuas_na_largura)) + ' tábuas'
    else:
        #print('impossivel - largura da tabua nao serve')
        texto_resultado = 'Impossivel cobrir todo o piso do salão'
    
    print(todas_fileiras_no_comprimento)

    pygame.init()               # Inicializa o pygame
    largura_tela = 800          # Define as dimensões da tela
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))     # Cria a tela
    
    cor_preta = (0, 0, 0)               # Define a cor do texto (preto neste exemplo)
    fonte = pygame.font.Font(None, 36)  # Define a fonte e o tamanho do texto
    #texto = "Olá, mundo!"              
    texto_tabuas_1 = f'Para uma sala de dimensões {M_largura_sala} x {N_comprimento_sala},'
    texto_tabuas_2 = f'com tábuas de {L_largura_tabuas} cm de largura'
    
    #K_qtde_tabuas + todas_tabuas

    superficie_texto_tabuas_1 = fonte.render(texto_tabuas_1, True, cor_preta)         
    superficie_texto_tabuas_2 = fonte.render(texto_tabuas_2, True, cor_preta)         
                                        # Cria a superfície contendo o texto
    posicao_x_texto_tabuas_1 = 100               # Define a posição do texto na tela
    posicao_y_texto_tabuas_1 = 30
    posicao_x_texto_tabuas_2 = 100               # Define a posição do texto na tela
    posicao_y_texto_tabuas_2 = 60
    
    superficie_texto_resultado = fonte.render(texto_resultado, True, cor_preta)         
                                        # Cria a superfície contendo o texto
    posicao_x_texto_resultado = 100               # Define a posição do texto na tela
    posicao_y_texto_resultado = 90
    
    cor_retangulo = (255, 0, 0)     # Define a cor do retângulo (vermelho neste exemplo)
    posicao_x_retangulo = 100             # Define as coordenadas e dimensões do retângulo
    posicao_y_retangulo = 120
    largura_retangulo = 200
    altura_retangulo = L_largura_tabuas/5

    # Loop principal do jogo
    executando = True
    while executando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False
        tela.fill((255, 255, 255))  # Preenche a tela com uma cor de fundo (branco neste exemplo)
        
        for largura_retangulo in todas_tabuas:
            pygame.draw.rect(tela, cor_retangulo, 
                        (posicao_x_retangulo, posicao_y_retangulo, (int(largura_retangulo)*20), altura_retangulo))  # Desenha o retângulo na tela
            # Desenha a borda do retângulo na tela
            pygame.draw.rect(tela, cor_preta, 
                        (posicao_x_retangulo, posicao_y_retangulo, (int(largura_retangulo)*20), altura_retangulo), 2)
            posicao_y_retangulo =  posicao_y_retangulo + (L_largura_tabuas/5) + 5            

        posicao_x_retangulo = 300
        posicao_y_retangulo = 120

        for fileira in todas_fileiras_no_comprimento:
            for tamanho_tabua in fileira:
                pygame.draw.rect(tela, cor_retangulo, 
                            (posicao_x_retangulo, posicao_y_retangulo, (tamanho_tabua*20), altura_retangulo))  # Desenha o retângulo na tela
                # Desenha a borda do retângulo na tela
                pygame.draw.rect(tela, cor_preta, 
                            (posicao_x_retangulo, posicao_y_retangulo, (tamanho_tabua)*20, altura_retangulo), 2)
                posicao_x_retangulo =  posicao_x_retangulo + ((tamanho_tabua)*20)             
            posicao_x_retangulo = 300
            posicao_y_retangulo = posicao_y_retangulo + (L_largura_tabuas/5)            

        posicao_x_retangulo = 600
        posicao_y_retangulo = 120

        for fileira in todas_fileiras_na_largura:
            for tamanho_tabua in fileira:
                pygame.draw.rect(tela, cor_retangulo, 
                            (posicao_x_retangulo, posicao_y_retangulo, (tamanho_tabua*20), altura_retangulo))  # Desenha o retângulo na tela
                # Desenha a borda do retângulo na tela
                pygame.draw.rect(tela, cor_preta, 
                            (posicao_x_retangulo, posicao_y_retangulo, (tamanho_tabua)*20, altura_retangulo), 2)
                posicao_x_retangulo =  posicao_x_retangulo + ((tamanho_tabua)*20)             
            posicao_x_retangulo = 600
            posicao_y_retangulo = posicao_y_retangulo + (L_largura_tabuas/5)            

        posicao_x_retangulo = 100
        posicao_y_retangulo = 120

        tela.blit(superficie_texto_resultado, (posicao_x_texto_resultado, posicao_y_texto_resultado))     # Desenha a superfície contendo o texto na tela
        tela.blit(superficie_texto_tabuas_1, (posicao_x_texto_tabuas_1, posicao_y_texto_tabuas_1))     # Desenha a superfície contendo o texto na tela
        tela.blit(superficie_texto_tabuas_2, (posicao_x_texto_tabuas_2, posicao_y_texto_tabuas_2))     # Desenha a superfície contendo o texto na tela
        pygame.display.flip()   # Atualiza a tela
    pygame.quit()       # Finaliza o pygame
