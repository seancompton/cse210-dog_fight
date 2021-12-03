import os

from game.bullet import Bullet


MAX_X = 800
MAX_Y = 600
FRAME_RATE = 60

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BRICK = os.path.join(os.getcwd(), "./batter/assets/brick-3.png")
IMAGE_PADDLE = os.path.join(os.getcwd(), "./batter/assets/bat.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./batter/assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

AIRPLANE_SPEED_AMERICAN = 5
AIRPLANE_SPEED_RUSSIAN = 10

RUSSIAN_WIDTH = 50
RUSSIAN_HEIGHT = 50
X_RUSSIAN_LOCATION = 750
Y_RUSSIAN_LOCATION = 300
RUSSIAN_BULLET_VELOCITY = -10

AMERICAN_WIDTH = 50
AMERICAN_HEIGHT = 50
X_AMERICAN_LOCATION = 0
Y_AMERICAN_LOCATION = 300
AMERICAN_BULLET_VELOCITY = 10

KEY_UP = 265
KEY_DOWN = 264
KEY_LEFT = 263
KEY_W = 87
KEY_S = 83
KEY_D = 68

BULLET_WIDTH = 50
BULLET_HEIGHT = 10


