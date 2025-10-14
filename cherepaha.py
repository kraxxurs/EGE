from turtle import*

# №8137

# speed(0)
# screensize(2000, 2000)
# k = 25

# rt(90)
# for i in range(7):
#     fd(11 * k)
#     rt(45)
#     fd(8 * k)
#     rt(135)

# tracer(0)
# up()
# color("red")
# for x in range(-10, 5):
#     for y in range(-20, 5):
#         goto(x * k, y *k)
#         dot(3)


# №7410
screensize(3000, 3000)
k = 2
speed(0)
rt(45)
for i in range(10):
    write(pos())
    rt(45)
    fd(203 * k)
    rt(45)
up()
bk(40 * k)
rt(45)
down()
for i in range(5):
    write(pos())
    fd(20 * k)
    lt(90)

tracer(0)
up()
color("red")
for x in range(-10, 10):
    for y in range(-10, 100):
        goto(x * 10 * k, y * 10 * k)
        dot(2)

mainloop()
