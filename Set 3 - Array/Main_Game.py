from Tic_Tac_Toe import *

def main():

    T = 1

    Board = [["", "", ""], ["", "", ""], ["", "", ""]]

    Row, Column = ("", "")

    Player_1, Player_2 = Players()

    while T != 10:

        Turn = Player_Turn(T, Player_1, Player_2)

        if Turn == Player_1:

            print("Player_1 it is your turn \n")

            print("")

        elif Turn == Player_2:

            
            print("Player_2 it is your Turn \n")

            print("")

        Row, Column = Entries()

        Row, Column = Limit_Check(Row, Column)

        Row, Column = Board_Check(Board, Player_1, Player_2, Row, Column)

        Board = Board_Entry(Board, Turn, Row, Column)

        print(Board)
        print("")

        T+=1

    print ("Final Board \n")
    print(Board)

if __name__=="__main__":

    main()

