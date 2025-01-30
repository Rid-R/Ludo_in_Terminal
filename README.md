# Custom Ludo Game Implementation in Terminal

## Overview
This is a Python implementation of Ludo, a classic board game, with some custom rule modifications. The game supports 2-4 players and features a command-line interface with a visual board representation. Players roll dice and move their pieces around the board, aiming to get all their pieces to the finish line while adhering to the game's rules.

## Features
- Support for 2-4 players
- Visual command-line board representation
- Custom dice rolling mechanism
- Piece movement validation
- Cutting (capturing) opponent pieces
- Safe zones where pieces cannot be captured
- Home run tracking for winning condition

## Game Rules
1. Each player is assigned a color (Red, Green, Blue, or Yellow)
2. Players must roll a 6 to bring pieces out from their starting area
3. Players can move their pieces based on dice rolls
4. Multiple pieces can be moved in a single turn if the roll allows
5. Pieces can be cut (sent back to start) when landed upon by an opponent
6. Safe squares (marked on the board) protect pieces from being cut
7. Players must get all four pieces to the finish line to win

## How to Play
1. Run the script and enter the number of players (2-4)
2. For each turn:
   - The current player's color is announced
   - A dice is automatically rolled
   - If pieces can be brought out from start, you'll be prompted to choose how many
   - Select which piece to move based on the available moves
   - The board is updated and displayed after each move

## Technical Implementation Details

### Key Functions

#### `roll()`
Simulates dice rolls with a special rule: if a 6 is rolled, the player continues rolling up to three times. Returns the sum of rolls unless three 6's are rolled, in which case it returns 0.

#### `allow(roll, color)`
Handles the logic for bringing pieces out from the starting area:
- Calculates how many pieces can be brought out based on the roll
- Requires 6 points per piece to bring out
- Updates piece positions and status accordingly

#### `move(color, board, temp, roll)`
Manages piece movement on the board:
- Validates moves based on game rules
- Handles piece movement around the board
- Manages entry into home run (final stretch)
- Updates board state after moves

#### `cut(temp, board, p)`
Implements the cutting mechanism:
- Checks if a piece can be cut
- Sends cut pieces back to their starting position
- Protects pieces on safe squares

#### `print_board(board)`
Creates a visual representation of the game board in the console using ASCII characters.

## Data Structures

### Board Representation
- The board is represented as a list of 59 positions (52 main board + 6 home run + 1 extra)
- Each position contains either empty space ("  ") or piece identifiers (e.g., "r1" for red piece 1)

### Player State
Player information is stored in a nested list structure:
- Color identifier
- Position tracking for each piece (4 pieces per player)
- Status flags for pieces (in start, on board, in home run)
- Home run completion status

## Requirements
- Python 3.x
- No additional libraries required (uses only standard library)

## Notes
- The game uses a command-line interface and requires manual input for moves
- Safe squares are positioned at specific intervals around the board
- Each player's home run path is unique to their color
- The winning condition is checked after each player's turn

## Known Limitations
- No save game functionality
- Cannot undo moves
- Limited input validation
- No graphical user interface

Feel free to modify the game rules or implementation to suit your preferences. The code is structured to make such modifications relatively straightforward.
