# Tic Tac Toe.


def Play_Board():

    Board = [["", "", ""],
            ["", "", ""],
            ["", "", ""]]
    
    return (Board)

##############################################################################

# Declare Symbol for players

def Players():

    Player_1 = str(input("Hey Player_1, please select your symbol ('x') or ('o'): "))
    print("")

    Player_2 =""
    
    while ((Player_1 != 'x') and (Player_1 != 'o')):

        print ("Your entry is not valid, please enter 'x' or 'o': \n")

        Player_1 = str(input("Hey Player_1, please select your symbol ('x') or ('o'): "))

        print("")

    if (Player_1 == 'x'):

        Player_2 += 'o'

        print("Hey Player_1, your symbol is (x) \n")

        print("Hey Player_2, your symbol is (o) \n")
        
    elif (Player_1 == 'o'):
        
        Player_2 += 'x'

        print("Hey Player_1, your symbol is (o) \n")

        print("Hey Player_2, your symbol is (x) \n")
    
    return(Player_1, Player_2)

###############################################################################

# Declare who is playing

def Player_Turn(T, Player_1, Player_2):

    if T % 2 == 1:

        Chance = Player_1

    elif T % 2 == 0:

        Chance = Player_2
    
    return (Chance)

###############################################################################

# Players choosing their square

def Entries():

    Row = (int(input("Enter the Row Value: ")) - 1)

    print("")

    Column = (int(input("Enter the Column Value: ")) - 1)

    print("")

    return(Row, Column)

###############################################################################

# Checking if the given rows and columns are within the limit 

def Limit_Check(Row, Column):
    
# Checking if Row or Column Value is out of Range:

    while ((Row < 0) or (Row > 2)) or ((Column < 0) or (Column > 2)):
        
        if ((Row < 0) or (Row > 2)):

            print("The given Row value is out of range. \n")

            Row = (int(input("Enter the Row Number again: ")) - 1)

            print("")

            Column = (int(input("Enter the Column Number again: ")) - 1)

            print("")
            
        else:

            print("The given Column value is out of range. \n")

            Row = (int(input("Enter the Row Number again: ")) - 1)

            print("")

            Column = (int(input("Enter the Column Number again: ")) - 1)

            print("")
    
    return(Row, Column)

###################################################################################
       
#Checking if the square is already filled.

def Board_Check(Board, Player_1, Player_2, Row, Column):

    while ((Board[Row][Column] == Player_1) or (Board[Row][Column] == Player_2)):
        
        if (Board[Row][Column] == Player_1):
            
            print("The square is already  with " + "(" + str(Player_1)+ ")" + ". Please slect different square. \n")

        elif (Board[Row][Column] == Player_2):
            
            print("The square is already  with " + "(" + str(Player_2)+ ")" + ". Please slect different square. \n")

            
        else:
            
            pass

        Row = (int(input("Enter the Row Number: "))-1)
        print("")
        Column = (int(input("Enter the Column Number: "))-1)
        print("")

        Row, Column = Limit_Check(Row, Column)

    return(Row, Column)

###################################################################################

# Entering the players symbol in the square.

def Board_Entry(Board, Turn, Row, Column):

    Board[Row][Column] += Turn

    return(Board)