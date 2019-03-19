import turtle


def draw_diamond(turt):
    for i in range(1, 3):
        turt.forward(100)  # 向前走100步
        turt.right(45)  # 然后海龟头向右转45度
        turt.forward(100)  # 继续向前走100步
        turt.right(135)  # 然后有向右转135度


def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed('fast')

    for i in range(1, 37):
        draw_diamond(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(300)

    window.exitonclick()

draw_art()