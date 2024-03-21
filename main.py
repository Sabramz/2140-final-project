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
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

b = Board()

SQUARE_SIZE = 60

squares = []
for i in range(SQUARE_SIZE, SQUARE_SIZE * 9, SQUARE_SIZE):
    for j in range(SQUARE_SIZE, SQUARE_SIZE * 9, SQUARE_SIZE):
        r = pygame.Rect(i, j, SQUARE_SIZE, SQUARE_SIZE)
        squares.append(r)
print(squares)

# flag indicating whether it is white's turn (True) or black's (False). White goes first
white_turn = True

while running:
    
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # GAME RENDERING
    
    # render squares of board
    alternator = True
    count = 0
    for s in squares:
        color = ""
        if alternator:
            color = "white"
        else:
            color = "brown"
        pygame.draw.rect(screen, color, s)

        count += 1
        if count != 8:
            alternator = not alternator
        else:
            count = 0

    # render pieces
    for p in b.piece_images(not white_turn):
        screen.blit(p[0], p[1])

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
