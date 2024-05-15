# Project Title

This repository contains all the projects/task for the virtual python programming internship at CODSOFT

## File Descriptions

### to-do list.py

This file is responsible for creating a To-Do List application. The application is GUI-based, built using the tkinter library. It allows users to create, update, and track their to-do lists. The `ToDoList` class in this file has the following methods:

- `add_task()`: This method is used to add a new task to the list.
- `edit_task()`: This method is used to edit an existing task.
- `delete_task()`: This method is used to delete a task from the list.
- `complete_task()`: This method is used to mark a task as complete.

### password-generator.py

This file is responsible for creating a Password Generator application. The application allows users to specify the length and complexity of the password. The `password_generator` function in this file has the following parameters:

- `length`: This parameter specifies the desired length of the password.
- `upper`: This parameter specifies whether the password should include uppercase letters.
- `lower`: This parameter specifies whether the password should include lowercase letters.
- `numbers`: This parameter specifies whether the password should include numbers.
- `special`: This parameter specifies whether the password should include special characters.

### rock-paper-scissor-game.py

This file contains the code for a simple Rock, Paper, Scissors game. The game is implemented as a class `RockPaperScissors` with the following methods:

- `get_computer_choice()`: This method randomly selects the computer's choice from 'rock', 'paper', or 'scissors'.
- `determine_winner(user_choice, computer_choice)`: This method determines the winner of the game based on the user's choice and the computer's choice.
- `reset_game()`: This method resets the game by clearing the user's choice, the computer's choice, and the result.
- `play_game(user_choice)`: This method starts the game with the user's choice, determines the winner, updates the score, and sets the result.
