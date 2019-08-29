# Advanced Python Tutorial (Classes)
# Author: Melanie Chen
# Material taken from https://anandology.com/python-practice-book/object_oriented_programming.html 

'''
    Class for maintaining the state of a 2D array of "pixels."
    Note: (0,0) is located at the upper lefthand corner. x grows
    in the downward direction (corresponding to entries in the
    outer array). y grows in the rightward direction (corresponding
    to entires in each inner array).
'''
class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Note: [' '] * n yields a list of n ' ' characters. 
        self.data = [[' '] * width for i in range(height)]

    '''
         Mark the pixel at (row, col) with asterisk.
    '''
    def setpixel(self, row, col):
        self.data[row][col] = '*'

    '''
         Get the pixel at (row, col).
    '''
    def getpixel(self, row, col):
        return self.data[row][col]

    '''
        Display the canvas.
    '''
    def display(self):
        # Note: char.join(iter) joins every element in iter with 
        # char in between.
        print "\n".join(["".join(row) for row in self.data])
'''
    Base class Shape.
'''
class Shape:
    def paint(self, canvas):
        # We will override this method in derived classes.
        pass

'''
    Derived class Rectangle.
'''
class Rectangle(Shape):
    '''
        Constructor for the Rectangle class
    '''
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    '''
        Given one endpoint and the width of a horizontal line, 
        paint the appropriate pixels on the canvas.
    '''
    def hline(self, x, y, w, canvas):
        for i in range(w+1):
            canvas.setpixel(x+i,y)

    '''
        Given one endpoint and the height of the desired line, 
        paint the appropriate pixels on the canvas.
    '''
    def vline(self, x, y, h, canvas):
        for i in range(h+1):
            canvas.setpixel(x,y+i)
    '''
        Given a canvas, paint the individual vertical and
        horizontal lines on it.
    '''
    def paint(self, canvas):
        self.hline(self.x, self.y, self.w, canvas)
        self.hline(self.x, self.y + self.h, self.w, canvas)
        self.vline(self.x, self.y, self.h, canvas)
        self.vline(self.x + self.w, self.y, self.h, canvas)
        canvas.display()

'''
    Derived class Square.
'''
class Square(Rectangle):
    '''
        Given the coordinates of a corner and the size (which is
        equal to both height and width), initialize a new Square
        instance by referencing the Rectangle base class.
    '''
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size)

'''
    Derived class CompoundShape.
'''
class CompoundShape(Shape):
    '''
        Given a list of shapes, initialize an instance object that
        maintains the state of each shape.
    '''
    def __init__(self, shapes):
        self.shapes = shapes

    def paint(self, canvas):
        for s in self.shapes:
            s.paint(canvas)

if __name__ == "__main__":
   c = Canvas(5,5)
   r = Rectangle(0,0,2,3)
   r.paint(c)

# Bonus TODO: What could go wrong with this class? Hint: It has to do with out-of-bounds. How would we fix this?

# If a user tries to paint a line that exceeds the boundaries of the canvas, an exception will be raised. To fix this, we can test for this condition in setpixel() and print a user-friendly error message.

# Extra Bonus: TODO: Add Circle to this inheritance structure!

