from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.score = {"player1": 0, "player2": 0}

        # Separate turtles for each player's score display
        self.player1_display = Turtle()
        self.player2_display = Turtle()

        # Set up player score displays
        for display in (self.player1_display, self.player2_display):
            display.color("white")
            display.hideturtle()
            display.penup()

    def update_score(self, name):
        """
        Updates the scoreboard with new score
        :param name: the name of the player
        """
        self.score[name] += 1

    def get_score(self):
        """
        Returns the scoreboard
        :return: the score of the players
        """
        return self.score

    def reset_score(self):
        """
        Resets the scoreboard
        """
        self.score = {"player1": 0, "player2": 0}

    def detect_score(self, ball, screen):
        screen_width = screen.screen.window_width() / 2
        ball_x = ball.ball.xcor()
        score_updated = False

        # Check if the ball has passed the left boundary (Player 2 scores)
        if ball_x < -screen_width:
            self.score["player2"] += 1
            print("Player 2 scores!")
            ball.reset_position()
            score_updated = True

        # Check if the ball has passed the right boundary (Player 1 scores)
        elif ball_x > screen_width:
            self.score["player1"] += 1
            print("Player 1 scores!")
            ball.reset_position()
            score_updated = True
        return score_updated

    def display_scores(self, screen):
        """
        Displays the current scores for both players.
        """
        # Clear previous scores
        self.player1_display.clear()
        self.player2_display.clear()

        # Display updated scores for Player 1
        self.player1_display.goto(-150, (screen.screen.window_height() / 2) - 30)
        self.player1_display.write(f"Player 1: {self.score['player1']}", align="center", font=("Arial", 14, "normal"))

        # Display updated scores for Player 2
        self.player2_display.goto(150, (screen.screen.window_height() / 2) - 30)
        self.player2_display.write(f"Player 2: {self.score['player2']}", align="center", font=("Arial", 14, "normal"))
