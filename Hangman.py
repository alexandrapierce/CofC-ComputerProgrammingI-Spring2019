#Name: Alex Pierce CSCI220-03
#hangman.py
#Purpose:Play hangman
#Inputs:letter guesses from user 
#Outputs: game of hangman
#Certification: I certify that this lab is entirely my own work with help from CS lab

import random
from graphics import *

def listWords():
    infile=open("wordlist.txt","r")
    words=[]
    for word in infile:
        word = word.replace("\n","").replace("\ufeff","")
        words.append(word)
    return words

def randomWord(wordList):
    word=random.choice(wordList)
    return word

def updateGuessedWord(guessWord,secretWord,letter):
    for i in range(len(secretWord)):
        if letter == secretWord[i]:
            guessWord[i] = letter
    return guessWord

def buildString(guessWord):
    strWord= "".join(guessWord)
    return strWord

def isSecretWord(guessWord,secretWord):
    for i in range(len(guessWord)):
        if guessWord[i]=="_":
            return False
    return True
        
def isValidGuess(letter,secretWord):
    for i in range(len(secretWord)):
        if letter == secretWord[i]:
           return True   
    return False


def playGame():
    #drawing all objects
    winWidth = 400
    winHeight = 400
    win = GraphWin("Hangman", winWidth, winHeight)
    win.setBackground("Pink")
    #instructions at bottom of screen
    instPt = Point(winWidth/2, winHeight-10)
    instructions = Text(instPt,"Welcome to Hangman! Good Luck!")
    instructions.setSize(20)
    instructions.setFace("times roman")
    instructions.setTextColor("Black")
    instructions.draw(win)
    #guess count
    guessCountPt = Point(50,25)
    guessCount = Text(guessCountPt, "Guesses: "+ str(7))
    guessCount.setSize(16)
    guessCount.setFace("times roman")
    guessCount.setTextColor("Blue")
    guessCount.draw(win)
    #wrong letter count
    wrongLetterPt = Point(65,65)
    wrongLetter = Text(wrongLetterPt, "Wrong letters:")
    wrongLetter.setSize(16)
    wrongLetter.setFace("times roman")
    wrongLetter.setTextColor("Blue")
    wrongLetter.draw(win)
    #entry box
    inputBox = Text(Point(68,312),"Guess a letter:")
    inputBox.setSize(16)
    inputBox.setFace("times roman")
    inputBox.setTextColor("Red")
    inputBox.draw(win)
    entryBox = Entry(Point(130,311),2)
    entryBox.draw(win)
    #submit button
    submitButton = Rectangle(Point(152,301), Point(216,322))
    submitButton.setFill("Red")
    submitButton.draw(win)
    submit = Text(Point(182,313),"Submit")
    submit.setTextColor("White")
    submit.setSize(15)
    submit.draw(win)
    #Hangman stand
    line1=Line(Point(243,75), Point(243,19))
    line1.setWidth(10)
    line1.setFill("Black")
    line1.draw(win)
    line2=Line(Point(238,22), Point(349,22))
    line2.setWidth(10)
    line2.setFill("Black")
    line2.draw(win)
    line3=Line(Point(345,19), Point(345,312))
    line3.setWidth(10)
    line3.setFill("Black")
    line3.draw(win)
    line4=Line(Point(269,312), Point(405,312))
    line4.setWidth(10)
    line4.setFill("Black")
    line4.draw(win)
    #MAN
    head = Circle(Point(241,104),30)
    head.setWidth(3)
    #head.draw(win)
    body = Line(Point(242,134), Point(241,227))
    body.setWidth(3)
    #body.draw(win)
    rArm = Line(Point(241,172), Point(286,150))
    rArm.setWidth(3)
    #rArm.draw(win)
    lArm = Line(Point(242,172), Point(201,151))
    lArm.setWidth(3)
    #lArm.draw(win)
    rLeg = Line(Point(241,227), Point(286,257))
    rLeg.setWidth(3)
    #rLeg.draw(win)
    lLeg = Line(Point(241,227), Point(196,257))
    lLeg.setWidth(3)
    #lLeg.draw(win)
    rEye = Circle(Point(229,97),5)
    rEye.setFill("Blue")
    #rEye.draw(win)
    lEye = Circle(Point(252,98),5)
    lEye.setFill("Blue")
    #lEye.draw(win)
    mouth = Oval(Point(234,109), Point(248,122))
    mouth.setFill("Red")
    #mouth.draw(win)

    
    #Playing
    playing= True
    wordList=listWords()
    secretWord= randomWord(wordList)
    guessWord = ("_ "*len(secretWord)).split()
    spaces= Text(Point(86,208),guessWord)
    spaces.draw(win)
    print(secretWord)
    wrongLetterList=""
    count= 7
    while playing:
        clickSubmit = win.getMouse()
        submitX = clickSubmit.getX()
        submitY = clickSubmit.getY()
        if 152 < submitX < 216 and 301 < submitY < 322:
            print('button clicked')
            guess = entryBox.getText()
            if isValidGuess(guess, secretWord) == True:
                guessWord = updateGuessedWord(guessWord,secretWord,guess)
                spaces.setText(guessWord)
            if isValidGuess(guess,secretWord) == False:
                if guess not in wrongLetterList:
                    count-=1
                    wrongLetterList = wrongLetterList + guess 
                    wrongLetter.setText("Wrong Letters: \n" + str(wrongLetterList))
                    guessCount.setText("Guesses: "+ str(count))
                    if count == 6:
                        head.draw(win)
                    if count == 5:
                        body.draw(win)
                    if count == 4:
                        rArm.draw(win)
                    if count == 3:
                        lArm.draw(win)
                    if count == 2:
                        rLeg.draw(win)
                    if count == 1:
                        lLeg.draw(win)
                    if count == 0:
                        rEye.draw(win)
                        lEye.draw(win)
                        mouth.draw(win)
                        spaces.undraw()
                        youLose = Text(Point(115,208),"YOU LOSE!")
                        youLose.setSize(36)
                        youLose.setTextColor("White")
                        youLose.draw(win)
                        playing = False
                        playAgain = Text(Point(111,251),"Would you like to play again?")
                        playAgain.setTextColor("White")
                        playAgain.draw(win)
                        yesButton = Rectangle(Point(58,267), Point(85,287))
                        yesButton.setFill("Green")
                        yesButton.draw(win)
                        yesText = Text(Point(72,277),"YES")
                        yesText.setTextColor("White")
                        yesText.draw(win)
                        noButton = Rectangle(Point(118,267), Point(145,287))
                        noButton.setFill("Red")
                        noButton.draw(win)
                        noText = Text(Point(131,278),"NO")
                        noText.setTextColor("White")
                        noText.draw(win)
                        clickYesOrNo = win.getMouse()
                        clickYesOrNoX = clickYesOrNo.getX()
                        clickYesOrNoY = clickYesOrNo.getY()
                        if 58 < clickYesOrNoX < 85 and 267 < clickYesOrNoY < 287:
                            win.close()
                            playGame()
                        if 118 < clickYesOrNoX < 145 and 267 < clickYesOrNoY < 287:
                            instructions.setText("Click to close")
                            win.getMouse()
                            win.close()
            if isSecretWord(guessWord,secretWord):
                spaces.undraw()
                youWin = Text(Point(115,208),"YOU WIN!")
                youWin.setSize(36)
                youWin.setTextColor("White")
                youWin.draw(win)
                playing = False
                playAgain = Text(Point(111,251),"Would you like to play again?")
                playAgain.setTextColor("White")
                playAgain.draw(win)
                yesButton = Rectangle(Point(58,267), Point(85,287))
                yesButton.setFill("Green")
                yesButton.draw(win)
                yesText = Text(Point(72,277),"YES")
                yesText.setTextColor("White")
                yesText.draw(win)
                noButton = Rectangle(Point(118,267), Point(145,287))
                noButton.setFill("Red")
                noButton.draw(win)
                noText = Text(Point(131,278),"NO")
                noText.setTextColor("White")
                noText.draw(win)
                clickYesOrNo = win.getMouse()
                clickYesOrNoX = clickYesOrNo.getX()
                clickYesOrNoY = clickYesOrNo.getY()
                if 58 < clickYesOrNoX < 85 and 267 < clickYesOrNoY < 287:
                    win.close()
                    playGame()
                if 118 < clickYesOrNoX < 145 and 267 < clickYesOrNoY < 287:
                    instructions.setText("Click to close")
                    win.getMouse()
                    win.close()
               
playGame()
