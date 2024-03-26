import math
import os
import sys
# Add pieces directory to python path so modules can be imported from another directory
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, 'game', 'pieces' )
sys.path.append( mymodule_dir )

from game.board import Board
from game.player import Player

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

# flag indicating whether it is white's turn (True) or black's (False). White goes first
white_turn = True
# position of selected square
selected_sq = (-1, -1)
# flag indicating whether or not a piece has been selected
piece_selected = False
# position of location a piece will move to
move_to = (-1, -1)
# posible moves of selected piece
poss_moves = []

while running:
    
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if piece_selected == False:
                if white_turn:
                    # TODO: Make these functions
                    selected_sq = ( math.ceil((mouse_pos[0] - BASE_X) / SQUARE_SIZE), \
                                    9 - math.ceil(((mouse_pos[1] - BASE_Y) / SQUARE_SIZE)))
                    if 1 <= selected_sq[0] and selected_sq[0] <= 8 and 1 <= selected_sq[1] and selected_sq[1] <= 8:
                        if b.get_piece(selected_sq).team == "Black":
                            selected_sq = (-1, -1)
                            piece_selected = False
                        else:
                            piece_selected = True
                else:
                    selected_sq = ( 9 - math.ceil((mouse_pos[0] - BASE_X) / SQUARE_SIZE), \
                                    math.ceil(((mouse_pos[1] - BASE_Y) / SQUARE_SIZE)))
                    if b.get_piece(selected_sq).team == "White":
                        selected_sq = (-1, -1)
                        piece_selected = False
                    else:
                        piece_selected = True
                
            else:
                if white_turn:
                    move_to = ( math.ceil((mouse_pos[0] - BASE_X) / SQUARE_SIZE), \
                                9 - math.ceil(((mouse_pos[1] - BASE_Y) / SQUARE_SIZE)))
                else:
                    move_to = ( 9 - math.ceil((mouse_pos[0] - BASE_X) / SQUARE_SIZE), \
                                math.ceil(((mouse_pos[1] - BASE_Y) / SQUARE_SIZE)))
                if 1 <= move_to[0] and move_to[0] <= 8 and 1 <= move_to[1] and move_to[1] <= 8:
                    if move_to in b.get_possible_moves(selected_sq):
                        b.move_to(selected_sq, (move_to[0], move_to[1]))
                        selected_sq = (-1, -1)
                        move_to = (-1, -1)
                        white_turn = not white_turn
                        piece_selected = False
                    else:
                        if white_turn and b.get_piece(move_to).team == "Black" \
                        or not white_turn and b.get_piece(move_to).team == "White":
                            pass
                        else:
                            selected_sq = move_to

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # GAME RENDERING
    
    # render squares of board
    alternator = True
    row = 1
    col = 1
    if white_turn:
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
    else:
        for s in squares:
            color = ""
            if (9 - col, 9 - row) == selected_sq:
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

    if piece_selected:
        if white_turn:
            for move in b.get_possible_moves(selected_sq):
                pygame.draw.circle(screen, "grey", pygame.Vector2((BASE_X + move[0] * SQUARE_SIZE) - (SQUARE_SIZE / 2), (BASE_Y + (9 - move[1]) * SQUARE_SIZE) - (SQUARE_SIZE / 2)), SQUARE_SIZE * 0.25)
        else:
            for move in b.get_possible_moves(selected_sq):
                pygame.draw.circle(screen, "grey", pygame.Vector2((BASE_X + (9 - move[0]) * SQUARE_SIZE) - (SQUARE_SIZE / 2), (BASE_Y + move[1] * SQUARE_SIZE) - (SQUARE_SIZE / 2)), SQUARE_SIZE * 0.25)

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
