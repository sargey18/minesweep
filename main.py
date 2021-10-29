import random

# let create a board object to represent the minesweeper game 
# this is so that we can just say "create a new board object, or dig here or render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # lets keep track of these parameters, they be helpful later 
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        # lets create the board 
        # helper function 
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()
        
        # initialize a set to keep track of which locations weve uncovered 
        # well save (row, col) tuples into this set 
        self.dug = set() # if we dig at 0,0 then self.dug = {(0,0)}
        
    def make_new_board(self):
        
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation you prefer, but since we have a 2-d board list of lists is most natural)
        
        # generate a new board this board is going to = none and then repeat that dimension size number of times, because that how long e want this to be 
        # then we will have dimesion size number of these lists so that we can get a square board 
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]  
        # this create an array like this:
        # [None, None, ..., None],
        # [None, None, ..., None],
        # [...                  ],
        # [None, None, ..., None],
        # we can see how this represents a board!
        
        # plant the bombs
        bombs = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1) # think aboutthis logix as we are literally assigning a number from zero, you know to the number of spots on the board and were assigning each spot on the board its own unique id 
            row = loc // self.dim_size #' how many times does my dimention size go into te location i chose thats the row we are indexing in
            col = loc % self.dim_size
            
            if board[row][col] == '*':
                # this means were actually planted a bomb there already so keep going 
                continue
            
            board[row][col] = '*' # plant the bomb
            bombs_planted += 1
            
        return board

    def assign_values_to_board(self):
        # make the notes here 
        


# play the game 

def play(dim_size=10, num_bombs=10):
    # step 1: create the board and plant the bombs 
    # step 2: show the user the board and ask for where they want to dig 
    # step 3a: if location is a bomb, show game over message 
    # step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # step 4: repeat steps 2 and 3a/3b until there are no more places to dig -> VICTORY!
    pass 

