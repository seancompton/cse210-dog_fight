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
        covers = cast["obstacles"]
        x = 0
        remove_bullets = []

        for bullet in bullets:
            x = x + 1
            
            for airplane in airplanes:
                if self._physics_service.is_collision(airplane, bullet):
                    remove_bullets.append(x)
                    airplane.set_hit_points(1)                 

            for cover in covers:
                if self._physics_service.is_collision(bullet, cover):
                    remove_bullets.append(x)
        try:            
            for i in remove_bullets:
                bullets.pop(i-1)

        except:
            pass