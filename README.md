# Overview
Our final project will be a chess game implemented using the pygame framework. The basic functionality will be a welcome screen, and a chess game that can be played by two players on the same computer. The chess game will be rendered in a window using pygame. The game will know when a player has won, allow players to draw, and allow players to resign if they feel the game has been lost. Players will also be able to highlight squares in order to plan out their next move. There will be modes of chess available, such as blitz chess or chess with no clock, that the player will be able to choose from. The program can also keep score between the players to allow them to play multiple games in a series. 

If time allows for this, the scope of the project can be expanded to use AI to evaluate the player’s moves, either during or after the game. The player can choose to play against an AI. The games can be saved and reviewed using an AI evaluator. Networking can be utilized to allow two players on two separate machines to play over a network. None of these features are guaranteed, as they may prove too difficult or time consuming for our group.

# Organization

Game assets, such as sprites, can be found in **assets**. All game logic will be found in **game**. UI components will be found in **ui**.

# Running

To run the game, first you must install the python virtual environment below. Once inside of the virtual environment, run

```
python main.py
```

To exit the game, just close the game window

# Installation Instructions

Clone this repository (and enter the directory). Install python and pip if you do not have them on your computer.

Install virtualenv:
```
pip install virtualenv
```

Create a new virtual environment:
```
python -m venv env
```

# Activate the environment:

On Mac:
```
source env/bin/activate
```
On Windows:
```
env/Scripts/activate.bat //In CMD
env/Scripts/Activate.ps1 //In Powershel
```

Once you are in the environment, install the program's requirements:
```
pip install -r requirements.txt
```

To leave the virtual environment, run:
```
deactivate
```

# Sources

Chess pieces were sourced from https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent
