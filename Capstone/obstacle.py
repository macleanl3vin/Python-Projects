"""
The Obstacle class represents an obstacle to avoid in the game.
Constructor:
    Obstacle(x_coord: int, y_coord: int)
        - Constructs an obstacle based on the window's dimensions.
        - x_coord, y_coord - The max x and y coordinates of the window.
                             These are used for determining the dimensions
                             and speed of the obstacle.
Instance Variables:
    shape: Rectangle - The shape of the obstacle
                     - The shape should be a rectangle. In the obstacle constructor,
                       create the rectangle by first generating a random starting position,
                       then generate a random width, height, and color.
                     - Starting position: The x value of the obstacles starting position can
                       be the x_coord value and the y value can be a random number between
                       0 and the y_coord.
                     - Dimensions: Add a random width and height to the starting point to get
                       the other corner of the rectangle. The width and height should be anywhere
                       between 5 and 10 % of the window's x and y coordinates respectively.
                       For example, if x_coord is 90, the width would be a random number between
                       4.5 (5% of 90) and 9 (10% of 90).
                     - Color: Have a list of possible color strings and randomly choose one. Then
                       set the rectangles fill color to that color.
    speed: float - The speed of the obstacle.
                 - This should be a random number generated based off the x_coord (because speed is
                   movement in the x direction)
                 - The recommended speeds are between 0.5 and 0.8 % of the x_coord
"""
"""
Methods:
    draw(win: GraphWin) -> None
        Takes a GraphWin object as a parameter and draws the obstacle to the win
    undraw() -> None
        Undraws the obstacle.
    move() -> None
        Moves the obstacle the amount of the speed instance variable. Note that this
        will likely be a negative value because the obstacle is moving from right to left
    is_done() -> bool
        Checks if the obstacle has reached the end (left side) of the screen. This can likely
        be accomplished by getting one of the right corners of the rectangle and
        checking if its x value is less than or equal to 0
        This method will be used during the game to remove obstacles that have already passed
    get_shape() -> Rectangle
        Returns the obstacle's shape instance variable.
        This is used in the Player's is_hit method to check for collisions
"""
from graphics import *
from random import *
class Obstacle:
    def __init__(self, x_coord: int, y_coord: int):
        self.x_coord = x_coord
        self.y_coord = y_coord
        # Shape Coordinates
        randomX = uniform((5 * x_coord)/100, (10 * x_coord)/100)
        randomY = uniform((5 * y_coord)/100, (10 * y_coord)/100)

        self.startX = x_coord
        self.startY = randint(0, (y_coord-20))

        self.oppoX = randomX + self.startX
        self.oppoY = randomY + self.startY
        self.shape = Rectangle(Point(self.startX, self.startY), Point(self.oppoX, self.oppoY))

        # Color Selection
        colors = ['Blue', 'Green', 'Red', 'Orange', 'Purple', 'Yellow']
        self.shape.setFill(colors[randint(0, 5)])

        # Speed creation
        # Changed given speed to make difficulty feel harder
        self.speed = uniform(((0.4 / 100) * x_coord), (0.7 / 100) * x_coord)

    def draw(self, win: GraphWin):
        self.shape.draw(win)

    def undraw(self):
        self.shape.undraw()

    def move(self):
        self.shape.move(-self.speed, 0)

    def is_done(self):
        point1X = self.shape.getP2().getX()
        if point1X <= 0:
            return True
        else:
            return False

    def get_shape(self):
        return self.shape


