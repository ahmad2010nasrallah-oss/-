import turtle
import time

# إعداد النافذة
window = turtle.Screen()
window.title("Air Ball Duo")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# المضرب الأيسر
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("Blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# المضرب الأيمن
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("Red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# الكرة
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# سرعة الكرة
ball.dx = 2
ball.dy = 2

# السكور
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 18, "normal"))

# تحريك المضارب
def paddle_a_up():
    y = paddle_a.ycor()
    paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    paddle_b.sety(y - 20)

# ربط الأزرار
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# لوب اللعبة
while True:
    window.update()

    # حركة الكرة
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # حدود الشاشة (فوق وتحت)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # يمين ويسار (تسجيل نقاط)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 18, "normal"))

    # تصادم الكرة مع المضارب
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    time.sleep(0.01)