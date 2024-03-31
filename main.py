import math
import os
import sys

# Add pieces directory to python path so modules can be imported from another directory
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, 'game', 'pieces' )
sys.path.append( mymodule_dir )

from game.pieces.bishop import Bishop
from game.pieces.knight import Knight
from game.pieces.queen import Queen
from game.pieces.rook import Rook

from game.board import Board

# pygame setup
import pygame
pygame.init()
pygame.freetype.init()
my_font = pygame.freetype.SysFont(pygame.font.get_default_font(), 30)

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
# flag for a pawn at the end of the board
pawn_at_end = False
# flag set when a player has made a move
moved = False

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
                    if pawn_at_end:
                        pawn = b.promotion("White")
                        x = pawn[0]
                        if selected_sq[0] == x:
                            if selected_sq[1] == 8:
                                b.pieces[promote] = Queen(team)
                                pawn_at_end = False
                            elif selected_sq[1] == 7:
                                b.pieces[promote] = Knight(team)
                                pawn_at_end = False
                            elif selected_sq[1] == 6:
                                b.pieces[promote] = Rook(team)
                                pawn_at_end = False
                            elif selected_sq[1] == 5:
                                b.pieces[promote] = Bishop(team)
                                pawn_at_end = False
                    elif 1 <= selected_sq[0] and selected_sq[0] <= 8 and 1 <= selected_sq[1] and selected_sq[1] <= 8:
                        if b.get_piece(selected_sq).team == "Black":
                            selected_sq = (-1, -1)
                            piece_selected = False
                        else:
                            piece_selected = True
                else:
                    selected_sq = ( 9 - math.ceil((mouse_pos[0] - BASE_X) / SQUARE_SIZE), \
                                    math.ceil(((mouse_pos[1] - BASE_Y) / SQUARE_SIZE)))
                    if pawn_at_end:
                        pawn = b.promotion("Black")
                        x = pawn[0]
                        if selected_sq[0] == x:
                            if selected_sq[1] == 1:
                                b.pieces[promote] = Queen(team)
                                pawn_at_end = False
                            elif selected_sq[1] == 2:
                                b.pieces[promote] = Knight(team)
                                pawn_at_end = False
                            elif selected_sq[1] == 3:
                                b.pieces[promote] = Rook(team)
                                pawn_at_end = False
                            elif selected_sq[1] == 4:
                                b.pieces[promote] = Bishop(team)
                                pawn_at_end = False
                    elif 1 <= selected_sq[0] and selected_sq[0] <= 8 and 1 <= selected_sq[1] and selected_sq[1] <= 8:
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
                        moved = True
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

    if pawn_at_end:
        if white_turn:
            promote = b.promotion("White")
        else:
            promote = b.promotion("Black")
        x = promote[0]
        y = promote[1]
        if white_turn:
            team = "White"
            x = x - 1
            y = 8 - y
        else:
            team = "Black"
            x = 8 - x
            y = y - 1
        pygame.draw.rect(screen, "grey", pygame.Rect((BASE_X + x * SQUARE_SIZE, BASE_Y + y * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE * 4)))
        screen.blit(Queen(team).to_image(), (BASE_X + x * SQUARE_SIZE, BASE_Y + y * SQUARE_SIZE))
        screen.blit(Knight(team).to_image(), (BASE_X + x * SQUARE_SIZE, BASE_Y + y * SQUARE_SIZE + 1 * SQUARE_SIZE)) #knight
        screen.blit(Rook(team).to_image(), (BASE_X + x * SQUARE_SIZE, BASE_Y + y * SQUARE_SIZE + 2 * SQUARE_SIZE))
        screen.blit(Bishop(team).to_image(), (BASE_X + x * SQUARE_SIZE, BASE_Y + y * SQUARE_SIZE + 3 * SQUARE_SIZE))

    if (not b.promotion("White") == None or not b.promotion("Black") == None) and not pawn_at_end:
        pawn_at_end = True

    if piece_selected and not pawn_at_end:
        if white_turn:
            for move in b.get_possible_moves(selected_sq):
                pygame.draw.circle(screen, "grey", pygame.Vector2((BASE_X + move[0] * SQUARE_SIZE) - (SQUARE_SIZE / 2), (BASE_Y + (9 - move[1]) * SQUARE_SIZE) - (SQUARE_SIZE / 2)), SQUARE_SIZE * 0.25)
        else:
            for move in b.get_possible_moves(selected_sq):
                pygame.draw.circle(screen, "grey", pygame.Vector2((BASE_X + (9 - move[0]) * SQUARE_SIZE) - (SQUARE_SIZE / 2), (BASE_Y + move[1] * SQUARE_SIZE) - (SQUARE_SIZE / 2)), SQUARE_SIZE * 0.25)

    if b.checkmate("White"):
        render = my_font.render("Black Wins")
        text = render[0]
        rect = pygame.Rect((SCREEN_X / 2 - (render[1].w / 2) - 5, SCREEN_Y / 2 - (render[1].h / 2) - 5), (render[1].w + 10, render[1].h + 10))
        pygame.draw.rect(screen, "white", rect)
        screen.blit(text, (SCREEN_X / 2 - (render[1].w / 2), SCREEN_Y / 2 - (render[1].h / 2)))
    elif b.checkmate("Black"):
        render = my_font.render("White Wins")
        text = render[0]
        rect = pygame.Rect((SCREEN_X / 2 - (render[1].w / 2) - 5, SCREEN_Y / 2 - (render[1].h / 2) - 5), (render[1].w + 10, render[1].h + 10))
        pygame.draw.rect(screen, "white", rect)
        screen.blit(text, (SCREEN_X / 2 - (render[1].w / 2), SCREEN_Y / 2 - (render[1].h / 2)))
    elif (white_turn and b.stalemate("White")) or (not white_turn and b.stalemate("Black")):
        render = my_font.render("Stalemate")
        text = render[0]
        rect = pygame.Rect((SCREEN_X / 2 - (render[1].w / 2) - 5, SCREEN_Y / 2 - (render[1].h / 2) - 5), (render[1].w + 10, render[1].h + 10))
        pygame.draw.rect(screen, "white", rect)
        screen.blit(text, (SCREEN_X / 2 - (render[1].w / 2), SCREEN_Y / 2 - (render[1].h / 2)))
    
    if moved and not pawn_at_end:
        moved = False
        white_turn = not white_turn

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
