from turtle import*

# №7364

speed(0)
screensize(2000, 2500)
k = 40

for i in range(10):
    goto(xcor() + 6 * k, ycor() + 15 * k)
    goto(xcor() + 4 * k, ycor() - 6 * k)
    goto(2 * k, 2 * k)
    goto(xcor() + 3 * k, ycor() + 9 * k)

tracer(0)
up()
color("red")
for x in range(-10, 20):
    for y in range(-10, 30):
        goto(x * k, y *k)
        dot(6)

mainloop()