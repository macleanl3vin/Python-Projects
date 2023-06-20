"""
The Player class represents the main character in the game.

Constructor:
    Player(x_coord: int, y_coord: int)
        - Constructs the player based on the window's dimensions.
        - x_coord, y_coord - The max x and y coordinates of the window.
                             These are used for determining the dimensions
                             of the player.
Instance Variables:
    shape: Circle - The outline of the player.
                  - A radius of 4% of the y_coord value is recommended
                  - The circle's center can start at the center of the screen (half the x and y coords)
    shapes: List[Shape] (List of graphics objects)
                - This is a list of all the shapes used to make the player (this list must include
                  at least 2 items, the player outline and one additional shape)
                - When moving and drawing the player we will need this list
                  to move and draw every shape in the list

    x_coord, y_coord: int
                - store the x and y coords passed into the constructor
                - we will need these values to make sure the player stays on the screen
                  when moving and when resetting the player's position


"""
"""
Methods:
    draw(win: GraphWin) -> None
        Takes a GraphWin object as a parameter and draws the player (all of the players's components) to the win
        
    is_clicked(click: Point) -> bool
        Takes a Point object as a parameter and returns True if the point's coordinates are inside the
        button's shape, otherwise returns False
"""
"""
    move(direction: string) -> None
        Moves the player in the given direction
        direction will be the string "Right", "Left", "Up", or "Down"
        The player should not be able to move off the screen.
        The amount the player moves (the player's speed), should be a percentage of
        the x_coord (1.3% of x_coord is recommended)

    ************
    is_hit(obstacle: Obstacle) -> bool
        This method is given to you
        Takes an Obstacle object as a parameter and returns True if the Player and the obstacle are
        touching/overlapping, otherwise False.
        This can be used when checking if an obstacle hit the player
    ***********


    reset() -> None
        Moves the Player to the starting position in the middle of the screen
        Consider using the Player's move method along with x_coord and y_coord instance variable
        This method can be used if the Player gets hit and selects to play again
        
"""
from graphics import *
from time import *
class Player:
    def __init__(self, x_coord: int, y_coord: int):
        self.x_coord = x_coord
        self.y_coord = y_coord

        self.shape = Circle(Point((x_coord/2), (y_coord/2)), ((5/100) * y_coord))
        innerC = Circle(Point((x_coord/2), (y_coord/2)), ((2/100) * y_coord))

        self.shape.setFill('Red')
        innerC.setFill('Grey')

        self.shapes = [self.shape, innerC]


    def draw(self, win: GraphWin):
        for shape in self.shapes:
            shape.draw(win)

    #
    def is_clicked(self, point: Point):
        pointOneX = self.shape.getP1().getX()
        pointOneY = self.shape.getP1().getY()

        pointTwoX = self.shape.getP2().getX()
        pointTwoY = self.shape.getP2().getY()

        pointX = point.getX()
        pointY = point.getY()

        if (pointX >= pointOneX and pointX <= pointTwoX) and (pointY >= pointOneY and pointY <= pointTwoY):
            return True
        else:
            return False

    ##
    def move(self, direction: str):
        sRadius = self.shape.getRadius()
        for shape in self.shapes:
            # update(60)
            moveX = (1.9 / 100) * self.x_coord
            moveY = (1.8 / 100) * self.y_coord

            if direction == 'Left':
                shape.move(-moveX, 0)
                xCoord = shape.getCenter().getX()
                if (xCoord - sRadius) <= 0:
                    shape.move(moveX, 0)

            if direction == 'Right':
                shape.move(moveX, 0)
                xCoord = shape.getCenter().getX()
                if (xCoord + sRadius) >= self.x_coord:
                    shape.move(-moveX, 0)

            if direction == 'Up':
                shape.move(0, -moveY)
                yCoord = shape.getCenter().getY()
                if (yCoord - sRadius) <= 0:
                    shape.move(0, moveY)

            if direction == 'Down':
                shape.move(0, moveY)
                yCoord = shape.getCenter().getY()
                if (yCoord + sRadius) >= self.y_coord:
                    shape.move(0, -moveY)

    def is_hit(self, obstacle):
        player_shape = self.shape
        center = player_shape.getCenter()
        obs = obstacle.get_shape()
        center_distances_x = abs(center.getX() - obs.getCenter().getX())
        center_distances_y = abs(center.getY() - obs.getCenter().getY())
        obs_width = abs(obs.getP1().getX() - obs.getP2().getX())
        obs_height = abs(obs.getP1().getY() - obs.getP2().getY())

        if center_distances_x > (obs_width / 2 + player_shape.getRadius()):
            return False
        if center_distances_y > (obs_height / 2 + player_shape.getRadius()):
            return False
        if center_distances_x <= (obs_width / 2):
            return True
        if center_distances_y <= (obs_height / 2):
            return True

        corner_distance_sq = ((center_distances_x - obs_width / 2) ** 2) + (center_distances_y - obs_height / 2) ** 2

        return corner_distance_sq <= player_shape.getRadius() ** 2

    # calculate using the center x, y values of the shape before it got hit. Subtracting/Adding to the center of the screen
    def reset(self):
        for shape in self.shapes:
            xValue = shape.getCenter().getX()
            yValue = shape.getCenter().getY()
            shape.move((500 - xValue), (250 - yValue))


