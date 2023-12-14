# For the parts here that do not resemble day14/part2.py,
# Credit to Jeremy Pitcock for having found a way to simply
# not loop through every sphere (like a normal person)
#

grid = [['#'] + list(i.strip()) + ['#'] for i in open('day14/input.txt').readlines()]
grid.append (['#'] * len(grid[0]))
grid.insert(0, ['#'] * len(grid[0]))

def tilt_north():
    open_pos = 0
    round_rock = 0
    for j in range(len(grid[0])):

        open_pos = 0
        round_rock = 0
        
        for i in range(len(grid)):

            if grid[i][j] == 'O':
                round_rock += 1

            elif grid[i][j] == '#':

                new_open = i+1
                
                #print (open_pos, round_rock)
                for k in range(open_pos, open_pos+round_rock):
                    
                    grid[k][j] = 'O'

                for k in range (open_pos+round_rock, new_open-1):
                    grid[k][j] = '.'

                open_pos = new_open
                

                round_rock = 0


def rotate_grid_clockwise():
    global grid
    grid = [list(row[::-1]) for row in zip(*grid)]


def tilt():
    for i in range (4):
        tilt_north()
        rotate_grid_clockwise()
    

grids = []
looped = False
i = 0

while i < 1000000000:

    tilt()

    if grid in grids and looped == False:
        looped = True

        # get really close to iteration 1000000000 without changing the grid
        difference = i - grids.index(grid)
        remaining = 1000000000 - i
        i += difference * (remaining // difference)

    grids.append([[c for c in g] for g in grid])

    i += 1


s = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[len(grid)-1-i][j] == 'O':
            s += i

print (s)
