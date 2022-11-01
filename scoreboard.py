from turtle import Turtle
import random

SCORE = 0

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.points = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 250)
        self.game_over()
        self.update_score()



    def update_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score:{self.points}", False, "center", ("Arial", 15, "normal"))
        self.points += 1


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", False, "center", ("Arial", 25, "normal"))
