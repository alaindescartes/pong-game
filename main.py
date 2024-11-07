from ball import Ball
from screen import GameScreen
from paddle import Paddle
from separator import Separator
from scoreboard import Scoreboard

#init
screen = GameScreen()
paddle1 = Paddle((screen.screen.window_width() / 2 - 25, 0))  # left side
paddle2 = Paddle((-(screen.screen.window_width() / 2 - 15), 0))  # right side
separator = Separator()
scoreboard = Scoreboard()
ball = Ball() #draw the ball on the screen

#set up paddle controls
paddle2.bind_keys( controls={'Up': 'w', 'Down': 's'})
paddle1.bind_keys( controls={'Up': 'Up', 'Down': 'Down'})

#draw the ball
ball.draw_ball()
scoreboard.display_scores(screen=screen)

while True:
    ball.move_ball()
    if paddle1.detect_collision_with_ball(ball=ball) or paddle2.detect_collision_with_ball(ball=ball):
        ball.bounce_ball()

    # Check for score update
    if scoreboard.detect_score(ball=ball, screen=screen):
        scoreboard.display_scores(screen=screen)

    screen.screen.update()
