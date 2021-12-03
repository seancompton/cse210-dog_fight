from game.point import Point
from game.action import Action

class HandleOffScreenAction(Action):

    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        i = 0
        for bullet in cast["bullets"]:
            position = bullet.get_position()
            x = position.get_x()
            print(x)
            
            
            if x == 0 or x == 800:
                cast["bullets"].pop(i)
                
            i = i + 1