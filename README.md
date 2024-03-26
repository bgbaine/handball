# CS50P Final Project: Handball
## Video Demo:  [<URL HERE>]()
## What it is
This project is a simple clone of the classic [**Handball**](https://youtu.be/cQ9iGNSjwWo?t=17) game present in the first Coleco videogame, [**Coleco Telstar (1976)**](https://en.wikipedia.org/wiki/Coleco_Telstar_series#Model_comparison). Handball is a variation of the classic Atari's Pong (which also has a clone present in Coleco Telstar), the difference being that instead of competing against another person, the player competes alone against a wall that bounces the ball back to the them. The player cannot score, but if he fails to hit the ball back to the wall, a goal is scored. When a goal is scored, the ball is given back towards the player in a random direction (going upwards or downwards). If the scoreboard reaches eleven, the game ends. You can watch some gameplay [**here**](https://youtu.be/915a8Y-OpBs).

## How to play
When the game launches, the ball will be bouncing randomly on the screen until the player presses `Backspace` to start the game. If playing already, pressing `Backspace` restarts the game. `Up` `arrow` moves the paddle up, whereas `down` `arrow` moves the paddle down. Pressing `Escape` ends the game.

## Modules / libraries used
The game was fully written in **Python** and uses two built-in modules:

* `random`
* `sys`

The [**random**](https://docs.python.org/3/library/random.html) module was used to generate the random numbers responsible for directing the ball upwards or downwards towards the player. The [**sys**](https://docs.python.org/3/library/sys.html) module was used for general purposes, such as closing the game window and exiting the program if an error was found.

And one external library:

* `pygame`

[**Pygame**](https://www.pygame.org/docs/) was used to build the game itself (window, logic, player, player input, sound, etc).

## Files
The project folder contains the following files:

* `requirements.txt`
* `Handball.py`
* `project.py`
* `test_project.py`
* `README.md`

### `requirements.txt`
Contains all the `pip`-installable libraries required to run the project.

### `Handball.py`

A module called `Handball`. Contains four classes, `Block`, `Player`, `Ball` and `GameManager`.
#### `Block`
A subclass of `pygame`'s `Sprite` `class`. It creates a rectangular shape at a given position, with given dimensions and color. Its only method is the `Initializer`.
#### `Player`
Inherits from `Block`. It creates a paddle at a given position and with given dimensions, color and speed. This `class` contains the `court_collision` method, that ensures the player does not leave the screen and the `update` method, that updates player position and also calls the `court_collision` method.
#### `Ball`
Also inherits from `Block`. It creates a ball at a given position and with given dimensions, color and speed. Contains the `reset` method, that resets the ball's position, the `collision` method, that controls the collision of the ball with both the court and the paddle aswell as adding sound to those collisions, and the `update` method, that updates ball position and also the calls the `collision` method.
#### `GameManager`
Creates a Game Manager responsible for controling the game's logic. Contains the `restart` method, that restarts the game and plays the restart sound, the `draw_score` method, that draws the score on the screen, the `goal` method, that checks if goal was scored and plays the respective sound if so, and the `update` method, that updates the entire game, by drawing and updating both player and ball, and also calling the `draw_score` and `goal` methods.

### `project.py`
The main file, where the **main game loop** is. Imports the `Handball` module and constructs the objects created in the module (`Player`, `Ball` and `GameManager`). Also responsible for creating the game window, checking for user input and updating the screen at a given frame rate. Contains the `ensure_color` function, that ensures a valid color (0-255) is returned regardless of what was input, the `set_color` function, that returns a valid color tuple (validated by `ensure_color`) based on input, and the `set_speed` function, that returns a valid speed for each object (ball or paddle).

### `test_project.py`
Using [**pytest**](https://docs.pytest.org/en/7.1.x/contents.html), tests:

* `ensure_color` for different color inputs
* `set_color` for different tuples
* `set_speed` for different objects and speeds

### `README.md`
This file. Used to explain the whole project.

## Design choices
This project started with the intent of being a **Pong** clone. Before getting into any programming, [this](https://www.youtube.com/watch?v=fiShX2pTz9A) video of the original Pong was used to understand more about the game itself. The decisions to end the game when a player reaches eleven and to throw the ball to the player in random direction (upwards or downards) comes from here. Since the main goal of the project is to show our newly acquired skills (rather than the project itself) the first choice was to build the game in a more arkane way, by using **Turtle**, a built-in **Python** module used mainly not to create games, but basic 2D shapes and drawings. To learn about working with the module and how to develop Pong, [this](https://www.youtube.com/watch?v=C6jJg9Zan7w) tutorial was used alongside the **[official documentation](https://docs.python.org/3/library/turtle.html)**. Unfortunately, **Turtle** presented many problems in development, especially when updating the screen. Depending on user input, the ball would move significantly faster or slower, making the game unplayable.

The decision was then made to migrate to **Pygame**. Just as it was done with **Turtle**, alongside the **[official documentation](https://www.pygame.org/docs/)**, [these](https://www.youtube.com/watch?v=Qf3-aDXG8q4&list=PL8ui5HK3oSiEk9HaKoVPxSZA03rmr9Z0k) tutorials were used to learn about both **Pygame** and the development of **Pong** in it. Initially developed using just **procedural programing**, then "ported" to an **object orienteded** approach, more on that later. Working with **Pygame** made the game finally playable, but you had to play against another player locally, which is not very convenient. Thus, due to the popularity of the original game and the simplicity of its gameplay, the amount of content available online made the project feel not very unique. Looking for some old videogames in the **Pong** genre, **[Handball](https://www.youtube.com/watch?v=cQ9iGNSjwWo)** was found. The game is very similar to **Pong**, though not as popular. Instead of facing an opponent, the player competes against a wall that bounces the ball back to them. Sounds were extracted from [this](https://www.youtube.com/watch?v=915a8Y-OpBs) real **Handball** gameplay. This last shift made not just a better singleplayer game, but also made it possible to use the whole knowledge acquired in the different stages of development with **Turtle** and **Pygame** in a more authoral project.

In this paragraph, to be better understood, I'll express myself in the first person. It was really hard to implement my own version of the contents learned from these different modules. It is still very unatural to look at what looks like somebody's "solution" and "extract" something (even if not literal) since, in most of the course, we tend to "get our hands dirty" and really create most things from the ground up, in a more arkane and direct way, without any feeling of: "Am I 'peeking' in the actual solution?". Of course, I also understand that working on more advanced projects require a more profound reading of official documentation and even some of these "peeks" on some videos. I must finally add, then, that some concepts used to build the game (like the collision between the player and the ball, for example) are similar to the ones found in some of the **Pygame** tutorials cited before.

Back to **Handball**, the game imports the `Handball` module and runs on `project.py`. [**Mypy**](https://mypy.readthedocs.io/en/stable/) was used to ensure variables and functions were used correctly, except for **Pygame** objects, that couldn't be properly type checked. As mentioned before, the project also makes use of **object-oriented programming**. Initially, there was one file for each `class` (`Block.py`, `Player.py`, `Ball.py`, `GameManager.py`) what implied the creation of a **package**. For simplicity's sake, a general module called `Handball` was created, containing all classes.

Ultimately, about the unit testing. The fact that a game is basically an infinite loop that gets altered "x" frames per second makes it hard to create tests that are to be ran in isolation. Using [**pytest**](https://docs.pytest.org/en/7.1.x/contents.html) makes it even more difficult, since the framework was not made to test specifically games. For this reason, even though it was tried to make it in a more useful way, the three tests present in this project are really simple, and did not have to exist at all for the project to work. They were made with the only intent of fulfilling the project's requirements. In fact, the design of the program had to be altered (and get worse) just to make the unit testing possible.
