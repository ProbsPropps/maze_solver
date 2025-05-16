from point import Point, Line


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, x2, y1, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1,y1), Point(x1, y2))
            self._win.draw_line(line, "white")            
        if self.has_right_wall:
            line = Line(Point(x2,y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x2,y1), Point(x2, y2))
            self._win.draw_line(line, "white") 
        if self.has_top_wall:
            line = Line(Point(x1,y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1,y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1,y2), Point(x2, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1,y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        center_x_first = int((self._x1 + self._x2) / 2)
        center_x_second = int((to_cell._x1 + to_cell._x2) / 2)
        center_y_first = int((self._y1 + self._y2) / 2)
        center_y_second = int((to_cell._y1 + to_cell._y2) / 2)
        line = Line(Point(center_x_first, center_y_first), Point(center_x_second, center_y_second))
        color = "red"
        if undo:
            color = "grey"
        self._win.draw_line(line, color)
        