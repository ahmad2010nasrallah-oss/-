import turtle
import time
import random

# إعداد النافذة
window = turtle.Screen()
window.title("AIR BALL DUO")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# متغيرات اللعبة
game_over = False
game_started = False

# السكور
score_a = 0
score_b = 0

# عدد الأهداف المطلوبة للفوز
winning_score = 5

# -----------------------------------
# واجهة البداية
# -----------------------------------

start_pen = turtle.Turtle()
start_pen.speed(0)
start_pen.color("white")
start_pen.penup()
start_pen.hideturtle()

start_pen.goto(0, 120)
start_pen.write(
    "AIR BALL DUO",
    align="center",
    font=("Courier", 36, "bold")
)

start_pen.goto(0, 40)
start_pen.write(
    "Press SPACE To Start",
    align="center",
    font=("Courier", 20, "normal")
)

start_pen.goto(0, -40)
start_pen.write(
    "اهلا و سهلا بك في اول لعبة لي",
    align="center",
    font=("Courier", 16, "normal")
)

def start_game():
    global game_started
    game_started = True
    start_pen.clear()

# -----------------------------------
# خط المنتصف
# -----------------------------------

middle_line = turtle.Turtle()
middle_line.speed(0)
middle_line.color("white")
middle_line.penup()
middle_line.goto(0, 300)
middle_line.setheading(270)
middle_line.pensize(3)

for i in range(30):
    middle_line.pendown()
    middle_line.forward(10)
    middle_line.penup()
    middle_line.forward(10)

# -----------------------------------
# المضرب الأيسر (لاعب)
# -----------------------------------

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# -----------------------------------
# المضرب الأيمن (AI)
# -----------------------------------

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# -----------------------------------
# الكرة
# -----------------------------------

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 3
ball.dy = 3

# -----------------------------------
# السكور
# -----------------------------------

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

pen.write(
    "Player: 0  AI: 0",
    align="center",
    font=("Courier", 18, "normal")
)

# -----------------------------------
# إعلان الفائز
# -----------------------------------

winner_pen = turtle.Turtle()
winner_pen.speed(0)
winner_pen.color("yellow")
winner_pen.penup()
winner_pen.hideturtle()

# -----------------------------------
# حركة اللاعب
# -----------------------------------

a_up = False
a_down = False

def press_w():
    global a_up
    a_up = True

def press_s():
    global a_down
    a_down = True

def release_w():
    global a_up
    a_up = False

def release_s():
    global a_down
    a_down = False

# -----------------------------------
# إعادة تشغيل
# -----------------------------------

def restart_game():
    global score_a, score_b, game_over

    score_a = 0
    score_b = 0
    game_over = False

    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)

    ball.goto(0, 0)
    ball.dx = 3
    ball.dy = 3

    winner_pen.clear()

    pen.clear()
    pen.goto(0, 260)
    pen.write(
        "Player: 0  AI: 0",
        align="center",
        font=("Courier", 18, "normal")
    )

# -----------------------------------
# الأزرار
# -----------------------------------

window.listen()

window.onkeypress(start_game, "space")

window.onkeypress(press_w, "Up")
window.onkeypress(press_s, "Down")

window.onkeyrelease(release_w, "Up")
window.onkeyrelease(release_s, "Down")
window.onkeypress(restart_game, "r")

# -----------------------------------
# لوب اللعبة
# -----------------------------------

while True:

    window.update()

    if not game_started:
        continue

    if game_over:
        continue

    # -----------------------------------
    # حركة اللاعب
    # -----------------------------------

    if a_up:
        paddle_a.sety(paddle_a.ycor() + 5)

    if a_down:
        paddle_a.sety(paddle_a.ycor() - 5)

    # -----------------------------------
    # AI (واقعي + أخطاء)
    # -----------------------------------

    if ball.xcor() > 0:

        target = ball.ycor() + random.randint(-60, 60)

        speed = 3

        if paddle_b.ycor() < target:
            paddle_b.sety(paddle_b.ycor() + speed)

        if paddle_b.ycor() > target:
            paddle_b.sety(paddle_b.ycor() - speed)

    # -----------------------------------
    # حركة الكرة
    # -----------------------------------

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # -----------------------------------
    # النقاط
    # -----------------------------------

    if ball.xcor() > 390:

        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1

        pen.clear()
        pen.write(
            f"Player: {score_a}  AI: {score_b}",
            align="center",
            font=("Courier", 18, "normal")
        )

        # فوز اللاعب
        if score_a >= winning_score:

            game_over = True

            winner_pen.clear()

            winner_pen.goto(0, 120)
            winner_pen.write(
                "👑 PLAYER WINS 👑",
                align="center",
                font=("Courier", 28, "bold")
            )

    if ball.xcor() < -390:

        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1

        pen.clear()
        pen.write(
            f"Player: {score_a}  AI: {score_b}",
            align="center",
            font=("Courier", 18, "normal")
        )

        # فوز الذكاء الاصطناعي
        if score_b >= winning_score:

            game_over = True

            winner_pen.clear()

            winner_pen.goto(0, 120)
            winner_pen.write(
                "game over",
                align="center",
                font=("Courier", 28, "bold")
            )

    # -----------------------------------
    # التصادم
    # -----------------------------------

    if (
        340 < ball.xcor() < 350 and
        paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50
    ):
        ball.setx(340)
        ball.dx *= -1

    if (
        -350 < ball.xcor() < -340 and
        paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50
    ):
        ball.setx(-340)
        ball.dx *= -1

    time.sleep(0.01)