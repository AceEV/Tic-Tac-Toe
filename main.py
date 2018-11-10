from helper import *


board = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
turns = 0
play = 'y'


if __name__ == '__main__':
    while play.lower().strip() == 'y':
        while turns < 9 :
            if(turns % 2 == 0):
                print("Player 1 plays\n")
                print("\n",print_board(board),"\n")
                try:
                    r = int(input("Row : "))
                    c = int(input("Coulmn : "))
                
                    if board[r-1][c-1] == '0':
                        board[r-1][c-1] = 'X'
                        turns += 1
                        if check_for_winner(board, 'X', r-1, c-1):
                            print("\n",print_board(board),"\n")
                            print("\n**** PLAYER 1 WINS ****\n")
                            break
                    else:
                        print("Invalid play. Try again\n")
                        continue
                except:
                    print("Invalid Numbers1. Try again\n")
                    continue
                

            else:
                print("Player 2 plays")
                print("\n",print_board(board),"\n")
                try:
                    r = int(input("Row : "))
                    c = int(input("Coulmn : "))
                
                    if board[r-1][c-1] == '0':
                        board[r-1][c-1] = 'O'
                        turns += 1
                        if check_for_winner(board, 'O', r-1, c-1):
                            print("\n",print_board(board),"\n")
                            print("\n**** PLAYER 2 WINS ****\n")
                            break
                    else:
                        print("Invalid play. Try again\n")
                        continue
                except:
                    print("Invalid Numbers2. Try again\n")
                    continue

        if turns == 10:
            print("\n**** MATCH TIED ****\n")
        play = input("\nPlay again? (y/n) : ")
        board = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        turns = 0
        