import turtle
from turtle import Turtle
import random

class Ball():
    def __init__(self):
        self.ball = Turtle()
        self.color ="yellow"
        self.position = (0,0)
        self.x_velocity = random.choice([-4, 5])
        self.y_velocity = random.choice([-4, 2])
        self.screen = turtle.Screen()

    def draw_ball(self):
        """
        draws ball on the screen
        """
        self.ball.hideturtle()
        self.ball.penup()
        self.ball.goto(self.position)
        self.ball.shape("circle")
        self.ball.color(self.color)
        self.ball.showturtle()

    def move_ball(self):
        """
        moves ball on the screen
        :return:
        """
        # Randomly adjust velocities slightly to introduce unpredictability
        # self.x_velocity += random.uniform(-0.15, 0.15)
        # self.y_velocity += random.uniform(-0.15, 0.15)

        x_position = self.ball.xcor()
        y_position = self.ball.ycor()

        # Calculate new x and y positions based on velocities
        new_x = x_position + self.x_velocity
        new_y = y_position + self.y_velocity
        self.position = (new_x, new_y)

        # Move the ball to the new position
        self.ball.goto(new_x, new_y)
        self.detect_collision_with_roof_and_floor()

    def detect_collision_with_roof_and_floor(self):
        """
        detects collision with roof and floor of the screen
        """
        window_height = self.screen.window_height() / 2
        ball_y_position = self.ball.ycor()

        # Check if the ball has hit the top boundary and is moving upward
        if ball_y_position > window_height and self.y_velocity > 0:
            # Invert y_velocity to bounce the ball downwards
            self.y_velocity *= -1

        # Check if the ball has hit the bottom boundary and is moving downward
        if ball_y_position < -window_height and self.y_velocity < 0:
            # Invert y_velocity to bounce the ball upwards
            self.y_velocity *= -1

    def bounce_ball(self):
        """
        bounces ball on the screen
        :return:
        """
        self.x_velocity *= -1

    def reset_position(self):
        """
        resets the position of the ball on the screen
        :return:
        """
        self.position = (0,0)
        self.draw_ball()
        self.x_velocity = random.choice([-2, 2])
        self.y_velocity = random.choice([-1, 1])