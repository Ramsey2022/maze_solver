from pyamaze import maze
m=maze(5, 5)
m.CreateMaze()

#Creates dictionary with the maze cells as keys and values as another dictionary of (N)orth (S)outh (E)ast (W)est. 1 means path is open, 0 means path is closed
print(m.maze_map)

#Creates a list of all cells
print(m.grid)

m.run()