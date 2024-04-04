import random

def initialize_board():
    return [['?' for _ in range(3)] for _ in range(3)]

def place_bomb(board):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    return row, col

def print_board(board):
    for row in board:
        print(' '.join(row))

def count_safe_box(board):
    return sum(row.count('?') for row in board)

def play_game():
    board = initialize_board()
    print("Let's play Minesweeper!")
    print("=============================================")
    print_board(board)
    
    bomb_row, bomb_col = place_bomb(board)
    safe_box = 9
    
    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        
        if (row, col) == (bomb_row, bomb_col):
            print("BOOM! Game Over!")
            board[bomb_row][bomb_col] = 'X'
            print_board(board)
            print("=============================================")
            break
        else:
            print("Not a bomb, keep going!")
            print("=============================================")
            board[row][col] = 'O'
            print_board(board)
            
            safe_box -= 1
            if safe_box == 0:
                print("=============================================")
                print("You win!")
                board[bomb_row][bomb_col] = 'X'
                print_board(board)
                break

play_game()
