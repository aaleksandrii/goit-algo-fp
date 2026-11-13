import turtle


def draw_branch(t: turtle.Turtle, length: float, level: int) -> None:
    if level <= 0:
        return

    t.forward(length)

    child_length = length / (2 ** 0.5)
    t.left(35)
    draw_branch(t, child_length, level - 1)
    t.right(70)
    draw_branch(t, child_length, level - 1)
    t.left(35)

    t.backward(length)


def draw_pythagoras_tree(level: int, size: float = 150) -> None:
    screen = turtle.Screen()
    screen.setup(width=900, height=900)
    screen.title(f"Дерево Піфагора — рівень {level}")
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -330)
    t.setheading(90)
    t.pendown()
    t.color("firebrick")

    draw_branch(t, size, level)

    t.hideturtle()
    screen.update()
    screen.mainloop()


def main() -> None:
    while True:
        try:
            level = int(input("Enter the recursion level (0–12, 8 is a better option): "))
        except ValueError:
            print("Invalid input. Let's try again")
            continue

        if 0 <= level <= 12:
            break
        print("Recursion level should be 0 to 12. Level 0 is empty picture.")

    draw_pythagoras_tree(level)


if __name__ == "__main__":
    main()
