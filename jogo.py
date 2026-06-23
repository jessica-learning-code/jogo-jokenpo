import pygame
import random

#inicializar
pygame.init()

#tamanho da tela 
tamanho_tela = (800,600)
tela = pygame.display.set_mode(tamanho_tela)

pygame.display.set_caption("JOGO JOKENPÔ")

#fontes para as escrituras na tela
fonte = pygame.font.SysFont("timesnewroman",30)
fonte2 = pygame.font.SysFont("timesnewroman",25)



#cores
cor_branca = (255,255,255)
cor_preta = (0,0,0)
cor_verde = (0,255,0)
cor_roxa = (128,0,255)
cor_amarela = (0,128,128)

#criar funções do jogo
botao_pedra = pygame.image.load("pedra.png")
botao_papel = pygame.image.load("papel.png")
botao_tesoura = pygame.image.load("tesoura.png")

#mudar o tamanho dos ícones
botao_pedra = pygame.transform.scale(botao_pedra,(40,40))
botao_papel = pygame.transform.scale(botao_papel,(40,40))
botao_tesoura = pygame.transform.scale(botao_tesoura,(40,40))

#informa a posição das imagens
rect_pedra = botao_pedra.get_rect(topleft=(100,130))
rect_papel = botao_papel.get_rect(topleft=(350,130))
rect_tesoura = botao_tesoura.get_rect(topleft=(600,130))

#criar loop finito
fim_jogo = False
imagem_computador = None

#contador de pontos
pontousuario = 0
pontocomputador = 0
pontoempate = 0

while not fim_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

        #usuario escolheu pedra
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_pedra.collidepoint(evento.pos):
                escolha = 1
                computador = random.randint(1,3) 
                if computador == 1:
                    imagem_computador = botao_pedra
                    pontoempate+= 1
                elif computador == 2:
                    imagem_computador = botao_papel
                    pontocomputador+= 1
                else:
                    imagem_computador = botao_tesoura
                    pontousuario+= 1

            #usuario escolheu papel
            elif rect_papel.collidepoint(evento.pos):
                escolha = 2
                computador = random.randint(1,3)   
                if computador == 1:
                    imagem_computador = botao_pedra
                    pontousuario+= 1
                elif computador == 2:
                    imagem_computador = botao_papel
                    pontoempate+= 1
                else:
                    imagem_computador = botao_tesoura
                    pontocomputador+= 1

            #usuario escolheu tesoura       
            elif rect_tesoura.collidepoint(evento.pos):
                escolha = 3
                computador = random.randint(1,3)
                if computador == 1:
                    imagem_computador = botao_pedra 
                    pontocomputador+= 1
                elif computador == 2:
                    imagem_computador = botao_papel
                    pontousuario+= 1
                else:
                    imagem_computador = botao_tesoura
                    pontoempate+= 1
    

    #limpar a tela para desenhar o próximo frame(quadro)
    tela.fill(cor_amarela)

    #fazer a imagem imprimir na tela
    tela.blit(botao_pedra, rect_pedra)
    tela.blit(botao_papel, rect_papel)
    tela.blit(botao_tesoura, rect_tesoura)

    #Frases escritas na tela
    texto = fonte.render("~~~~~~~~~~~~~~~~~~JOGO JOKENPÔ~~~~~~~~~~~~~~~~~~", True, cor_preta)
    tela.blit(texto,(0,10))
    texto2 = fonte2.render("Faça sua escolha ", True, cor_branca)
    tela.blit(texto2,(30,80))

    if imagem_computador != None:
        texto3 = fonte2.render(f"Escolha do computador:", True, cor_branca)
        tela.blit(texto3,(15,220))
        tela.blit(imagem_computador,(270,220))

    texto4 = fonte2.render(f"Pontos COMPUTADOR: {pontocomputador}", True, cor_verde)
    tela.blit(texto4,(15,300))

    texto5 = fonte2.render(f"Pontos USUÁRIO: {pontousuario}", True, cor_verde)
    tela.blit(texto5,(15,350))

    texto6 = fonte2.render(f"Pontos EMPATE: {pontoempate}", True, cor_verde)
    tela.blit(texto6,(15,400))
    

    pygame.display.update()
pygame.quit()

