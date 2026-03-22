'''
Jack — 9.5 / 10

Overall

One of the strongest submissions.

This student demonstrates a very clear conceptual understanding of:

the search tree
the shared mutable board
symmetry reduction

Strengths

Excellent explanation of why moves are undone.
Clear STI reasoning.
Good explanations of helper functions.

Example of strong insight:

The board is reused and moves are erased instead of creating millions of lists.

That is exactly the core computational idea behind the program.

Weaknesses

Slightly conversational tone in explanations.

AI likelihood

Moderate.

Reasons:

Some phrasing resembles AI explanations.
However the informal tone (“I kept getting confused by this at first”) suggests personal reasoning.

Estimated probability of AI assistance: 30–40%

GRADE 99

'''

"""
Homework: Reading Code with State / Transitions / Invariants (Tic-Tac-Toe)

This program brute-forces tic-tac-toe WITHOUT recursion.

What it actually counts:
- It explores all possible games where X starts and players alternate.
- The search STOPS as soon as someone wins (a terminal state).
- It also records full boards that end in a tie.
- It tracks UNIQUE *terminal* boards “up to symmetry” (rotations + reflections),
  meaning rotated/flipped versions are treated as the same terminal board.

YOUR TASKS:

RULE:  Do not change any executable code (no reformatting logic, no renaming variables, no moving lines). 
       Only add/replace comments and docstrings.
       
1) Define STATE for this program.
   - What variables change as the program runs?
The state for this program is mainly the currrent state of the board. As the game progresses and we get moves put on the board, all our variables having to due wiht win sceanrios change so we can establish a winner. The main ones are board, x_win, o_win etc.

2) Explain where TRANSITIONS happen.
Transitions happen whenever we move from one board to another so whenever a move is placed. 
   - Where does the state change? (where in the code, which functions)
   This happens when we have to start the program again and have a new game or a new move is placed. One example is in record full board becuase this happems after we have a winner determined.

3) Identify 4 INVARIANTS.

   - What properties remain true as the program runs (and what checks enforce them).
   1- players alternate turns. Enforced by structure of our nested loop
     2- Game stops when win condition is met. Has winner function to see if sum=30.
     3- same space may not be pikced twice. in loops we only allow the move to place if the space is ""
     4- inputs can only be int 1-9. Moves and board created by range (9)

4) For every function that says ''' TODO ''', replace that docstring with a real explanation
   of what the function does (1-4 sentences).
5) Add inline comments anywhere you see "# TODO" explaining what that code block is doing.
6) DO NOT USE AI. Write 5-8 sentences explaining one non-obvious part (choose one):  
   (a) symmetry logic (what makes a board unique), 
   (b) why we undo moves, 

We undo moves so the machine can keep replaying games and explore different end scenarions. We only have one created board and if we did not undo these moves in the loop structure, it would keep playing games over & over on one board which would then screw up win conditions bc of how they're calculated. Undoing moves ensures our board reutnrs to standard 3x3 grid state following each time we reach full board. 
   (c) why standard_form() produces uniqueness


7) The output from the program is two print statements:
       127872
       138 81792 46080 91 44 3
print(full_boards)
print(len(unique_seen), x_wins_on_full_board, draws_on_full_board, x_wins, o_wins, ties)

    explain what each number represents.

12782- # of games played and boards seen
138- number of unique formal board outcomes excluding rotations & duplicates
81792- total X wins
46080- total draws observed
91- X wins
44- O wins
3- ties

Submission:
- Update this file with your answers. Commit and sync

"""

# ----------------------------
# Global running totals (STATE)
# ----------------------------

unique_seen = []             # TODO: Stores boards as unique ensures we don't get dupliuctes
board = [' '] * 9            # TODO: Current tic tac toe board as a list

full_boards = 0              # TODO: Counts total games ran
x_wins_on_full_board = 0     # TODO: Games where X wins
draws_on_full_board = 0      # TODO: Draws 

x_wins = 0                   # TODO: When X wins 
o_wins = 0                   # TODO: Wwhen O wins
ties = 0                     # TODO: Games that end in tie


# ----------------------------
# Board representation helpers
# ----------------------------

def to_grid(flat_board: list[str]) -> list[list[str]]:
    ''' Converts our board from a list of 9 into 3x3 grid. easier to check values & winner '''
    grid = []
    for row in range(3):
        row_vals = []
        for col in range(3):
            row_vals.append(flat_board[row * 3 + col])
        grid.append(row_vals)
    return grid


