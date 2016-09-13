import turtle

def draw_square(a_turtle, size):
    '''draws a square with length of each side *size* '''
    a_turtle.pendown()
    for _ in range(4):
        a_turtle.forward(size)
        a_turtle.right(90)
    a_turtle.penup()

def draw_triangle(a_turtle, size, direction):
    '''draws an equilateral triangle with legnth of each side *size*.
    if *direction* is 'up', the triangle points upward,
    if *direction* is 'down', the triangle points downward.'''
    a_turtle.pendown()
    for _ in range(3):
        a_turtle.forward(size)
        if direction == 'up':
            a_turtle.left(120)
        elif direction == 'down':
            a_turtle.right(120)
    a_turtle.penup()

def _draw_fractal(a_turtle, size):
    '''helper function for draw_fractal()'''
    if size == 10:
        draw_triangle(a_turtle, size, 'down')
    else:
        draw_triangle(a_turtle, size, 'down')
        cor = [a_turtle.xcor(), a_turtle.ycor()]
        next_cor =  [[cor[0] + size/4, cor[1] + size/4*(3**.5)],
                     [cor[0] - size/4, cor[1] - size/4*(3**.5)],
                     [cor[0] + size/4*3, cor[1] - size/4*(3**.5)]]
        for start_pt in next_cor:
            a_turtle.setx(start_pt[0])
            a_turtle.sety(start_pt[1])
            _draw_fractal(a_turtle, size/2)

def draw_fractal(size):
    '''draws a Sierpinski triangle.
    size(int) must be a power of 2'''
    size *= 10
    canvas = turtle.Screen()
    canvas.bgcolor('yellow')
    canvas.setup (width=size+10, height=size+10, startx=0, starty=0)

    elfie = turtle.Turtle()
    elfie.shape('turtle')
    elfie.color('blue')
    elfie.speed(8)
    elfie.penup()
    elfie.setx(-200)
    elfie.sety(-200)

    draw_triangle(elfie, size, 'up')
    elfie.setx(elfie.xcor() + size/4)
    elfie.sety(elfie.ycor() + size/4 * (3**.5))
    _draw_fractal(elfie, size/2)

    canvas.exitonclick()


if __name__ == '__main__':
    draw_fractal(64)
