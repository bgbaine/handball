############################################
#    cs50p/fproject/project/project.py/    #
#    Final project                         #
############################################

from Handball import *


# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
FPS: int = 60

# Window setup
WINDOW_WIDTH: int = 1280
WINDOW_HEIGHT: int = 720
DISPLAY_SURFACE: object = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("CS50P Final Project: Handball")

# Main game function


def main():

    # Player attributes
    PLAYER_COLOR: tuple = set_color(211, 211, 211)
    PLAYER_SPEED: float = set_speed(1, 18)

    # Player object
    player: object = Player(1080, 360, 15, 60, PLAYER_COLOR, PLAYER_SPEED)

    # Add player to the player_sprite group of sprites (that only stores one
    # sprite)
    player_sprite: object = pygame.sprite.GroupSingle()
    player_sprite.add(player)

    # Ball attributes
    BALL_COLOR: tuple = set_color(211, 211, 211)
    BALL_SPEED: float = set_speed(0, 12)

    # Ball object
    ball: object = Ball(634, 354, 12, 12, BALL_COLOR, BALL_SPEED, player_sprite)

    # Add ball to the ball_sprite group of sprites (that only stores one sprite)
    ball_sprite: object = pygame.sprite.GroupSingle()
    ball_sprite.add(ball)

    # Game manager
    game_manager: object = GameManager(
        DISPLAY_SURFACE,
        player_sprite,
        ball_sprite
    )

    # Main game loop
    while True:

        # Check for events
        for event in pygame.event.get():

            # Check for clicking on window close button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for events pressing a determined key
            if event.type == pygame.KEYDOWN:

                # Start new game by pressing down the Return key
                if event.key == pygame.K_RETURN:
                    game_manager.restart()
                    game_manager.playing = True
                    game_manager.score = 0

                # End current game by pressing down the Esc key
                if event.key == pygame.K_ESCAPE:
                    game_manager.playing = False

                # Move paddle up by pressing the Up Arrow key
                if event.key == pygame.K_UP:
                    player.movement -= player.speed

                # Move paddle down by pressing the Down Arrow key
                if event.key == pygame.K_DOWN:
                    player.movement += player.speed

            # Check for events releasing a determined key
            if event.type == pygame.KEYUP:

                # Stop moving paddle up by releasing the Up Arrow key
                if event.key == pygame.K_UP:
                    player.movement += player.speed

                # Stop moving paddle down by releasing the Down Arrow key
                if event.key == pygame.K_DOWN:
                    player.movement -= player.speed

        # Update game
        game_manager.update()

        # Update screen on a pre-determined frame rate per second
        pygame.display.flip()
        clock.tick(FPS)


# Ensures a valid color is returned regardless of user input (Defaults to 211)
def ensure_color(color=211) -> int:

    # Ensure color input is a valid number
    try:
        if color < 0:
            color = 0
        elif color > 255:
            color = 255

    # If color is not a number, exit program
    except TypeError:
        sys.exit("Color must be a number.")

    # If we've reached this far, return color
    return int(color)


# Return valid color tuple (Defaults to (211, 211, 211))
def set_color(red=211, green=211, blue=211) -> tuple:

    # Ensure colors input are valid
    red = ensure_color(red)
    green = ensure_color(green)
    blue = ensure_color(blue)

    # If we've reached this far, return tuple
    return (red, green, blue)


# Returns valid speed for each object (0 being a ball, anything else being a
# paddle)
def set_speed(object, speed) -> float:

    # Check for ball or paddle
    try:
        match object:

            # If setting the speed of a ball, use these constraints
            case 0:
                if speed < 6 or speed > 15:
                    speed = 12

            # If setting the speed of a paddle, use these constraints
            case _:
                if speed < 12 or speed > 25:
                    speed = 18

    # If speed is not a number, exit program
    except TypeError:
        sys.exit("Speed must be a number.")

    # If we've reached this far, return tuple
    return float(speed)


if __name__ == "__main__":
    main()
