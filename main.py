import os
import sys
# Add pieces directory to python path so modules can be imported from another directory
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, 'game', 'pieces' )
sys.path.append( mymodule_dir )

from game.pieces.pawn import Pawn
from game.board import Board

def main():
    b = Board()
    b.new_game()

main()