def rotate_clockwise(grid: list[list[str]]) -> list[list[str]]:
    ''' Returns our 3x3 grid rotated clockwise.  '''
    rotated = [[' '] * 3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            rotated[c][2 - r] = grid[r][c]
    return rotated


def flip_vertical(grid: list[list[str]]) -> list[list[str]]:
    ''' Reverses our rows but same contents just flipped '''
    return [grid[2], grid[1], grid[0]]


def standard_form(flat_board: list[str]) -> list[list[str]]:
    ''' Creates a standard version of the board so symmetric boards are treated the same. '''
    grid = to_grid(flat_board)
    flipped = flip_vertical(grid)

    variants = []
    for _ in range(4):
        variants.append(grid)
        variants.append(flipped)
        grid = rotate_clockwise(grid)
        flipped = rotate_clockwise(flipped)

    return min(variants)


def record_unique_board(flat_board: list[str]) -> None:
    ''' ID when we see a board we havent seen before then what the result is '''
    global x_wins, o_wins, ties

    rep = standard_form(flat_board)

    # TODO: We check this to make sure we have not seen this board before 
    if rep not in unique_seen:
        unique_seen.append(rep)

        # TODO: X wins, O wins, Tie
        winner = who_won(flat_board)
        if winner == 'X':
            x_wins += 1
        elif winner == 'O':
            o_wins += 1
        else:
            ties += 1


# ----------------------------
# Game logic
# ----------------------------

def has_winner(flat_board: list[str]) -> bool:
    ''' Checks if there is a winner by checking all of the winning combos. returns trye if theres a winner '''
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [6, 4, 2],             # diagonals
    ]

    for line in winning_lines:
        score = 0
        for idx in line:
            if flat_board[idx] == 'X':
                score += 10
            elif flat_board[idx] == 'O':
                score -= 10
        if abs(score) == 30:
            return True

    return False


def who_won(flat_board: list[str]) -> str:
    ''' Takes the last step and then tells us who won, x, o , or tie  '''
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [6, 4, 2],             # diagonals
    ]

    for line in winning_lines:
        score = 0
        for idx in line:
            if flat_board[idx] == 'X':
                score += 10
            elif flat_board[idx] == 'O':
                score -= 10

        if score == 30:
            return 'X'
        elif score == -30:
            return 'O'

    return 'TIE'


def should_continue(flat_board: list[str], move_number: int) -> bool:
    ''' '''
    # TODO: WWhen we have a winner
    if has_winner(flat_board):
        record_unique_board(flat_board)
        return False
    return True


def record_full_board(flat_board: list[str]) -> None:
    ''' Records when we have a board with 9/9 spaces filled counts if thats a x win or a tie '''
    global full_boards, x_wins_on_full_board, draws_on_full_board

    # TODO: This is a terminal state because the board is full (9 moves).    I dont know what you want us to say here
    record_unique_board(flat_board)
    full_boards += 1

    # TODO: On a full board, either X has won (last move) or it is a draw. 
    if has_winner(flat_board):
        x_wins_on_full_board += 1
    else:
        draws_on_full_board += 1


# ----------------------------
# Brute force search (9 nested loops)
# ----------------------------

# TODO: The transitions take place whenever the board changes so either palcing or removing a move


# TODO: This is in full and unique boards because this is how we check to see if we have a winner and we transition to run the program again. 

# Move 1: X
for x1 in range(9):
    board[x1] = 'X'
    if should_continue(board, 1):

        # Move 2: O
        for o1 in range(9):
            if board[o1] == ' ':
                board[o1] = 'O'
                if should_continue(board, 2):

                    # Move 3: X
                    for x2 in range(9):
                        if board[x2] == ' ':
                            board[x2] = 'X'
                            if should_continue(board, 3):

                                # Move 4: O
                                for o2 in range(9):
                                    if board[o2] == ' ':
                                        board[o2] = 'O'
                                        if should_continue(board, 4):

                                            # Move 5: X
                                            for x3 in range(9):
                                                if board[x3] == ' ':
                                                    board[x3] = 'X'
                                                    if should_continue(board, 5):

                                                        # Move 6: O
                                                        for o3 in range(9):
                                                            if board[o3] == ' ':
                                                                board[o3] = 'O'
                                                                if should_continue(board, 6):

                                                                    # Move 7: X
                                                                    for x4 in range(9):
                                                                        if board[x4] == ' ':
                                                                            board[x4] = 'X'
                                                                            if should_continue(board, 7):

                                                                                # Move 8: O
                                                                                for o4 in range(9):
                                                                                    if board[o4] == ' ':
                                                                                        board[o4] = 'O'
                                                                                        if should_continue(board, 8):

                                                                                            # Move 9: X
                                                                                            for x5 in range(9):
                                                                                                if board[x5] == ' ':
                                                                                                    board[x5] = 'X'

                                                                                                    # Full board reached (terminal)
                                                                                                    record_full_board(board)

                                                                                                    # undo move 9
                                                                                                    board[x5] = ' '

                                                                                        # undo move 8
                                                                                        board[o4] = ' '

                                                                            # undo move 7
                                                                            board[x4] = ' '

                                                                # undo move 6
                                                                board[o3] = ' '

                                                    # undo move 5
                                                    board[x3] = ' '

                                        # undo move 4
                                        board[o2] = ' '

                            # undo move 3
                            board[x2] = ' '

                # undo move 2
                board[o1] = ' '

    # undo move 1
    board[x1] = ' '


print(full_boards)
print(len(unique_seen), x_wins_on_full_board, draws_on_full_board, x_wins, o_wins, ties)
