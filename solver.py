from pyamaze import maze, agent, textLabel
from queue import PriorityQueue

#Heuristic function finding manhattan distance between two cells and estimates cheapest path from n to the goal
def h(cell1, cell2):
    x1,y1 = cell1
    x2,y2 = cell2
    
    return abs(x1 - x2) + abs(y1 - y2)

# Finds cost of path from start to n, then uses h() to estimate cheapest path from n to goal
def aStar(m):
    start = (m.rows, m.cols)
    g_score = {cell:float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell:float('inf') for cell in m.grid}
    f_score[start] = h(start, (1,1))
    
    # Use of PriorityQueue to implement selection by priority instead of FIFO in normal queue
    open=PriorityQueue()
    open.put((h(start, (1,1)), h(start, (1,1)), start))
    reverse_path = {}
    
    while not open.empty():
        curr_cell = open.get()[2]
        if curr_cell == (1,1):
            break
        for direction in 'ESNW':
            if m.maze_map[curr_cell][direction] == True:
                if direction == 'E':
                    child_cell = (curr_cell[0], curr_cell[1] + 1)
                if direction == 'S':
                    child_cell = (curr_cell[0] + 1, curr_cell[1])
                if direction == 'N':
                    child_cell = (curr_cell[0] - 1, curr_cell[1])
                if direction == 'W':
                    child_cell = (curr_cell[0], curr_cell[1] - 1)
                    
                temp_g_score = g_score[curr_cell] + 1
                temp_f_score = temp_g_score + h(child_cell, (1,1))
                
                if temp_f_score < f_score[child_cell]:
                    g_score[child_cell] = temp_g_score
                    f_score[child_cell] = temp_f_score
                    open.put((temp_f_score, h(child_cell, (1,1)), child_cell))
                    reverse_path[child_cell] = curr_cell
                    
    forward_path = {}
    cell = (1,1)
    while cell != start:
        forward_path[reverse_path[cell]] = cell
        cell = reverse_path[cell]
    return forward_path

if __name__ == '__main__':
    m=maze(10,15)
    m.CreateMaze()
    path = aStar(m)
    
    #adds visual for agent and the path it takes
    a = agent(m, footprints=True)
    m.tracePath({a:path})
    
    #adds text label to top left corner of app
    l = textLabel(m, 'A* path length', len(path) + 1)

#Creates dictionary with the maze cells as keys and values as another dictionary of (N)orth (S)outh (E)ast (W)est. 1 means path is open, 0 means path is closed
# print(m.maze_map)

#Creates a list of all cells
# print(m.grid)

    m.run()