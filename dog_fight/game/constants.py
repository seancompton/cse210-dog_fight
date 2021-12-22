import os

from game.bullet import Bullet

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 60

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_F16 = os.path.join(os.getcwd(), "./dog_fight/assets/f_16.png")
IMAGE_MIG = os.path.join(os.getcwd(), "./dog_fight/assets/mig.png")
IMAGE_ASTROID = os.path.join(os.getcwd(), "./dog_fight/assets/asteroid.png")

SOUND_START = os.path.join(os.getcwd(), "./dog_fight/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./dog_fight/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./dog_fight/assets/over.wav")

AIRPLANE_SPEED_AMERICAN = 5
AIRPLANE_SPEED_RUSSIAN = 5

RUSSIAN_WIDTH = 30
RUSSIAN_HEIGHT = 30
X_RUSSIAN_LOCATION = 770
Y_RUSSIAN_LOCATION = 300
RUSSIAN_BULLET_VELOCITY = -10
X_RUSSIAN_SCORE = 750
Y_RUSSIAN_SCORE = 20

AMERICAN_WIDTH = 30
AMERICAN_HEIGHT = 30
X_AMERICAN_LOCATION = 0
Y_AMERICAN_LOCATION = 300
AMERICAN_BULLET_VELOCITY = 10
X_AMERICAN_SCORE = 20
Y_AMERICAN_SCORE = 20

BULLET_WIDTH = 50
BULLET_HEIGHT = 10
BULLET_SHOOTING_SPEED = 200
BULLET_OFFSET = 35

OBSTACLE_WIDTH = 35
OBSTACLE_HEIGHT = 35
NUMBER_OF_OBSTACLES = 10