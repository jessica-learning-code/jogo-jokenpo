import pygame

#inicializar
pygame.init()

tamanho_tela = (800,600)
tela = pygame.display.set_mode(tamanho_tela)

pygame.display.set_caption("JOGO JOKENPÔ")

fonte = pygame.font.SysFont("Arial",32)
posicao_x = 0
posicao_y = 0

#cores
cor_branca = (255,255,255)
cor_preta = (0,0,0)


#criar funções do jogo
botao_pedra = pygame.image.load("pedra.png")
botao_papel = pygame.image.load("papel.png")
botao_tesoura = pygame.image.load("tesoura.png")

#mudar o tamanho dos ícones
botao_pedra = pygame.transform.scale(botao_pedra,(100,80))
botao_papel = pygame.transform.scale(botao_papel,(100,80))
botao_tesoura = pygame.transform.scale(botao_tesoura,(100,80))



#desenhar na tela

#criar loop infinito
fim_jogo = False

while not fim_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    tela.fill(cor_preta)#limpar a tela para desenhar o próximo frame(quadro)

    texto = fonte.render("/Para encerrar o jogo digite 0/", True, cor_branca)
    tela.blit(texto,(posicao_x,posicao_y))

    #fazer a imagem imprimir na tela
    rect_pedra = botao_pedra.get_rect(topleft=(100,400))
    tela.blit(botao_pedra, rect_pedra)
    rect_papel = botao_papel.get_rect(topleft=(150,510))
    tela.blit(botao_papel, rect_papel)
    rect_tesoura = botao_tesoura.get_rect(topleft=(200,420))
    tela.blit(botao_tesoura, rect_tesoura)

    pygame.display.update()
    

pygame.quit()

