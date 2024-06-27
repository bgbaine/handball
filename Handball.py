############################################
#    cs50p/fproject/project/Handball.py    #
#    Final project                         #
############################################
"""Handball module with game object classes and game manager class for handball

This module contains four classes, Block, Player, Ball and GameManager that make
up the Handball game.

Block is a subclass of pygame's Sprite class. It creates a rectangular shape at
a given position, with given dimensions and color. Its only method is the
Initializer.

Player inherits from Block. It creates a paddle at a given position and with
given dimensions, color and speed. This class contains the court_collision
method, that ensures the player does not leave the screen and the update method,
that updates player position and also calls the court_collision method.

Ball, that also inherits from Block. It creates a ball at a given position and
with given dimensions, color and speed. Contains the reset method, that resets
the ball's position, the collision method, that controls the collision of the
ball with both the court and the paddle aswell as adding sound to those
collisions, and the update method, that updates ball position and also the calls
the collision method.

GameManager creates a Game Manager that's responsible for controling the game's
logic. Contains the restart method, that restarts the game and plays the restart
sound, the draw_score method, that draws the score on the screen, the goal
method, that checks if goal was scored and plays the respective sound if so, and
the update method, that updates the entire game, by drawing and updating both
player and ball, and also calling the draw_score and goal methods.

"""

import pygame
import random
import sys


class Block(pygame.sprite.Sprite):
    """This class creates a pygame sprite (shape).

    :param x_pos: X coordinate (in pixels) for the sprite to be placed
    :type x_pos int
    :param y_pos: Y coordinate (in pixels) for the sprite to be placed
    :type y_pos: int
    :param width: Width (in pixels) of the sprite
    :type width: int
    :param height: Height (in pixels) of the sprite
    :type height: int
    :param color: Color of the sprite
    :type color: tuple
    :return: None
    :rtype: None
    """

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
        color: tuple
    ) -> None:
        """Initializes a Block object (Initializer method)
        """
        # Calls parent class Initializer method
        super().__init__()

        # Set sprite's width and height
        self.width: int = width
        self.height: int = height

        # Set sprite's color
        self.color: tuple = color

        # Create an image with given dimensons and colors
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Create a rectangle with the image created priorly
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class Player(Block):
    """A subclass of block that creates a player (paddle).

    :param speed: The speed that is added when the player moves
    :type speed: float
    :param movement: The actual player speed and direction
    :type movement: float
    :return: None
    :rtype: None
    """

    def __init__(
            self,
            x_pos: int,
            y_pos: int,
            width: int = 15,
            height: int = 60,
            color: tuple = (211, 211, 211),
            speed: float = 18
    ) -> None:
        """Initializes a Player object (Initializer method)
        """
        # Calls parent class Initializer method
        super().__init__(x_pos, y_pos, width, height, color)

        # Set player speed
        self.speed: float = speed

        # Set player movement to be zero at start
        self.movement: int = 0

    def court_collision(self) -> None:
        """Controls player collision with the court(Instance method)

        :return: None
        :rtype: None
        """
        # Ensure player does not leave the court
        if self.rect.y <= 90:
            self.rect.y = 90
        elif self.rect.y >= 570:
            self.rect.y = 570

    def update(self) -> None:
        """Updates player position respecting collision (Instance method)

        :param rect.y: The current position of the player in the y axis
        :type rect.y: float
        :return: None
        :rtype: None
        """
        # Set player y position to be their current position added to their
        # movement (which is incremented (or decremented) in the main game loop)
        self.rect.y += self.movement

        # Call court_collision method
        self.court_collision()


class Ball(Block):
    """A subclass of block that creates a ball.

    :param speed: The speed that the ball moves
    :type speed: float
    :param player_sprite: Pygame object containing the player sprite (a Player
    object in a group)
    :type player_sprite: object
    :param wall_sound: Pygame object containing the sound file to be used when
    the ball hits the wall
    :type wall_sound: object
    :param paddle_sound: Pygame object containing the sound file to be used when
    the ball hits the paddle
    :type paddle_sound: object
    :param x_movement: The actual ball speed and direction in the x axis
    :type x_movement: int
    :param y_movement: The actual ball speed and direction in the x axis
    :type y_movement: int
    :return: None
    :rtype: None
    """

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int = 12,
        height: int = 12,
        color: tuple = (211, 211, 211),
        speed: int = 12,
        player_sprite=None
    ) -> None:
        """Initializes a Ball object (Initializer method)
        """
        # Calls parent class Initializer method
        super().__init__(x_pos, y_pos, width, height, color)

        # Set ball speed
        self.speed: int = speed

        # Import player sprite
        self.player_sprite = player_sprite

        # Set ball sounds
        self.wall_sound = pygame.mixer.Sound("assets/sounds/wall.wav")
        self.paddle_sound = pygame.mixer.Sound("assets/sounds/paddle.wav")

        # Throw ball randomly (set initial ball x and y movement to be random)
        self.x_movement: int = self.speed * random.choice((1, -1))
        self.y_movement: int = self.speed * random.choice((1, -1))

    def reset(self) -> None:
        """Resets ball (Instance method)

        :param rect.center: Places the center of the ball at determined
        coordianates
        :type rect.center: tuple
        :return: None
        :rtype: None
        """
        # Place ball on left wall and throw the ball back to the player in a
        # random y direction (set its y movement to be random)
        self.rect.center = (150, random.randrange(100, 625))
        self.x_movement *= -1
        self.y_movement *= random.choice((1, -1))

    def collision(self, playing: bool) -> None:
        """Controls ball collision (Instance method)

        :param playing: Controls the game status, True if playing
        :type playing: bool
        :return: None
        :rtype: None
        """
        # Ensure ball does not leave the court (if playing, play sound when ball
        # hits a wall)
        if self.rect.top <= 90 or self.rect.bottom >= 630:
            if playing:
                pygame.mixer.Sound.play(self.wall_sound)
            self.y_movement *= -1
        elif self.rect.left <= 90 or self.rect.right >= 1280:
            if playing:
                pygame.mixer.Sound.play(self.wall_sound)
            self.x_movement *= -1

        # If playing, detect collision with paddle
        if playing:
            if pygame.sprite.spritecollide(self, self.player_sprite, False):
                pygame.mixer.Sound.play(self.paddle_sound)
                collision_paddle = pygame.sprite.spritecollide(
                    self, self.player_sprite, False)[0].rect
                if abs(self.rect.right - collision_paddle.left) < 10 and self.x_movement > 0:
                    self.x_movement *= -1
                elif abs(self.rect.left - collision_paddle.right) < 10 and self.x_movement < 0:
                    self.x_movement *= -1
                elif abs(self.rect.top - collision_paddle.bottom) < 10 and self.y_movement < 0:
                    self.rect.top = collision_paddle.bottom
                    self.y_movement *= -1
                elif abs(self.rect.bottom - collision_paddle.top) < 10 and self.y_movement > 0:
                    self.rect.bottom = collision_paddle.top
                    self.y_movement *= -1

    def update(self, playing) -> None:
        """Updates ball position respecting collision (Instance method)

        :param rect.x: The current position of the ball in the x axis
        :type rect.x: object
        :param rect.y: The current position of the ball in the y axis
        :type rect.y: object
        :param playing: Controls the game status, True if playing
        :type playing: bool
        :return: None
        :rtype: None
        """
        # Set ball x position to be their current position added to their
        # movement (which is altered every time the ball hits something)
        self.rect.x += self.x_movement
        self.rect.y += self.y_movement

        # Call collision function
        self.collision(playing)


