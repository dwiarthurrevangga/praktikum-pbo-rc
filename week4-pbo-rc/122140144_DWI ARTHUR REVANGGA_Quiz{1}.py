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

def play_game():
    board = initialize_board()
    print("Let's play Minesweeper!")
    print("=============================================")
    print_board(board)
    
    bomb_row, bomb_col = place_bomb(board)
    
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
            
            if all(cell != '?' for row in board for cell in row):
                print("You win!")
                break

play_game()
