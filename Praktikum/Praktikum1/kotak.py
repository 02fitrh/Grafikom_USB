import turtle

def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def draw_brain(rows, columns, size):
    start_x, start_y = turtle.position()

    for _ in range(rows):
        for _ in range(columns):
            draw_square(size)
            turtle.forward(size)  # Spasi antar kotak

        turtle.penup()
        turtle.goto(start_x, turtle.ycor() - size)  # Kembali ke awal baris
        turtle.pendown()

    turtle.penup()
    turtle.goto(start_x, start_y)  # Kembali ke posisi awal
    turtle.pendown()

def main():
    turtle.speed(2)  # Kecepatan turtle

    # Move to the center of the screen
    turtle.penup()
    turtle.goto(-150, 150)
    turtle.pendown()

    draw_brain(3, 4, 50)  # Menampilkan otak dengan 3 baris dan 4 kolom, setiap kotak berukuran 50
    turtle.exitonclick()

if __name__ == "__main__":
    main()
