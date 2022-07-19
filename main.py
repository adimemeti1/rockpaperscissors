def RockPaperScissors():
    play=input('Do you want to play this game:')
    while play != 'yes':
        print('OK')
        break
    else:
        print('This game called Rock Paper Scissors')
        print('I hope you know how  to play\nThis game played with 2 players!:')
        player1=input('Chose:Rock----Paper-------Scissors')
        player2=input('Chose:Rock----Paper-------Scissors')
        if player1=='Rock' and player2=='Scissors':
            print('Player1 win!\nLuck next time Player2')
        elif player1=='Scissors' and player2=='Rock':
            print('Player2 win!\nLuck next time Player1')
        elif player1=='Rock' and player2=='Paper':
            print('Player2 win!\nLuck next time Player1')
        elif player1=='Paper'and player2=='Rock':
            print('Player1 win!\nLuck next time Player2')
        elif player1=='Scissors' and player2 =='Paper':
            print('Player1 win!\nLuck next time Player2')
        elif player1=='Paper'and player2=='Scissors':
            print('Player2 win!\nLuck next time Player1')
RockPaperScissors()
