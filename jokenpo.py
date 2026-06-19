import random

comp1, comp2, comp3 = 1,2,3  #variaveis do computador

pontousuario = 0
pontocomputador = 0
pontoempate = 0
computador = random.randint(1,3)

print('----------JOGO DE JOKENPÔ----------')
print('/Para encerrar o jogo digite 0/')

while True:
    escolha = int(input("Escolha pedra[1], papel[2] ou tesoura[3]: "))

    if escolha == 0:
        print('JOGO ENCERRADO!')
        break
    else:
        if escolha < 1 or escolha > 3:
            print(f"ERRO, o número {escolha} não foi encontrado.")
        else:
            computador = random.randint(1,3)
    print(f'Escolha do computador: {computador}')

    if escolha == 1 and computador == comp1 or escolha == 2 and computador == comp2 or escolha == 3 and computador == comp3:
        pontousuario+=0
        pontocomputador+=0
        pontoempate+=1
        print('-->EMPATE')
        print('-'*30)
    elif escolha == 1 and computador == comp3 or escolha == 3 and computador == comp2 or escolha == 2 and computador == comp1:
        pontousuario+=1
        print('-->Ponto para USUÁRIO')
        print('-'*30)
    else:
        pontocomputador+=1
        print('-->Ponto para COMPUTADOR')
        print('-'*30)

print('---------------PLACAR---------------')
print(f'Pontos totais do USUÁRIO: {pontousuario} pontos')
print(f'Pontos totais COMPUTADOR: {pontocomputador} pontos')
print(f'Pontos totais do EMPATE: {pontoempate} pontos')
print('-'*36)

if pontousuario > pontocomputador:
    print("****************************")
    print("   PARABÉNS, VOCÊ GANHOU!   ")
    print("****************************")
elif pontocomputador > pontousuario:
    print("****************************")
    print("        VOCÊ PERDEU!        ")
    print("****************************")
else:
    print("****************************")
    print("          EMPATE            ")
    print("****************************")



