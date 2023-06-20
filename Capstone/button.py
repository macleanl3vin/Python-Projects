"""
The Button class represents a clickable button.
Constructor:
    Button(p1: Point, p2: Point, text: string)
        Constructs a button from two points (p1 and p2) and a string of text

Instance Variables:
    shape: Rectangle - The outline of the button
    text: Text - the text of the button
Methods:
    draw(win: GraphWin) -> None
        Takes a GraphWin object as a parameter and draws the button (all of the button's components) to the win

    undraw() -> None
        Undraws the button (each of the button's components).
    is_clicked(click: Point) -> bool
        Takes a Point object as a parameter and returns True if the point's coordinates are inside the
        button's shape, otherwise returns False
"""
from graphics import *
class Button:
    def __init__(self, p1: Point, p2: Point, text: str):
        self.shape = Rectangle(p1, p2)
        self.text = Text(self.shape.getCenter(), text)
        self.text.setSize(25)

    def draw(self, win: GraphWin):
        self.shape.draw(win)
        self.text.draw(win)

    # def checkColor(self):
    #     if self.text == 'YES':
    #         self.shape.setFill('Green')
    #
    #     elif self.text == 'NO':
    #         self.shape.setFill('Red')

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

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
