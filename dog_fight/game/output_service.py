import sys
from game import constants
import pyray

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        None
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
        """
        self._textures = {}

    def open_window(self, title):
        """
        Opens a new window with the provided title.
        """
        pyray.init_window(constants.MAX_X, constants.MAX_Y, title)
        pyray.set_target_fps(constants.FRAME_RATE)
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

    def draw_box(self, x, y, width, height):
        """
        Draws at rectangular box with the provided specifications.
        """
        pyray.draw_rectangle(x, y, width, height, pyray.BLUE)

    def draw_text(self, x, y, text, is_dark_text):
        """
        Outputs the provided text at the desired location.
        """
        color = pyray.WHITE

        if is_dark_text:
            color = pyray.BLACK

        pyray.draw_text(text, x + 5, y + 5, constants.DEFAULT_FONT_SIZE, color)

    def draw_image(self, x, y, image):
        """
        Outputs the provided image on the screen.
        """
        if image not in self._textures.keys():

            loaded = pyray.load_texture(image)
            self._textures[image] = loaded

        texture = self._textures[image]
        pyray.draw_texture(texture, x, y, pyray.WHITE)

    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (Actor): The actor to render.
        """ 
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        width = actor.get_width()
        height = actor.get_height()

        if actor.has_image():
            image = actor.get_image()
            self.draw_image(x, y, image)
            #self.draw_image(x - width / 2, y - height / 2, image)
        elif actor.has_text():
            text = actor.get_text()
            self.draw_text(x, y, text, False)
        elif width > 0 and height > 0:
            self.draw_box(x, y, width, height)
        
    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        pyray.end_drawing()