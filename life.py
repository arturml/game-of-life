import pygame
import sys
from pygame.locals import *

#        CONSTANTS
SIZE = 15
WIDTH = 900
Nx = WIDTH/SIZE
HEIGHT = 600
Ny = HEIGHT/SIZE
FPS = 5

#        R  G  B
BLACK = (0, 0, 0)
WHITE = (255,255,255)

def neighboors(x,y, grid):
    alives = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if 0 <= i < Nx and 0 <= j < Ny and (i,j) != (x,y):
                alives += int(grid[i][j])
    return alives

def draw_grid(screen, grid):

    for i in range(Nx):
        for j in range(Ny):
            if grid[i][j] == True:
                pygame.draw.rect(screen, BLACK, (i*SIZE,j*SIZE, SIZE, SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (i*SIZE,j*SIZE, SIZE, SIZE))

def draw_lines(screen, grid):
    for x in range(0,WIDTH,SIZE):
        pygame.draw.line(screen, BLACK, (x,0), (x,HEIGHT)) 

    for y in range(0,HEIGHT,SIZE):
        pygame.draw.line(screen, BLACK, (0,y), (WIDTH,y))

def start_screen(screen, grid):
    pygame.display.set_caption("Game of Life: click on the cells you wish to activate. Press Enter to start.")
    while True:
        

        draw_grid(screen, grid)
        draw_lines(screen, grid)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                coord = pygame.mouse.get_pos()
                i, j = coord[0]/SIZE, coord[1]/SIZE
                grid[i][j] = not grid[i][j]
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == K_RETURN:
                    return

        
        pygame.display.update()

def copy(M):
	return [row[:] for row in M]

def main():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    grid = [[False for y in range(Ny)] for x in range(Nx)]
    new_grid = copy(grid)
    start_screen(screen, grid)
    pygame.display.set_caption("Game of Life")
    
    while True:    
        for i in range(Nx):
            for j in range(Ny):
                    alives = neighboors(i, j, grid)
                    if grid[i][j] == True:
                        if alives in (2,3):
                    	     new_grid[i][j] = True
                    	else:
                    		new_grid[i][j]  = False
                    elif grid[i][j] == False:
                    	if alives == 3:
                            new_grid[i][j] = True
                        else:
                            new_grid[i][j] = False
        grid = copy(new_grid)  
            
        draw_grid(screen, grid)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
if __name__ == '__main__':
	main()
