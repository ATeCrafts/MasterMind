import turtle
import random

COLOURS = ["red", "green", "blue", "yellow", "orange", "pink", "grey", "white"]
RADIUS = 20
FEEDBACK_SIZE = 10
SPACING = 60
NUMTURNS = 12

code = [random.choice(COLOURS) for i in range(4)]

window = turtle.Screen()
window.title("MasterMind")
window.bgcolor("lightgrey")

guessTurtle = turtle.Turtle()
guessTurtle.speed(0)
guessTurtle.hideturtle()

feedbackTurtle = turtle.Turtle()
feedbackTurtle.speed(0)
feedbackTurtle.hideturtle()

def drawGuess(x, y, colour):
    guessTurtle.penup()
    guessTurtle.goto(x, y - RADIUS)
    guessTurtle.pendown()
    guessTurtle.color(colour)
    guessTurtle.begin_fill()
    guessTurtle.circle(RADIUS)
    guessTurtle.end_fill()

def drawFeedback(x, y, numBlack, numWhite):
    feedbackTurtle.penup()
    feedbackTurtle.goto(x, y)
    for i in range(numBlack):
        feedbackTurtle.dot(FEEDBACK_SIZE, "black")
        feedbackTurtle.forward(SPACING / 2)
    for i in range(numWhite):
        feedbackTurtle.dot(FEEDBACK_SIZE, "white")
        feedbackTurtle.forward(SPACING / 2)

def checkGuess(guess):
    numBlack = 0
    numWhite = 0
    tempCode = code.copy()
    tempGuess = guess.copy()

    for i in range(4):
        if guess[i] == code[i]:
            numBlack += 1
            tempCode[i] = None
            tempGuess[i] = None
    
    for i in range(4):
        if tempGuess[i] in tempCode:
            numWhite += 1
            tempCode[tempCode.index(tempGuess[i])] = None
    
    return numBlack, numWhite

def makeTurn(turnNumber):
    guess = []
    for i in range(4):
        colour = input(f"Turn {turnNumber + 1}" + f" Enter color for position {i + 1} (choices: {COLOURS}): ").strip().lower()
        while colour not in COLOURS:
            colour = input(f"Turn {turnNumber + 1}" + f" Enter color for position {i + 1} (choices: {COLOURS}): ").strip().lower()
        guess.append(colour)

    for i in range(4):
        drawGuess(-150 + i * SPACING, 200 - turnNumber * SPACING, guess[i])

    black, white = checkGuess(guess)
    drawFeedback(150, 200 - turnNumber * SPACING + RADIUS, black, white)

    print("Feedback", f"Feedback for this guess:\n" f"- {black} black peg(s): Correct color in the correct position.\n" f"- {white} white peg(s): Correct color in the wrong position.")

    if black == 4:
        return True
    return False

for turn in range(NUMTURNS):
    if makeTurn(turn):
        print("Game Over", "Congratulations! You guessed the code correctly!")
        break
else:
    print("Game Over", f"Sorry! You couldn't guess the code. The correct code was: {code}")

window.mainloop()