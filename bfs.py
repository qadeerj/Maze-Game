from pyamaze import maze, agent, COLOR

def bfs(m):
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfsPath = {}
    
    while(len(frontier) > 0):
        currCell = frontier.pop(0)
        
        if(currCell == (1,1)): # goal state
            break
        
        for i in 'SNWE':
            if(m.maze_map[currCell][i]) == True:
                if(i=='N'):
                    childCell = (currCell[0]-1, currCell[1])
                
                elif(i=='S'):
                    childCell = (currCell[0]+1, currCell[1])
                    
                elif(i=='W'):
                    childCell = (currCell[0], currCell[1]-1)
                
                elif(i=='E'):
                    childCell = (currCell[0], currCell[1]+1)
                    
                
                if(childCell in explored):
                    continue
                    
                frontier.append(childCell)
                explored.append(childCell)
        
                bfsPath[childCell] = currCell

    fwdPath = {}
    cell = (1, 1)
    while(cell != start):
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return fwdPath
    
    
    
    
m = maze(10 , 10)
m.CreateMaze()
path = bfs(m)

a = agent(m, footprints=True)
m.tracePath({a : path})

m.run()