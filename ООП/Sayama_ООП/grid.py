import tkinter as tk

LINESIZE = 5
POINTSIZE = 5

class Grid:
    """
    Grid has own coordinates (as in mathematics) in own units
    gwidth  - width in g units
    gheight - height in g units
    scale   - 1 g unit = scale pixels
    gltx    - left top point in x g coord
    glty    - left top point in y g coord
    gltx = - gwidth / 2
    glty = gheight / 2
    wx = (gx - gltx) * scale
    wy = (-gy + glty) * scale
    
    major_n - ticks per 10 g units
    """
    def done(self):
        self.root.mainloop()
        
    def __init__(self, gwidth=150, gheight=150, scale=5, d=10, minor_color='red', major_color='dark gray', axis_color='black'):
        self.root = tk.Tk()
        self.w = tk.Canvas(self.root, width=gwidth * scale, height=gheight * scale)
        self.w.pack()
        self.x0 = 0   # zero coordinates, x
        self.y0 = 0   # zero coordinates, y
        self.gwidth = gwidth
        self.gheight = gheight
        self.gltx = - gwidth // 2
        self.glty = gheight // 2
        self.scale = scale        # 1 grid unit = scale window pixels
        self.d = d
        self.major_n = 5
        self.minor_color = minor_color
        self.major_color = major_color
        self.axis_color = axis_color
        self.create()
        
    def win_coord(self, gx, gy):
       return ( (gx - self.gltx) * self.scale, (-gy + self.glty) * self.scale)
        
    def create(self):
        w = self.w
        #width = w.winfo_reqwidth()
        #height = w.winfo_reqheight()
        #print(w.winfo_reqwidth(), w.winfo_reqheight(), w.winfo_width(), w.winfo_height())

        xmin = self.gltx
        xmax = self.gltx + self.gwidth
        ymin = self.glty - self.gwidth
        ymax = self.glty

        # # draw | lines
        # i = 0
        # for x in range(0, xmax, self.d):
        #     col = self.line_color(i)
        #     wx, wy1 = self.win_coord(x, ymin)
        #     wx, wy2 = self.win_coord(x, ymax)
        #     w.create_line(wx, wy1, wx, wy2, fill=col)
        #     i += 1
        # i = 0
        # for x in range(0, xmin, -self.d):
        #     col = self.line_color(i)
        #     wx, wy1 = self.win_coord(x, ymin)
        #     wx, wy2 = self.win_coord(x, ymax)
        #     w.create_line(wx, wy1, wx, wy2, fill=col)
        #     i += 1
        
        # # draw ---- lines
        # i = 0
        # for y in range(0, ymax, self.d):
        #     col = self.line_color(i)
        #     x1, wy = self.win_coord(xmin, y)
        #     x2, wy = self.win_coord(xmax, y)
        #     w.create_line(x1, wy, x2, wy, fill=col)
        #     i += 1
        # i = 0
        # for y in range(0, ymin, -self.d):
        #     col = self.line_color(i)
        #     x1, wy = self.win_coord(xmin, y)
        #     x2, wy = self.win_coord(xmax, y)
        #     w.create_line(x1, wy, x2, wy, fill=col)
        #     i += 1
            
        w.create_line(*self.win_coord(xmin, 0), *self.win_coord(xmax, 0), fill=self.axis_color)
        w.create_line(*self.win_coord(0, ymin), *self.win_coord(0, ymax), fill=self.axis_color)

    def line_color(self, n=0):
        if n % self.major_n == 0:
            return self.major_color
        else:
            return self.minor_color
            
    def draw_rect(self, x1, y1, x2, y2, color):
        wx1, wy1 = self.win_coord(x1, y1)
        wx2, wy2 = self.win_coord(x2, y2)
        self.w.create_rectangle(wx1, wy1, wx2, wy2, width=LINESIZE, outline=color)
        
    def draw_line(self, x1, y1, x2, y2, color='blue'):
        wx1, wy1 = self.win_coord(x1, y1)
        wx2, wy2 = self.win_coord(x2, y2)
        self.w.create_line(wx1, wy1, wx2, wy2, width=LINESIZE, fill=color)

    def draw_dot(self, x, y, color='blue'):
        wx, wy = self.win_coord(x, y)
        print (f"win_coord : ({wx}, {wy})")
        self.w.create_oval(
            wx - POINTSIZE, wy - POINTSIZE, 
            wx + POINTSIZE, wy + POINTSIZE, 
            fill=color)
            

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point x={self.x} y={self.y}'
        
    def draw(self, color='blue'):
        g.draw_dot(self.x, self.y)
        
        
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def __repr__(self):
        return f'Rectangle x={self.x} y={self.y} width={self.width} height={self.height}'

    def draw(self, color='blue'):
        g.draw_rect(self.x, self.y, self.x + self.width, self.y + self.height, color)
    
        
if __name__ == '__main__':

    #root = tk.Tk()
    #w = tk.Canvas(root, width=800, height=600)
    #w.pack()

    g = Grid()

    # тут будет ваш код
    p = Point(0, 0)
    # print(p)
    p.draw()

    p1 = Point(-5, 5)
    # print(p1)
    p1.draw('red')

    # r = Rectangle(12, 22, 20, 10)
    # print(r)
    # r.draw()

    g.done()

