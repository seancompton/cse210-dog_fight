import sys
from game.point import Point
import pyray

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._d_key_status = True
        self._left_key_status = True
        
    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if self.is_left_pressed():
            dx = -1
        
        if self.is_d_pressed():
            dx = 1        
        
        if self.is_up_pressed():
            dy = -1
        
        if self.is_down_pressed():
            dy = 1

        if self.is_w_pressed():
            dy = -2

        if self.is_s_pressed():
            dy = 2
            

        direction = Point(dx, dy)
        return direction

    def is_left_pressed(self):
        return pyray.is_key_down(pyray.KEY_LEFT)
    
    def is_left_not_pressed(self):
        return pyray.is_key_up(pyray.KEY_LEFT)

    def is_right_pressed(self):
        return pyray.is_key_down(pyray.KEY_RIGHT)

    def is_up_pressed(self):
        return pyray.is_key_down(pyray.KEY_UP)

    def is_up_not_pressed(self):
        return pyray.is_key_up(pyray.KEY_UP)

    def is_down_pressed(self):
        return pyray.is_key_down(pyray.KEY_DOWN)
    
    def is_down_not_pressed(self):
        return pyray.is_key_up(pyray.KEY_DOWN)

    def is_w_pressed(self):
        return pyray.is_key_down(pyray.KEY_W)
    
    def is_w_not_pressed(self):
        return pyray.is_key_up(pyray.KEY_W)

    def is_s_pressed(self):
        return pyray.is_key_down(pyray.KEY_S)

    def is_s_not_pressed(self):
        return pyray.is_key_up(pyray.KEY_S)

    def is_s_not_pressed(self):
        return pyray.is_key_up(pyray.KEY_S)

    def is_d_pressed(self):
        return pyray.is_key_down(pyray.KEY_D)

    def is_d_not_pressed(self):
        return pyray.is_key_up(pyray.KEY_D)
        
    def window_should_close(self):
        return pyray.window_should_close()
    
    def set_d_key_status(self, status):
        self._d_key_status = status

    def set_left_key_status(self, status):
        self._left_key_status = status

    def return_d_key_status(self):
        return self._d_key_status

    def return_left_key_status(self):
        return self._left_key_status
