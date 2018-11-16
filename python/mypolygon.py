import turtle

turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def name(a, length):
    square(a, length)

bob = turtle.Turtle()
length = int(input())
name(bob, length)
turtle.mainloop()
