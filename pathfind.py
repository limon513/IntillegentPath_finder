import curses
from curses import wrapper
import queue
import time

xcor = [-1,0,1,0]   #moves for up , down , left , right
ycor = [0,1,0,-1]

maze = [
    ["#", "#", " ", "#", "#", "#", "O", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", " ", "X"]
]

def print_maze(stdscr,path=[]):
    blue_=curses.color_pair(1)
    red_=curses.color_pair(2)
    for i,row in enumerate(maze):
        for j,val in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"X",red_)
            else:
                stdscr.addstr(i,j*2,val,blue_)
    


def find_start():
    for i, row in enumerate(maze):
        for j,val in enumerate(row):
            if val == "O":
                return i,j
            
    return None

def isvalid(x,y):
    if(x<0 or x>=len(maze) or y<0 or y>=len(maze[0])):
        return False
    
    return True


def find_neighbour(x,y):
    neighbour = []
    for i in range(0,4):
        if isvalid(x+xcor[i],y+ycor[i]):
            neighbour.append((x+xcor[i],y+ycor[i]))
    return neighbour
        
    


def find_path(stdscr):
    startingind = find_start()
    q = queue.Queue()
    q.put((startingind,[startingind]))
    visited = set()
    visited.add(startingind)
    while not q.empty():
        currentind , path = q.get()
        row, col = currentind
        
        stdscr.clear()
        print_maze(stdscr,path)
        time.sleep(0.5)
        stdscr.refresh()
        
        if maze[row][col] == "X":
            return path
        
        neighbour = find_neighbour(row,col)
        
        for x in neighbour:
            r,c = x
            if (r,c) in visited:
                continue
            if maze[r][c] == "#":
                continue
            
            visited.add((r,c))
            new_path = path+[x]
            q.put((x,new_path))



def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    find_path(stdscr)
    stdscr.getch()
    
    
wrapper(main)


