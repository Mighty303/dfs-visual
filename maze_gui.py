import tkinter as tk
from maze import dfs_solve_maze_recursive  # Import the solver

class MazeGUI:
    def __init__(self, maze, start, end, cell_size=50):
        self.maze = maze
        self.cell_size = cell_size
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = start
        self.end = end

        # Solve the maze and store the path
        self.path = dfs_solve_maze_recursive(maze, start, end)

        # Create main window
        self.root = tk.Tk()
        self.root.title("Maze")

        # Create canvas
        self.canvas = tk.Canvas(
            self.root, 
            width=self.cols * cell_size,
            height=self.rows * cell_size
        )
        self.canvas.pack()

        self.draw_maze()
        self.draw_path()

    def draw_maze(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                color = "black" if self.maze[i][j] == 1 else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_path(self):
        if not self.path:
            return
        for (i, j) in self.path:
            x1 = j * self.cell_size + self.cell_size // 4
            y1 = i * self.cell_size + self.cell_size // 4
            x2 = x1 + self.cell_size // 2
            y2 = y1 + self.cell_size // 2
            self.canvas.create_oval(x1, y1, x2, y2, fill="red")

        # Highlight start and end
        si, sj = self.start
        ei, ej = self.end
        self.canvas.create_rectangle(
            sj * self.cell_size, si * self.cell_size,
            (sj + 1) * self.cell_size, (si + 1) * self.cell_size,
            outline="green", width=3
        )
        self.canvas.create_rectangle(
            ej * self.cell_size, ei * self.cell_size,
            (ej + 1) * self.cell_size, (ei + 1) * self.cell_size,
            outline="blue", width=3
        )

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    maze = [
        [1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1]
    ]
    start = (0, 1)
    end = (6, 5)
    gui = MazeGUI(maze, start, end)
    gui.run()
