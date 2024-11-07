from turtle import Turtle, Screen
from ball import Ball


class Paddle:
    def __init__(self, position=(0, 0), color="white", speed=40, length=3):
        self.color = color
        self.screen = Screen()
        self.length = length
        self.paddle = Turtle()
        self.position = position
        self.speed = speed
        self.ball = Ball()
        self.has_collided = False
        self.draw_paddle()

    def draw_paddle(self):
        """
        Draws the paddle at a specified position
        """
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.goto(self.position)
        self.paddle.color(self.color)
        self.paddle.shapesize(stretch_wid=self.length, stretch_len=1)

    def move_up(self):
        """
        Move the paddle up
        """
        max_height = self.screen.window_height()/2 - 30
        new_y = self.paddle.ycor() + self.speed
        if new_y > max_height:
            new_y = max_height
        self.paddle.sety(new_y)

    def move_down(self):
        """
        Move the paddle down
        :return:
        """
        max_height = -(self.screen.window_height()/2 - 50)
        new_y = self.paddle.ycor() - self.speed
        if new_y < max_height:
            new_y = max_height
        self.paddle.sety(new_y)

    def bind_keys(self, controls):
        """
        Bind keys to move paddle up and down for multiplayer controls.
        :param controls: Dictionary with 'up' and 'down' keys for this paddle
        """
        self.screen.listen()
        self.screen.onkeypress(self.move_up, controls["Up"])
        self.screen.onkeypress(self.move_down, controls["Down"])

    def detect_collision_with_ball(self, ball):
        """
        Detects collision with the given ball across the paddle's full height.
        """
        collision_distance = 20
        paddle_top = self.paddle.ycor() + (self.paddle.shapesize()[0] * 10 / 2)  # Top edge of paddle
        paddle_bottom = self.paddle.ycor() - (self.paddle.shapesize()[0] * 10 / 2)  # Bottom edge of paddle
        ball_y = ball.ball.ycor()
        ball_x = ball.ball.xcor()

        # Check horizontal and vertical alignment
        if self.paddle.distance(ball.ball) < collision_distance and paddle_bottom <= ball_y <= paddle_top:
            if not self.has_collided:
                self.has_collided = True
                return True  # Collision detected
        else:
            # Reset collision detection if ball moves away
            if self.paddle.distance(ball.ball) > collision_distance + 5:
                self.has_collided = False
        return False  # No collision detected



