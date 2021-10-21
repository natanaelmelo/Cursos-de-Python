import random

# Apresentação do jogo e decisão de jogar
print('Seja bem vindo ao jogo pedra papel e tesoura!')
choice = str(input('Você deseja jogar [S/N]: ')).upper()

# Loop para que o usuário escolha a opção correta
while choice != 'S' and choice != 'N':
    print('\nERRO: Opção invalidade, escolha apenas com S ou N. Vamos tentar de novo?')
    choice = str(input('Você deseja jogar [S/N]: ')).upper()

# Se o usuário escolhe jogar
if choice == 'S':

    # Loop para jogar de novo após as rodadas acabar
    flag = 0  # Flag para sair do loop

    while flag != 1:

        # Por quantas rodadas o usuário deseja jogar
        rounds = int(input('\nPor quantas rodadas deseja jogar: '))
        print('\n')

        # Variaveis para armazenar de rodadas e o placar
        game = score_comp = score_user = 0

        # Loop para que o usuário continue jogando até atingir a quantidade de rodadas desejada
        while game < rounds:

            # Escolha do usuário
            print(f'RODADA {game + 1}')
            user_action = str(input("Faça sua escolha entre pedra, papel ou tesoura: ")).lower()

            # Escolha do computador
            possible_actions = ['pedra', 'papel', 'tesoura']
            computer_action = random.choice(possible_actions)

            # Determinar o ganhador
            # Quando ambos escolhem a mesma coisa
            if user_action == computer_action:
                print(
                    f'Você escolheu {user_action} e o compuatdor escolheu {computer_action}, portanto houve um empate!')
                print('Tente de novo! \n')
                game += 1

            # Usuário escolhe pedra
            elif user_action == 'pedra':
                # Computador escolhe papel
                if computer_action == 'papel':
                    print(
                        f'Você escolheu {user_action} e o compuatdor escolheu {computer_action}, portanto o computador ganhou e você perdeu!')
                    print('Sinto muito! \n')
                    score_comp += 1
                    game += 1

                # Computador escolhe tesoura
                elif computer_action == 'tesoura':
                    print(
                        f'Você escolheu {user_action} e o computador escolheu {computer_action}, portanto você ganho e o computador perdeu!')
                    print('Parabéns! \n')
                    score_user += 1
                    game += 1

            # Usuário escolheu papel
            elif user_action == 'papel':
                # Computador escolhe pedra
                if computer_action == 'pedra':
                    print(
                        f'Você escolheu {user_action} e o compuatdor escolheu {computer_action}, portanto você ganho e o computador perdeu!')
                    print('Parabéns! \n')
                    score_user += 1
                    game += 1

                # Computador escolhe tesoura
                elif computer_action == 'tesoura':
                    print(
                        f'Você escolheu {user_action} e o computador escolheu {computer_action}, portanto o computador ganhou e você perdeu!')
                    print('Sinto muito! \n')
                    score_comp += 1
                    game += 1

            # Usuário escolhe tesoura
            elif user_action == 'tesoura':
                # Computador escolhe pedra
                if computer_action == 'pedra':
                    print(
                        f'Você escolheu {user_action} e o computador escolheu {computer_action}, portanto o computador ganhou e você perdeu!')
                    print('Sinto muito! \n')
                    score_comp += 1
                    game += 1

                # Computador escolhe papel
                elif computer_action == 'papel':
                    print(
                        f'Você escolheu {user_action} e o computador escolheu {computer_action}, portanto você ganho e o computador perdeu!')
                    print('Parabéns! \n')
                    score_user += 1
                    game += 1

        # Informar que o jogo já atingiu a rodadas
        print(f'Você acabou de atingir {game} rodadas')

        # Se o computador ganhar
        if score_comp > score_user:
            print(f'E você PERDEU, porque o placar ficou {score_comp} x {score_user} para o computador!')
            print('Boa sorte na proxima! \n')

        # Se o usuário ganhar
        elif score_user > score_comp:
            print(f'E você GANHOU, porque o placar ficou {score_user} x {score_comp} para você!')
            print('Parabéns! \n')

        # Se houver empate
        else:
            print(f'EMPATOU o jogo, o placar ficou {score_user} x {score_comp} para vocês!')
            print('Não foi dessa vez! \n')

        # Perguntar se o usuário deseja jogar novamente
        again = str(input('Você deseja jogar de novo [S/N]: ')).upper()

        # Loop para que o usuário escolha a opção correta
        while again != 'S' and again != 'N':
            print('\nERRO: Opção invalidade, escolha apenas com S ou N. Vamos tentar de novo?')
            again = str(input('Você deseja jogar de novo [S/N]: ')).upper()

        # Concional para jogar de novo ou sair do jogo
        # Caso o usuário deseje jogar novamente
        if again == 'S':
            flag = 0

        # Caso o usuário não desejar jogar novamente
        else:
            print('Obrigado por jogar com a gente! Se desejar jogar de novo, já sabe né? hehehehe')
            flag = 1

# Se o usuário não desejar jogar
else:
    print('Se desejar jogar, é só executar o jogo novamente!')
