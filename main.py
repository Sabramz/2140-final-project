import math
import os
import sys
# Add pieces directory to python path so modules can be imported from another directory
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, 'game', 'pieces' )
sys.path.append( mymodule_dir )

from game.board import Board

# pygame setup
import pygame
pygame.init()
SCREEN_X = 1280
SCREEN_Y = 720
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
clock = pygame.time.Clock()
running = True

b = Board()

SQUARE_SIZE = 60
BASE_X = math.floor((SCREEN_X - SQUARE_SIZE * 8) / 2)
BASE_Y = math.floor((SCREEN_Y - SQUARE_SIZE * 8) / 2)

squares = []
for i in range(BASE_X, BASE_X + SQUARE_SIZE * 8, SQUARE_SIZE):
    for j in range(BASE_Y + SQUARE_SIZE * 8, BASE_Y, -SQUARE_SIZE):
        r = pygame.Rect(i, j - SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        squares.append(r)
print(squares)

# flag indicating whether it is white's turn (True) or black's (False). White goes first
white_turn = True
# position of selected square
selected_sq = (-1, -1)

while running:
    
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            selected_sq = ()
            if white_turn:
                selected_sq = ( math.ceil((mouse_pos[0] - BASE_X) / SQUARE_SIZE), \
                                9 - math.ceil(((mouse_pos[1] - BASE_Y) / SQUARE_SIZE)))
            else:
                selected_sq = ( math.ceil((mouse_pos[0] - BASE_X) / SQUARE_SIZE), \
                                math.ceil(((mouse_pos[1] - BASE_Y) / SQUARE_SIZE)))
            print(selected_sq)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # GAME RENDERING
    
    # render squares of board
    alternator = True
    row = 1
    col = 1
    for s in squares:
        color = ""
        if (col, row) == selected_sq:
            color = "yellow"
        elif alternator:
            color = "white"
        else:
            color = "brown"
        pygame.draw.rect(screen, color, s)

        row += 1
        if row < 9:
            alternator = not alternator
        else:
            col += 1
            row = 1

    # render pieces
    for p in b.piece_images(white_turn):
        p[1][0] = BASE_X + p[1][0] * SQUARE_SIZE
        p[1][1] = BASE_Y + p[1][1] * SQUARE_SIZE
        screen.blit(p[0], p[1])

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
