import turtle
import os

wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


def create_paddle(pos):
    paddle = turtle.Turtle()
    paddle.speed(0)  # speed of animation
    paddle.shape('square')
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.color('white')
    paddle.penup()
    paddle.goto(pos, 0)
    return paddle


# Paddle A
paddle_a = create_paddle(-350)
# Paddle B
paddle_b = create_paddle(350)
# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)

ball.dx = 2  # so when it will move it will move up and to the side
ball.dy = 2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {0} Player B: {1}".format(score_a, score_b),
          align='center',  font=('Courier', 24,'normal'))


def move_paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def move_paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def move_paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def move_paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(move_paddle_a_up, 'w')
wn.onkeypress(move_paddle_a_down, 's')
wn.onkeypress(move_paddle_b_up, 'k')
wn.onkeypress(move_paddle_b_down, 'j')
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {0} Player B: {1}".format(score_a, score_b),
                  align='center',  font=('Courier', 24,'normal'))
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {0} Player B: {1}".format(score_a, score_b),
                  align='center',  font=('Courier', 24,'normal'))
    elif ball.ycor() > 290:
        ball.dy *= -1
        os.system('afplay bounce.wav&') # & to remove delay
    elif ball.ycor() < -290:
        ball.dy *= -1
        os.system('afplay bounce.wav&')


    # paddle and ball colidion
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
            (ball.ycor() < paddle_b.ycor() + 40
             and ball.ycor() > paddle_b.ycor() - 40):
        ball.dx *= -1
        os.system('afplay bounce.wav&')
    elif (ball.xcor() < -340 and ball.xcor() > -350) and \
            (ball.ycor() < paddle_a.ycor() + 40
             and ball.ycor() > paddle_a.ycor() - 40):
        ball.dx *= -1
        os.system('afplay bounce.wav&')

