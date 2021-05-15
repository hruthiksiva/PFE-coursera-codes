def printblock(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

def printresults(score):
    print("\t--------------------------------")
    print("\t\t    ScoreBoard")
    print("\t--------------------------------")
    for key,value in score.items():
        print("\t   ", key, "\t    ", value)
    print("\t--------------------------------")
    pass

def checkwin(playerpos,curplayer):
    soln=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in soln:
        if all(y in playerpos[curplayer] for y in i):
            return True
    return False

def checkdraw(playerpos):
    if(len(playerpos['X']+playerpos['O'])==9):
        return True
    return False

def singlegame(curplayer):
    values=[' ' for i in range(9)]
    playerpos={'X':[],'O':[]}

    while True:
        printblock(values)
        try:
            move=int(input(f"Player  {curplayer}  turn. Which box?"))

        except ValueError:
            print("Wrong Input Try Again")
            continue

        if move<1 and move>9:
            print("Wrong input try again")
            continue
        if values[move-1]!=' ':
            print("Place filled Try Different Number")
            continue
        values[move-1]=curplayer
        playerpos[curplayer].append(move)

        if checkwin(playerpos,curplayer):
            printblock(values)
            print("Player ", curplayer, " has won the game!!")     
            print("\n")
            return curplayer

        if checkdraw(playerpos):
            printblock(values)
            print("Match Drawn")     
            print("\n")
            return 'D'

        if curplayer == 'X':
            curplayer = 'O'
        else:
            curplayer = 'X'

if __name__ == '__main__':

    print("Player 1")
    player1=input("Enter Player Name 1 : ")
    print("\nPlayer 2")
    player2=input("Enter Player Name 2 : ")
    print("\n")

    curplayer=player1
    playerchoice={"X":"","O":""}

    score={player1:0,player2:0}
    printresults(score)

    options = ['X', 'O']

    while True:
        print('''
    Turn to choose for hruthik
    Enter 1 for X
    Enter 2 for O
    Enter 3 to Quit\n''')

        try:
            choice=int(input())
        except ValueError:
            print("Error in choosing choice! try again")
            continue
        
        if choice>=1 and choice<=3:
            print("Error in choosing choice! try again")
            if choice==1:
                playerchoice["X"]=curplayer
                if playerchoice["X"]==player1:
                    playerchoice["O"]==player2
                else:
                    playerchoice["X"]==player1
            elif choice==2:
                playerchoice["O"]=curplayer
                if playerchoice["O"]==player1:
                    playerchoice["O"]==player2
                else:
                    playerchoice["O"]==player1
            else:
                print("\tFinal Score Board")
                printresults(score)
                break
        else:
            print("Wrong Choice Try Again")    
            continue

        winner=singlegame(options[choice-1])

        if winner!='D':
            playerwon=playerchoice[winner]
            score[playerwon]+=1
        
        printresults(score)

        # Switch player who chooses X or O
        if curplayer == player1:
            curplayer = player2
        else:
            curplayer = player1


            

            


