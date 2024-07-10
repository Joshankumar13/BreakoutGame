# Breakout Game

## Description

The Breakout Game is a classic arcade game where the player controls a paddle to bounce a ball and break bricks on the screen. The game features simple controls, engaging gameplay, and a classic visual design. The objective is to clear the screen of bricks by hitting them with the ball while avoiding the ball falling off the bottom of the screen.

## Features

- **Paddle Control:**
  - Use the left and right arrow keys to move the paddle.
- **Ball Physics:**
  - The ball bounces off walls, the paddle, and bricks.
- **Collision Detection:**
  - Detects collisions between the ball, paddle, and bricks.
- **Game Over and Win States:**
  - Displays messages when the player wins or loses.
- **Dynamic Difficulty:**
  - The game becomes progressively harder as more bricks are destroyed.

## Live Demo

Watch the video: [click here](https://github.com/joshan-18/BreakoutGame/assets/167819562/a6cfc1ab-9735-4f41-82e8-5ea5472af60b)

## Screenshots

### Gameplay

![Gameplay](https://github.com/joshan-18/BreakoutGame/assets/167819562/658899ae-2409-49a2-959c-d1cb64c9eb7c)

### Game Over

![Game Over](https://github.com/joshan-18/BreakoutGame/assets/167819562/b1c58d0c-21e3-4e48-9d06-a5b694793dea)


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/joshan-18/BreakoutGame.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd BreakoutGame
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## How to Play

1. **Run the game:**

    ```bash
    python BreakOutGame.py
    ```

2. **Use the left and right arrow keys to move the paddle and prevent the ball from falling off the bottom edge of the screen.**

3. **Break all the bricks by bouncing the ball off the paddle. If the ball falls off the bottom edge, the game ends.**

4. **Win the game by breaking all the bricks.**

## Controls

- **Left Arrow**: Move paddle left.
- **Right Arrow**: Move paddle right.

## Project Structure

- **`BreakOutGame.py`**: Main game script containing the game loop and main logic.
- **`Paddle.py`**: Class definition for the paddle object and its behaviors.
- **`Ball.py`**: Class definition for the ball object and its behaviors.
- **`Bricks.py`**: Class definition for the brick objects and their arrangement.

## Game States

- **Running**: The game is in progress.
- **Game Over**: The ball touches the bottom edge of the screen.
- **Win**: All bricks are destroyed.

## Technologies Used

- **Programming Language:**
  - Python
- **Library:**
  - Pygame for game development

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- **Email:** joshanroy13@gmail.com

Enjoy playing the Breakout Game!
