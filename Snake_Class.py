from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]





    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.create_segments(position)

    def create_segments(self, position):
        #We are naming the segment sally for convenience
        sally = Turtle()
        sally.shape("square")
        sally.color("GreenYellow")
        sally.penup()
        sally.goto(position)
        self.segments.append(sally)


    def extend_snake(self):
        self.create_segments(self.segments[-1].position())


    def move(self) :

        for segment in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[segment - 1].xcor()
            y_position = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_position, y_position)
        self.segments[0].forward(STEP)

    def up(self):
        if self.segments[0].heading() != 270 :
            self.head.setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.head.setheading(0)


