# 348. Design Tic-Tac-Toe

**Difficulty:** Medium  
**Topic:** Design, Array, Hash Table, Matrix

## Problem Statement

Assume the following rules are for the tic-tac-toe game on an `n x n` board between two players:

1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves are allowed.
3. A player who succeeds in placing `n` of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the `TicTacToe` class:

- `TicTacToe(int n)` Initializes the object the size of the board `n`.
- `int move(int row, int col, int player)` Indicates that the player with id `player` makes a move at the cell `(row, col)`. The move is guaranteed to be a valid move. Returns:
  - `0` if no player wins after this move,
  - `1` if player 1 wins after this move,
  - `2` if player 2 wins after this move.

## Examples

**Example 1:**
```
Input:
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0,0,1], [0,2,2], [2,2,1], [1,1,2], [2,0,1], [1,0,2], [2,1,1]]

Output:
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation:
TicTacToe ticTacToe = new TicTacToe(3);
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
ticTacToe.move(0, 2, 2); // return 0 (no one wins)
ticTacToe.move(2, 2, 1); // return 0 (no one wins)
ticTacToe.move(1, 1, 2); // return 0 (no one wins)
ticTacToe.move(2, 0, 1); // return 0 (no one wins)
ticTacToe.move(1, 0, 2); // return 0 (no one wins)
ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
```

## Constraints

- `2 <= n <= 100`
- Player is either `1` or `2`.
- `1 <= row, col <= n - 1`
- `(row, col)` are unique for each different call to `move`.
- At most `n^2` calls will be made to `move`.

## Follow-up

Could you do better than `O(n^2)` per `move()` operation?
