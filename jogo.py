import pygame

#inicializar
pygame.init()

tamanho_tela = (800,600)
tela = pygame.display.set_mode(tamanho_tela)

pygame.display.set_caption("JOGO JOKENPÔ")

fonte = pygame.font.SysFont("Arial",32)
posicao_x = 0
posicao_y = 0

cor_branca = (255,255,255)
cor_preta = (0,0,0)


#criar funções do jogo

botao_pedra = pygame.image.load("")
botao_papel = pygame.image.load("")
botao_tesoura = pygame.image.load("")

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

    pygame.display.update()
    

pygame.quit()

