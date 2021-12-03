from os import remove
from game.action import Action

class HandleCollisions(Action):

    def __init__(self, physics_service) -> None:
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        # Todo: come up with some code that updates stuff if their is a collision.
        bullets = cast["bullets"]
        airplanes = cast["airplanes"]
        x = 0
        remove_bullets = []
        for airplane in airplanes:

            for bullet in bullets:
                print(bullet)
                
                if self._physics_service.is_collision(bullet, airplane):
                    remove_bullets.append(x)
                    print("number has been added.")

        print(remove_bullets)
        if len(remove_bullets) != 0:
            for i in remove_bullets:
                bullets.pop(i-1)

            