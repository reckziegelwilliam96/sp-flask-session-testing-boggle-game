# Boggle

## The Game
The goal of the game is to get the highest point total. To gain points, players create words from a random assortment of letters in a 5x5 grid. 

Words can be created from adjacent letters – that is, letters which are horizontal or vertical neighbors of each other as well as diagonals. The letters must connect to each other in the proper sequence to spell the word correctly. This means that the next letter in the word can be above, below, left, or right of the previous letter in the word (excluding any letters previously used to construct the word).

### Written with: Python - Flask, JavaScript, Jinja, Unittest, JSON, "random" library, text files as dictionary, 

### Files included:
- **boggle.py:** Boggle class 
  - read_dict to read dictionary of words
  - make_board to make game board
  - check_valid_word to check user input is valid from dictionary
  - find_from to find words on the board
  - find to find user input word to find_from words
- **app.py:** Flask routes
  - display_board
  - add_word_guess
  - post_score
- **test.py**: Unittest cases
  - test_valid_word
  - __test_post_score__
  - __test_display_board__
  - __test to check_json__

Further Improvements:
- __tests to add__
- timer
- 'N x N' board size
- hint button