class GameManager:
    """This class creates a Game Manager (which controls the game's logic).

    :param display_surface: Pygame object containing the game's display surface
    :type display_surface: object
    :param game_font: Pygame object containing the font file to be used
    :type game_font: object
    :param game_color: Red, green and blue colors as a tuple (e.g. (255, 255,
    255))
    :type game_color: tuple
    :param restart_sound: Pygame object containing the sound file to be used
    when the game restarts
    :type restart_sound: object
    :param goal_sound: Pygame object containing the sound file to be used when
    a goal is scored
    :type goal_sound: object
    :param player_sprite: Pygame object containing the paddle sprite (a Player
    object in a group)
    :type player_sprite: object
    :param ball_sprite: Pygame object containing the the ball sprite (a Ball
    object in a group)
    :type ball_sprite: object
    :param score: Score
    :type score: int
    :param playing: Controls the game status, True if playing
    :type playing: bool
    :return: None
    :rtype: None
    """

    def __init__(self, display_surface, player_sprite, ball_sprite) -> None:
        """Initializes a GameManager object (Initializer method)
        """
        # Load display surface
        self.display_surface = display_surface

        # Import player and ball sprites
        self.player_sprite = player_sprite
        self.ball_sprite = ball_sprite

        # Load game font
        self.game_font = pygame.font.Font("assets/fonts/pong-score.ttf", 100)

        # Load game colors
        self.background_color = (0, 0, 0)
        self.game_color = (211, 211, 211)

        # Load game sounds
        self.restart_sound = pygame.mixer.Sound("assets/sounds/restart.wav")
        self.goal_sound = pygame.mixer.Sound("assets/sounds/goal.wav")

        # Set player score to zero
        self.score: int = 0

        # Set playing status to False
        self.playing: bool = False

    def restart(self) -> None:
        """Restarts the game (Instance method)

        :return: None
        :rtype: None
        """
        # Reset ball and play restart sound
        self.ball_sprite.sprite.reset()
        pygame.mixer.Sound.play(self.restart_sound)

    def draw_score(self) -> None:
        """Draws score on screen (Instance method)

        :return: None
        :rtype: None
        """
        # Setup text with player score to be drawn on screen
        player_text = self.game_font.render(f"{self.score}", False,
                                            self.game_color)

        # Draw player score on screen
        self.display_surface.blit(player_text, (1280/2 - 200, 100))

    def goal(self) -> None:
        """Resets ball (Instance method)

        :return: None
        :rtype: None
        """
        # If playing, add one to the score, reset the ball and play goal sound
        # when the ball touches the right of the screen (a goal is scored)
        if self.playing:
            if self.ball_sprite.sprite.rect.right >= 1280:
                self.score += 1
                self.ball_sprite.sprite.reset()
                pygame.mixer.Sound.play(self.goal_sound)

    def update(self) -> None:
        """Updates and controls the whole game (Instance method)

        :return: None
        :rtype: None
        """
        # Draw court
        self.display_surface.fill(self.background_color)
        pygame.draw.line(
            self.display_surface,
            self.game_color,
            (0, 75),
            (1280, 75),
            25
        )
        pygame.draw.line(
            self.display_surface,
            self.game_color,
            (75, 75),
            (75, 645),
            25
        )
        pygame.draw.line(
            self.display_surface,
            self.game_color,
            (0, 645),
            (1280, 645),
            25
        )
        pygame.draw.line(
            self.display_surface,
            self.game_color,
            (1280/2, 75),
            (1280/2, 645),
            10
        )

        # If playing, draw player and update its position
        if self.playing:
            self.player_sprite.draw(self.display_surface)
            self.player_sprite.update()

            # If score reaches eleven, end game
            if self.score == 11:
                self.playing = False

        # Draw ball and update its position
        self.ball_sprite.draw(self.display_surface)
        self.ball_sprite.update(self.playing)

        # Call draw_score and goal functions
        self.draw_score()
        self.goal()
