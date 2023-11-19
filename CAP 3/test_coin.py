import pygame
import pytest
from coin import*  

@pytest.fixture
def window():
    pygame.init()
    window_width = 350
    window_height = 400
    window = pygame.display.set_mode((window_width, window_height)) # Assuming you have a Game class in your script
    yield window
    pygame.quit()

#@pytest.fixture
#def game():
    #return window()

def test_movement_left(window):
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT}))
    tiger_initial_x = window_width / 2
    tiger_speed = 3

    coin_initial_x = window_width / 2
    coin_initial_y = window_height - 30

    # Set initial positions
    tiger_x = tiger_initial_x
    coin_x = coin_initial_x
    coin_y = coin_initial_y

def test_movement_right(window):
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT}))
    tiger_initial_x = window_width / 2
    tiger_speed = 3

    coin_initial_x = window_width / 2
    coin_initial_y = window_height - 30

    # Set initial positions
    tiger_x = tiger_initial_x
    coin_x = coin_initial_x
    coin_y = coin_initial_y


def test_coin_collection(window):
     # Assuming 'tiger_y' is an attribute of your Game class
    initial_tiger_y = window.tiger_y
    window.coin_y = initial_tiger_y
    window.update_game()

    # Your assertions based on the expected behavior
    assert window.game_instance.score == initial_tiger_y + 1
   
def test_obstacle_collision(window):
    window.obstacle_x = window.tiger_x  # Position the obstacle at the tiger's location
    window.update_game()
    assert window.game_over


def test_window_boundaries(game):
# Set the tiger's x-coordinate to a value beyond the left boundary
    game.tiger_x = -1

    # Call the function or perform actions that check boundaries in your game logic
    game.check_boundaries()  # Adjust this line based on your game logic

    # Assert that the tiger's x-coordinate is within the expected boundaries
    assert 0 <= game.tiger_x <= window_width, "Test Failed: Tiger x-coordinate is not within boundaries."
    

def test_score_display(game):
    game.coin_y = game.tiger_y  # Position the coin at the tiger's location
    game.update_game()
    assert "Score: 1" in game.get_score_text()


def test_game_over_display(game):
    game.obstacle_x = game.tiger_x  # Position the obstacle at the tiger's location
    game.update_game()
    assert "Game Over" in game.get_game_over_text()


def test_music_playback(music_player):
    music_player.load_music('MICHAEL-LENStake-me-to-your-heart.mp3')
    music_player.play()
    pygame.time.wait(1000)  # Wait for a short time to allow playback
    assert music_player.is_playing()
    music_player.stop()  # Stop the music after the test


def test_window_close():
    # This test might require a different approach depending on how your game handles window close events
    pass
