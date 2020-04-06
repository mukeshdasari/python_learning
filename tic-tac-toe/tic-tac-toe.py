def init_board():
    board = [x+1 for x in range(9)]
    return board

def display_board(board):
    class style:
        BOLD = '\033[1m'
        END = '\033[0m'  
    for x in range(len(board)):  
        if(x%3 == 0):
            print('\n')
            if(board[x] == '0' or board[x] == 'X'):
                print(style.BOLD + '['+board[x]+']' + style.END, end =" ")
            else:
                print('[{}]'.format(board[x]), end =" ")
        else:
            if(board[x] == 'X' or board[x] == '0'):
                print(style.BOLD + '['+board[x]+']' + style.END, end =" ")
            else:
                print('[{}]'.format(board[x]), end =" ")
    print('\n')
    return

def win_check(board):
    win_condition = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2, 4, 6]]
    for condition in win_condition:
        if (board[condition[0]] == board[condition[1]] == board[condition[2]] == 'X'):
            return 'player1'
        elif (board[condition[0]] == board[condition[1]] ==  board[condition[2]] == '0'):
            return 'player2'
    return False
 
def mark_board(board, choice, mark):
    board[int(choice) - 1] = mark
    return board

if __name__ == '__main__':
    board = init_board()
    win_result = win_check(board)
    player1 = input('Enter Player 1 Name : ')
    print("Hi {}! You will play with sign 'X'.".format(player1.upper()))
    player2 = input('Enter Player 2 Name : ')
    print("Hi {}! You will play with sign 'O'.".format(player2.upper()))
    attempt = 0
    display_board(board)

    while (win_result == False):
        player1_choice = input('Attempt {} : {} enter index of your play choice (X) : '.format(attempt+1, player1.upper()))
        board = mark_board(board, player1_choice, 'X')
        attempt += 1
        display_board(board)
        win_result = win_check(board)
        if (win_result != False or attempt == 9):
            break
        player1_choice = input('Attempt {} : {} enter index of your play choice (0) : '.format(attempt+1, player2.upper()))
        board = mark_board(board, player1_choice, '0')
        attempt += 1
        display_board(board)
        win_result = win_check(board)
        if (win_result != False):
            break


    if(win_result == 'player1'):
        print("{} won the match.".format(player1.upper()))
    elif(win_result == 'player2'):
        print("{} won the match.".format(player2.upper()))
    else:
        print("Match draw.")


