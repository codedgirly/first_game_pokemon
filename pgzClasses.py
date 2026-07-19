# Class imports to avoid the red underlines that are looking for the Type Hints
from pgzero.screen import Screen
from pgzero.keyboard import Keyboard
from pgzero.actor import Actor
from pygame import Rect
screen: Screen
keyboard: Keyboard
music: any

# Updates the window to be centered instead of in the bottom-right corner
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Coin Class
class Coin(Actor):
    def __init__(self, x, y):
        super().__init__("coin", (x, y))

