import sys


def init_board():
    board = [x+1 for x in range(9)]
    return board


def display_board(board):
    class style:
        BOLD = '\033[1m'
        END = '\033[0m'
    for x in range(len(board)):
        if(x % 3 == 0):
            print('\n')
            if(board[x] == '0' or board[x] == 'X'):
                print(style.BOLD + '['+board[x]+']' + style.END, end=" ")
            else:
                print('[{}]'.format(board[x]), end=" ")
        else:
            if(board[x] == 'X' or board[x] == '0'):
                print(style.BOLD + '['+board[x]+']' + style.END, end=" ")
            else:
                print('[{}]'.format(board[x]), end=" ")
    print('\n')
    return


def win_check(board, player):
    win_condition = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for condition in win_condition:
        if (board[condition[0]] == board[condition[1]] == board[condition[2]] == 'X'):
            print('{} won the match'.format(player))
            return True
        elif (board[condition[0]] == board[condition[1]] == board[condition[2]] == '0'):
            print('{} won the match'.format(player))
            return True
    return False


def mark_board(board, choice, mark):
    board[int(choice) - 1] = mark
    return board


if __name__ == '__main__':
    try:
        board = init_board()

        player1 = input('Enter Player 1 Name : ')
        print("Hi {}! You will play with sign 'X'.".format(player1.upper()))
        player2 = input('Enter Player 2 Name : ')
        print("Hi {}! You will play with sign 'O'.".format(player2.upper()))
        win_result = False
        player_list = (player1.upper(), player2.upper())
        attempt = 0
        display_board(board)

        while(win_result != True and attempt != 9):
            player = ''
            mark = ''
            if(attempt % 2 == 0):
                player = player_list[0]
                mark = 'X'
            else:
                player = player_list[1]
                mark = '0'
            player_choice = input('Attempt {} : {} enter index of your play choice [{}] : '.format(
                attempt+1, player, mark))
            if(player_choice.isnumeric()):
                if(int(player_choice) >= 1 and int(player_choice) <= 9):
                    if((board[int(player_choice)-1] != 'X') and (board[int(player_choice)-1] != '0')):
                        board[int(player_choice)-1] = mark
                        display_board(board)
                        win_result = win_check(board, player)
                        attempt += 1
                        continue
                    else:
                        print(
                            'Selected choice is already marked. Please enter valid choice.')
                        continue
                else:
                    print('Please enter choice within range 1-9')
                    continue
            else:
                print("Please enter Integer choice.")
                continue
        if(win_result == False):
            print('Match Draw!')

    except KeyboardInterrupt:
        print("\nBye Bye!")
        sys.exit()
