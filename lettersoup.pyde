import random  # To use random.choice and random.randint

global screen
screen = 0

gridSize = 8  # Size of the grid
grid = [[' ' for _ in range(gridSize)] for _ in range(gridSize)]  # 8x8 matrix with spaces
words = []  # The words to hide
input_field = ""

def setup():
    size(400, 400)  # Window size
    textFont(createFont("Arial", 24))

def draw():
    global screen
    background(255)  # White background
    if screen == 0:
        display_welcome()
        display_input_field()
    elif screen == 1:
        display_grid()  # Step 3: Show the grid


def fill_grid_with_random_letters():
    for i in range(gridSize):
        for j in range(gridSize):
            if grid[i][j] == ' ':
                grid[i][j] = chr(random.randint(65, 90))  # Random uppercase letters A-Z

def hide_words_in_grid():
    for word in words:
        place_word_randomly(word)  # Place each word randomly

def place_word_randomly(word):
    directions = [(0, 1), (1, 0), (1, 1)]  # Right, Down, Diagonal
    attempts = 0
    
    for attempts in range(1, 101):  # Try up to 100 times to place each word
        direction = random.choice(directions)
        row = random.randint(0, gridSize - 1)
        col = random.randint(0, gridSize - 1)
        
        if can_place_word(word, row, col, direction):
            place_word(word, row, col, direction)
            print("Placed word '{}' after {} attempts".format(word, attempts))
            return True
    
    print("Failed to place word '{}' after {} attempts".format(word, attempts))
    return False

def can_place_word(word, row, col, direction):
    dr, dc = direction
    if row + dr * (len(word) - 1) >= gridSize or col + dc * (len(word) - 1) >= gridSize:
        return False
    
    for i in range(len(word)):
        r, c = row + i * dr, col + i * dc
        if grid[r][c] != ' ' and grid[r][c] != word[i]:
            return False
    return True

def place_word(word, row, col, direction):
    dr, dc = direction
    for i in range(len(word)):
        r, c = row + i * dr, col + i * dc
        grid[r][c] = word[i]
        
def display_welcome():
    textAlign(CENTER, CENTER)
    fill(0)
    text('Welcome to Word Search', width/2, 50)
    
    # Display the dynamic message
    remaining_words = 3 - len(words)
    if remaining_words > 0:
        message = "Enter {} word{}".format(remaining_words, "s" if remaining_words > 1 else "")
        message += " to generate a lettersoup"
    
    textSize(16)  # Smaller text size for the message
    text(message, width/2, 100)
    textSize(24)  # Reset text size to default

def display_input_field():
    # Draw the input field box
    stroke(0)
    fill(240)  # Light gray 
    rect(50, height - 100, width - 100, 40)

    
    # Display the text in the input field
    fill(0)
    textAlign(LEFT, CENTER)
    text(input_field, 60, height - 80)
    
    # Display a blinking cursor
    if (frameCount // 30) % 2 == 0:
        text("|", 60 + textWidth(input_field), height - 80)


def keyPressed():
    global input_field, words
    if key == BACKSPACE:
        input_field = input_field[:-1]
    elif key == ENTER or key == RETURN:
        if input_field == "":
            return
        print("Entered:", input_field)
        words.append(input_field.upper()) # Add words in capitals
        print(words)
        check_if_ready()
        input_field = ""
    elif isinstance(key, unicode):
        if len(input_field) < 8 and key != " ":  # Only add character if word length is less than 8
            input_field += key

# When 3 words are added, start lettersalad
def check_if_ready():
    if len(words) >= 3:
        setup_lettersalad()
        

def setup_lettersalad():
    global screen
    hide_words_in_grid()  # Step 1: Hide the words
    fill_grid_with_random_letters()  # Step 2: Fill the remaining spaces with random letters
    screen = 1

def display_grid():
    textAlign(CENTER, CENTER)
    fill(0)
    for i in range(gridSize):
        for j in range(gridSize):
            text(grid[i][j], j * 50 + 25, i * 50 + 25)  # Display letters in grid cells
    save_grid_as_image()
    
def save_grid_as_image():
    # Save the current canvas as an image
    save("output/grid_output.jpg")
    print("Grid saved as 'grid_output.jpg' in the sketch folder")
    exit()
