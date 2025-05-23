import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].visited,
            False
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].visited,
            False
        )
        self.assertEqual(
            m1._cells[int(num_cols/2)][int(num_rows/2)].visited,
            False
        )

if __name__ == "__main__":
    unittest.main()