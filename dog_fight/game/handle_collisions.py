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
        scores = cast["scores"]
        x = 0
        remove_bullets = []

        for bullet in bullets:
            x = x + 1
            length = len(airplanes)
            for i in range(length):
                if self._physics_service.is_collision(airplanes[i], bullet):
                    remove_bullets.append(x)
                    scores[i].set_hit_points(1)
                    scores[i].set_text(str(scores[i].get_hit_points()))


            for cover in covers:
                if self._physics_service.is_collision(bullet, cover):
                    remove_bullets.append(x)
        try:            
            for i in remove_bullets:
                bullets.pop(i-1)

        except:
            pass