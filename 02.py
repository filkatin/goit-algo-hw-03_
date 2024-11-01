import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

def main():
    try:
        order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    size = 300
    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Малюємо три сторони сніжинки Коха
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    draw_koch_snowflake(3, size)

    window.mainloop()


if __name__ == "__main__":
    main()
