#Name:Alex Pierce CSCI220-03
#ticTacToe.py

#Purpose:Create program that generates a game of tic-tac-toe.

#Inputs:"X" and "O" from user 

#Outputs: Tic-tac-toe gameboard and gameplay to monitor

#Certification: I certify that this lab is entirely my own work with help from CS lab.

from graphics import *

def buildBoard():
    board=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def displayBoard():
    winWidth = 400
    winHeight = 400
    win = GraphWin("Tic-Tac-Toe", winWidth, winHeight)
    #instructions
    instPt = Point(winWidth/2, winHeight-10)
    instructions = Text(instPt,"Click to place an X or O")
    instructions.draw(win)
    board = Rectangle(Point(35,40), Point(360,345))
    board.setWidth(8)
    board.setFill("Azure")
    board.draw(win)
    line1=Line(Point(35,240), Point(360,240))
    line1.setWidth(8)
    line1.draw(win)
    line2=Line(Point(35,140), Point(360,140))
    line2.setWidth(8)
    line2.draw(win)
    line3=Line(Point(143,40), Point(143,345))
    line3.setWidth(8)
    line3.draw(win)
    line4=Line(Point(255,40), Point(255,345))
    line4.setWidth(8)
    line4.draw(win)
    return win

def isLegal(board, spot):
    if spot > 0 and spot < 10:
        if board[spot-1] != "X" and board[spot-1] != "O":
            return True
    return False  
    
def fillSpot(board, spot, char):
    if isLegal(board, spot) == True:
        board[spot-1]= char 


def isGameWon(board):
    if board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True 
    return False 

def isGameOver(board, numPlays):
    if isGameWon(board) == True:
        return True
    elif numPlays >= 9: 
        return True 
    return False

def playGame(board):
    playing = True
    win = displayBoard()
    board=buildBoard()
    numPlays=0
    while playing:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
        if numPlays%2 == 0:
            player = "X"
        else:
            player = "O"
        #row 1- [0,1,2]
        if 35 < x < 143 and 40 < y < 140:
            center= Text(Point(89,90),player)
            center.setSize(36)
        elif 143 < x < 255 and 40 < y < 140:
            center= Text(Point(199,90),player)
            center.setSize(36)
        elif 255 < x < 360 and 40 < y < 140:
            center= Text(Point(307.5,90),player)
            center.setSize(36)
        #row 2- [3,4,5]
        elif 35 < x < 143 and 140 < y < 240:
            center= Text(Point(89,190),player)
            center.setSize(36)
        elif 143 < x < 255 and 140 < y < 240:
            center= Text(Point(199,190),player)
            center.setSize(36)
        elif 255 < x < 360 and 140 < y < 240:
            center= Text(Point(307.5,190),player)
            center.setSize(36)
        #row3- [6,7,8]
        elif 35 < x < 143 and 240 < y < 345:
            center= Text(Point(89,292.5),player)
            center.setSize(36)
        elif 143 < x < 255 and 240 < y < 345:
            center= Text(Point(199,292.5),player)
            center.setSize(36)
        elif 255 < x < 360 and 240 < y < 345:
            center= Text(Point(307.5,292.5),player)
            center.setSize(36)
        center.draw(win)
        numPlays+=1
       
playGame(buildBoard())


#def main():
##    # Test buildBoard() -> list
##    board = buildBoard()
##    print("The board:", board)
##    print()
##
##    # Test displayBoard(list) -> void
##    displayBoard(board)
##    print()
##
##    # Test isLegal(board, spot) -> boolean
##    sampleBoard = ['x', 2, 'o', 4, 'x', 6, 'o', 8, 9]
##    inBoundsTest = isLegal(sampleBoard, 2)
##    outBoundsTest = isLegal(sampleBoard, 10)
##    spotTakenTestX = isLegal(sampleBoard, 1)
##    spotTakenTestO = isLegal(sampleBoard, 3)
##    print("The in bounds test is", inBoundsTest, "and should be True.")
##    print("The out bounds test is", outBoundsTest, "and should be False.")
##    print("The spot taken text x is", spotTakenTestX, "and should be False.")
##    print("The spot taken test o is", spotTakenTestO, "and should be False.")
##    print()
##
##    # Test fillSpot(board, spot, char) -> void
##    sampleBoard = ['x', 2, 'o', 4, 'x', 6, 'o', 8, 9]
##    print("Sample board before fill:", sampleBoard)
##    fillSpot(sampleBoard, 2, 'x')
##    print("Sample board after fill x on spot 2:", sampleBoard)
##    fillSpot(sampleBoard, 4, 'o')
##    print("Sample board after fill o on spot 4:", sampleBoard)
##    fillSpot(sampleBoard, 1, 'o')
##    print("Sample board after fail fill o on spot 1:", sampleBoard)
##    print()
##
##    # Test isGameWon(board) -> boolean
##    gameWonBoardHorizontal = ['o', 'o', 'o', 4, 5, 6, 7, 8, 9]
##    gameWonBoardDiagonal = ['o', 2, 3, 4, 'o', 6, 7, 8, 'o']
##    gameNotWonBoard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
##    print("Game won should be True and is:", isGameWon(gameWonBoardHorizontal))
##    print("Game won should be True and is:", isGameWon(gameWonBoardDiagonal))
##    print("Game won should be False and is:", isGameWon(gameNotWonBoard))
##    print()
##
##    # Test isGameOver(board, numPlays) -> boolean
##    gameWonBoard = ['o', 'o', 'o', 4, 5, 6, 7, 8, 9]
##    gameOverBoard = ['x', 'o', 'x', 'x', 'o', 'x', 'o', 'x', 'o']
##    gameNotOverBoard = ['o', 2, 3, 4, 5, 6, 7, 8, 'x']
##    gameIsOverWin = isGameOver(gameWonBoard, 3)
##    gameIsOverPlays = isGameOver(gameOverBoard, 9)
##    gameNotOver = isGameOver(gameNotOverBoard, 2)
##    print("Game is over should be True and is:", gameIsOverWin)
##    print("Game is over should be True and is:", gameIsOverPlays)
##    print("Game is over should be False and is:", gameNotOver)
##    print()


