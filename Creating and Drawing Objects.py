from swampy.World import World

world = World()

class Point(object):
    """Represents a point in 2-D space."""
blank = Point()

blank.x = 3.0
blank.y = 4.0

class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """
bbox = Rectangle()


def draw_rectangle(canvas,rectangle):
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.rectangle(rectangle.bbox, fill=rectangle.color)

def draw_point(canvas, point):
    bbox =[[point.x, point.y], [point.x, point.y,]]
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.rectangle(bbox, width=2, fill="black")


canvas = world.ca(width=600, height=500, background='white')
bbox = [[-200,-100], [150, 100]]
canvas.rectangle(bbox, outline='black', width=2, fill='RoyalBlue')

canvas2 = canvas
canvas2.circle([-25,0], 70, outline=None, fill='yellow')

canvas3 = canvas
canvas3.circle([-35,0], 60, outline='black', fill='skyblue')

canvas4 = canvas
canvas4.circle([-50,0], 40, outline='red', fill='lightgreen')

canvas5 = canvas
canvas5.circle([-75,0], 15, outline='purple', fill='yellow')


world.mainloop()
