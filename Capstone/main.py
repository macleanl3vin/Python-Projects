"""
This is where your game begins. There are many ways to arrange this module.
High level (very general) pseudocode and things to consider:
- Set up the window
- Initialize the player
- Initialize an empty obstacle list for storing all of the obstacles
  that are currently on the screen
- Initialize the score to 0
- Start the game loop
    - get the key press
    - create obstacles
        - you do not want to create an obstacle every time through the loop
          (creating an obstacle roughly every 1/100 loops seems to work well)
        - how can you create obstacles on random occasions through the loop?
        - when an obstacle is created, draw it to the screen and add it to the
          obstacles list
    - move the player
    
    - move obstacles, check for hits with the player, and check if the obstacle is done (off the screen)
        - if an obstacle is done, undraw it and remove it from the obstacles list
    - set the score text
    - sleep (try 0.01 seconds to start)
"""
"""
    - handle if there was a hit
        - the general flow for if there was a hit
            1. - If the score is the highest score, print the
                 high score text for three seconds, then remove it
                    - To keep track of high scores, any top five high score
                      needs to be saved to a text file called highscores.txt
                      
            2. - Display the screen that asks the user if they still want to play
               - The width and height of the screen should be 60 % of the window's
                 width and height
               - You can consider putting this functionality in a function where calling the function
                 displays the screen, waits for the click, clears the screen, and returns the result (yes/no)
               - Wait for the user to click either the yes or no button
            3. - If the user clicks yes, reset the hero, score, and undraw/remove all obstacles
               - You can consider putting this reset functionality in a function
            4. - If the user clicks no, display the top 5 high scores of all time
               - Exit the game after an additional user click
"""

from graphics import *
from random import *
from player import *
from obstacle import *
from button import *
# Set Up Part 1
maxX = 1000
maxY = 500
win = GraphWin('Dodger', maxX, maxY)
win.setBackground('Black')
player = Player(maxX, maxY)

player.draw(win)
obstacles = []

score = 0
scoreText = Text(Point(75, 475), f'Score: {score}')
scoreText.draw(win)
scoreText.setSize(25)
scoreText.setFill('Green')

winMsg = Text(Point(500, 250), 'High Score!')
winMsg.setFill('Gold')
winMsg.setSize(35)
# Set up Part 2: Game Loop
running = True
count = -1
while running:
    update(100)
    key = win.checkKey()
    count += 1
    sleep(0.01)
    if (count % 70) == 0:
        obstacle = Obstacle(maxX, maxY)
        obstacle.draw(win)
        obstacles.append(obstacle)

    player.move(key)

    for obstacle in obstacles:
        obstacle.move()
        player.is_hit(obstacle)
        if obstacle.is_done():
            print(obstacle.get_shape().getP1())
            print(score)
            obstacle.undraw()
            obstacles.remove(obstacle)
            score += 1
            scoreText.setText(f'Score: {score}')


        # If player is hit by obstacle
        if player.is_hit(obstacle):
            fileR = open('highscores.txt', 'r')
            highScores = fileR.read().split()
            for high in range(len(highScores)):
                highScores[high] = int(highScores[high])


            # if the users score is greater than the highest score on board or empty
            if not highScores or score > max(highScores):
                highScores.append(score)
                highScores.sort(reverse=True)
                # keep the top 5 scores
                highScores = highScores[:5]

                # open the file for writing, while also clearing the file | then writing the new values into file, and closing
                fileW = open('highscores.txt', 'w')
                for high in range(len(highScores)):
                    highScores[high] = str(highScores[high])
                fileW.write(' '.join(highScores))
                fileW.close()

                # telling user he has a high score
                winMsg.draw(win)
                sleep(3)
                winMsg.undraw()

            # if the users score is greater than the other high scores
            else:
                highScores.append(score)
                highScores.sort(reverse=True)
                highScores = highScores[:5]

                fileW = open('highscores.txt', 'w')
                for high in range(len(highScores)):
                    highScores[high] = str(highScores[high])
                fileW.write(' '.join(highScores))
                fileW.close()



            # Display screen to ask user if they still want to play
            displayMsg = Text(Point(500, 150), 'Do you want to play again?')
            displayMsg.setSize(30)

            # Set window width and height to 60 % of the max x,y for screen
            window = Rectangle(Point(200, 100), Point(800, 400))
            window.setFill('Dark Grey')
            window.setOutline('Black')
            window.setWidth(2)
            yesButton = Button(Point(275, 200), Point(455, 300), 'YES')
            noButton = Button(Point(550, 200), Point(730, 300), 'NO')
            window.draw(win)
            displayMsg.draw(win)
            noButton.draw(win)
            yesButton.draw(win)
            click = win.getMouse()

            # If user clicks no button,
            if noButton.is_clicked(click):
                for obj in obstacles:
                    obj.undraw()
                window.undraw()
                displayMsg.undraw()
                noButton.undraw()
                yesButton.undraw()
                sleep(0.01)
                # Display top 5 High Scores
                # Window
                top5window = Rectangle(Point(130, 0), Point(850, 500))
                top5window.setFill('Dark Grey')
                top5window.setOutline('Black')
                top5window.setWidth(2)
                # High Scores msg
                xVal = 500
                yVal = 50
                highScoreMsg = Text(Point(500, 50), 'HIGH SCORES')
                highScoreMsg.setSize(30)
                # Draw window, high score msg, and high scores
                top5window.draw(win)
                highScoreMsg.draw(win)
                # High scores
                fileHS = open('highscores.txt', 'r')
                currentHScores = fileHS.read().split()
                i = 50
                for hs in currentHScores:
                    hsText = Text(Point(xVal, (yVal + i)), hs)
                    hsText.setSize(25)
                    hsText.draw(win)
                    i += 75
                # Exit game after user clicks anywhere
                win.getMouse()
                exit()

            elif yesButton.is_clicked(click):
                player.reset()
                score = 0
                for obj in obstacles:
                    obj.undraw()

                # reset obstacles list so score doesn't get increased from previous placement of obstacles
                obstacles = []
                window.undraw()
                displayMsg.undraw()
                noButton.undraw()
                yesButton.undraw()
                scoreText.setText(f'Score: {score}')





