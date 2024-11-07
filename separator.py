from turtle import Turtle

class Separator:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.color("white")
        self.turtle.width(2)
        self.turtle.hideturtle()
        self.turtle.penup()
        self.draw_dashed_line()

    def draw_dashed_line(self):
        """
        Draws a dashed line in the center of the screen
        """
        self.turtle.goto(0, 300)
        self.turtle.setheading(270)

        # Draw dashed line
        for _ in range(15):
            self.turtle.pendown()
            self.turtle.forward(20)
            self.turtle.penup()
            self.turtle.forward(20)
