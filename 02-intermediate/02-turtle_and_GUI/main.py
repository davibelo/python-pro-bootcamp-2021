import colorsys
from turtle import Turtle, Screen


tim = Turtle()

tim.shape("turtle")
tim.color("#457b9d")

# drawing a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# drawing a dash line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


def get_N_HexCol(N=5):
    """generate a list of colors"""
    HSV_tuples = [(x * 2 / N, 0.75, 0.75) for x in range(N)]
    hex_out = []
    for rgb in HSV_tuples:
        rgb = map(lambda x: int(x * 255), colorsys.hsv_to_rgb(*rgb))
        hex_out.append('#%02x%02x%02x' % tuple(rgb))
    return hex_out


def draw_shape(num_sides):
    """draw a polygon"""
    tim.color(colours[num_sides])
    for _ in range(num_sides):
        tim.right(360/num_sides)
        tim.forward(50)


# setting the number of polygons
n = 20
# creating a array of colors
colours = get_N_HexCol(n)

# setting start position
tim.speed(0)
tim.penup()
tim.setposition(0, 300)
tim.pendown()

# drawing polygons
for num_sides in range(3, n):
    draw_shape(num_sides)

# setting screen to exit on click
screen = Screen()
screen.exitonclick()
