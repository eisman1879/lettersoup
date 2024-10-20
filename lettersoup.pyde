import random  # To use random.choice and random.randint

gridSize = 8  # Size of the grid
grid = [['' for _ in range(gridSize)] for _ in range(gridSize)]  # 8x8 matrix
words = ['CAT', 'DOG', 'SUN']  # The words to hide

def setup():
    size(400, 400)  # Window size
    textFont(createFont("Arial", 24))
    fill_grid_with_random_letters()  # Step 1: Fill the grid with random letters
    hide_words_in_grid()  # Step 2: Hide the words

def draw():
    background(255)  # White background
    display_grid()  # Step 3: Show the grid

def fill_grid_with_random_letters():
    for i in range(gridSize):
        for j in range(gridSize):
            grid[i][j] = chr(random.randint(65, 90))  # Random uppercase letters A-Z

def hide_words_in_grid():
    for word in words:
        place_word_randomly(word)  # Place each word randomly

def place_word_randomly(word):
    # Randomly choose direction using random integers
    direction = random.randint(0, 2)  # 0 for horizontal, 1 for vertical, 2 for diagonal
    
    # Find a random valid start position based on word length and direction
    if direction == 0:  # HORIZONTAL
        row = random.randint(0, gridSize - 1)
        col = random.randint(0, gridSize - len(word))  # Ensure word fits horizontally
    elif direction == 1:  # VERTICAL
        row = random.randint(0, gridSize - len(word))  # Ensure word fits vertically
        col = random.randint(0, gridSize - 1)
    else:  # DIAGONAL
        row = random.randint(0, gridSize - len(word))  # Ensure word fits diagonally
        col = random.randint(0, gridSize - len(word))
    
    # Place the word in the chosen direction
    for i in range(len(word)):
        if direction == 0:  # HORIZONTAL
            grid[row][col + i] = word[i]
        elif direction == 1:  # VERTICAL
            grid[row + i][col] = word[i]
        else:  # DIAGONAL
            grid[row + i][col + i] = word[i]

def display_grid():
    textAlign(CENTER, CENTER)
    fill(000)
    for i in range(gridSize):
        for j in range(gridSize):
            text(grid[i][j], j * 50 + 25, i * 50 + 25)  # Display letters in grid cells
