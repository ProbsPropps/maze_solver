from cell import Cell
from window import Window
import time
import random

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                row.append(Cell(self._win))
            self._cells.append(row)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        draw_x1 = self._x1 + (i * self._cell_size_x)
        draw_x2 = self._x1 + ((i+1) * self._cell_size_x)
        draw_y1 = self._y1 + (j * self._cell_size_y)
        draw_y2 = self._y1 + ((j+1) * self._cell_size_y)
        self._cells[i][j].draw(draw_x1, draw_x2, draw_y1, draw_y2)
        self._animate()

    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            visit = []
            # figure out which cells can be visited
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                visit.append([i + 1, j])
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                visit.append([i - 1, j])
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                visit.append([i, j + 1])
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                visit.append([i, j - 1])

            # if we cannot visit another cell, just draw the current cell
            if visit == []:
                self._draw_cell(i,j)
                return
            # choose a random available direction to move
            direction = random.randrange(len(visit))
            k, l = visit[direction]
            # remove walls based on the cell we moved to
            # right
            if k == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # left
            if k == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # down
            if l == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            # up
            if l == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            # recursively visit the next cell
            self._break_walls_r(k,l)
            
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        # if we reached the end then we have solved the maze
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        # check each direction if there's a wall blocking
        # right
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i + 1][j].draw_move(self._cells[i][j], undo = True)
        # left
        if i - 1 >= 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i - 1][j].draw_move(self._cells[i][j], undo = True)
        # down
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j + 1].draw_move(self._cells[i][j], undo = True)
        # up
        if j - 1 >= 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j - 1].draw_move(self._cells[i][j], undo = True)
        return False