'''
Primeiro jogo em python + pygame

Criando uma tela de fundo usando o modula display
com a função display.set_mode():

'''

import pygame 
from random import randrange
from pygame.locals import *

# definido tuplas de 3 valores para dar cor ao programas
# podendo procurar mais cores no site cloford.com/resources/colours/500col.htm
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)


# testando se está funcionado o pygame 
try: 
    pygame.init()
except: 
    print ('O modulo pygame não foi inicializado com sucesso!')

    
# crie duas variáveis

largura = 320
altura = 280
tamanho = 10
placar = 40

# definido o frame do jogo
# calculando o tempo
relogio = pygame.time.Clock()

# comando para abrir a tela 
fundo = pygame.display.set_mode((largura, altura))

# dando nome a tela
pygame.display.set_caption("Snake")

# criando a fonte das letras e tamanho


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, 15) 
    texto1 = font.render(msg, True, cor)
    # função para escrever o texto na tela
    fundo.blit(texto1, [x, y])

# desenhando a cobra
def cobra(cobraXY):
    for XY in cobraXY:
        #início da cobrinha
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])
        #testando a cobrinha
        #pos_x += 0.1

# definido a maça
def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])

def jogo():    
    #criando ideia de movimento, loop infinito no jogo para poder sair
    sair = True
    fimDeJogo = False
    '''
    # from random import randint
    # deixando aleatório a posição da cobra ao iniciar
    pos_x = randint(0, (largura-tamanho)/10)*10
    pos_y = randint(0, (altura-tamanho)/10)*10
    maca_x = randint(0, (largura-tamanho)/10)*10
    maca_y = randint(0, (altura-tamanho)/10)*10
    '''
    # deixando aleatório a posição da cobra ao iniciar
    pos_x = randrange (0, largura-tamanho, 10)
    pos_y = randrange (0, altura-tamanho - placar , 10)
    maca_x = randrange (0, largura-tamanho, 10)
    maca_y = randrange (0, altura-tamanho - placar, 10)    
    velocidade_x = 0
    velocidade_y = 0
    cobraXY = [] 
    cobraComp = 1
    pontos = 0
    
    while sair:
        while fimDeJogo:
            # se tiver na tela na tela de fim de jogo ou no jogando para poder sair
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimDeJogo = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            sair = True
                            fimDeJogo = False
                            pos_x = randrange (0, largura-tamanho, 10)
                            pos_y = randrange (0, altura-tamanho - placar ,10)
                            maca_x = randrange (0, largura-tamanho, 10)
                            maca_y = randrange (0, altura-tamanho - placar, 10)
                            velocidade_x = 0
                            velocidade_y = 0
                            cobraXY = [] 
                            cobraComp = 1
                            pontos = 0
                        if event.key == pygame.K_s:
                            sair = False
                            fimDeJogo = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if x > 45 and y > 120 and x < 180 and y < 147:
                            sair = True
                            fimDeJogo = False
                            pos_x = randrange (0, largura-tamanho, 10)
                            pos_y = randrange (0, altura-tamanho - placar ,10)
                            maca_x = randrange (0, largura-tamanho, 10)
                            maca_y = randrange (0, altura-tamanho - placar, 10)
                            velocidade_x = 0
                            velocidade_y = 0
                            cobraXY = [] 
                            cobraComp = 1
                            pontos = 0
                        elif x > 190 and y > 120 and x < 265 and y < 147:
                            sair = False
                            fimDeJogo = False
            fundo.fill(branco)
            texto("Fim de jogo", vermelho, 50, 65, 30 )
            texto("PONTUAÇÃO FINAL: " + str(pontos),preto, 30, 70 ,80 )
            #desenhando botão
            pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
            texto("Continuar(C)", branco, 30, 50, 125)
            pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
            texto("Sair (S)", branco, 30, 195, 125)
            pygame.display.update()
            
        for event in pygame.event.get():
            # fechando o jogo no x da janela
            if event.type == pygame.QUIT:
                sair = False
            #função do teclado para movimento
            if event.type == pygame.KEYDOWN:
                # se o objeto está se movendo em uma direção não pode mover para a direção oposta
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    # pos_x -= 10
                    velocidade_y = 0
                    velocidade_x -= tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != - tamanho:
                    #pos_x += 10
                    velocidade_y = 0
                    velocidade_x += tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    #pos_y -= 10
                    velocidade_x = 0
                    velocidade_y -= tamanho
                if event.key == pygame.K_DOWN and velocidade_y != - tamanho:
                    #pos_y += 10
                    velocidade_x = 0
                    velocidade_y += tamanho
                if event.key == pygame.K_SPACE:
                    cobraComp += 1
        
        if sair:           
            # print(event)
            # preenche a tela com fundo da cor escolhida
            fundo.fill(branco)  
            # deixando interativo
            pos_x += velocidade_x
            pos_y += velocidade_y
        
            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0, largura-tamanho, 10)
                maca_y = randrange(0, altura-tamanho - placar, 10)
                cobraComp += 1
                pontos +=1
                
        '''
        Quando o objeto chega na borda finaliza o jogo
            if pos_x + tamanho > largura:
                fimDeJogo = True
            if pos_x < 0:
                fimDeJogo = True
            if pos_y + tamanho > altura - placar:
                fimDeJogo = True
            if pos_y < 0:
                fimDeJogo = True
        '''
        # quando o objeto chega na borda passa para o outro lado
        if pos_x + tamanho > largura:
            pos_x = 0
        if pos_x < 0:
            pos_x = largura - tamanho
        if pos_y + tamanho > altura - placar:
            pos_y = 0
        if pos_y < 0:
            pos_y = altura - tamanho - placar
        # chamando a função cobra
        # criando tamanho da cobra e a cabaça
        
        #cabeça
        cobraInicio = []
        cobraInicio.append(pos_x)
        cobraInicio.append(pos_y)
        cobraXY.append(cobraInicio)
        if len (cobraXY) > cobraComp:
            del cobraXY[0]
        if any (bloco == cobraInicio for bloco in cobraXY[: - 1]):
            fimDeJogo = True
        
        # desenhando o placar
        pygame.draw.rect(fundo, preto, [0, altura - placar, largura, placar])
        texto("PONTUAÇÃO: " + str(pontos), branco, 20, 10, altura - 30)
        
        cobra(cobraXY)
        # definindo quando a cobra come a maçã e aumenta o tamanho
        maca(maca_x, maca_y)
        # definindo a velocidade, quantidade de frame por segundo
        relogio.tick(10)
        pygame.display.update()   


#inicializando o jogo, chamando a função jogo  
jogo()
# função para encerrar o programa
pygame.quit()