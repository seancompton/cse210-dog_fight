from game import point
from game.action import Action
from game import airplane, constants, input_service
from game.bullet import Bullet
from game.point import Point

class ConstrolActorsAction(Action):
    def __init__(self, input_service) -> None:
        super().__init__()
        self._input_service = input_service

    def execute(self, cast):
        # TODO come up with some code that will update the posistion and will
        #shoot somthinng for the airplanes.
        direction = self._input_service.get_direction()
        y = direction.get_y()
        x = direction.get_x()

        if y == -2 or y == 2:
            airplane = cast["airplanes"][0]
            direction = Point(0, y)
            airplane.set_velocity(direction.scale(constants.AIRPLANE_SPEED_AMERICAN))

        elif y == -1 or y == 1:
            direction = Point(0, y)
            airplane = cast["airplanes"][1]
            airplane.set_velocity(direction.scale(constants.AIRPLANE_SPEED_RUSSIAN))

        else: 
            for airplane in cast["airplanes"]:
                velocity = Point(0, 0)
                airplane.set_velocity(velocity)

        if x == -1:
            bullet = Bullet()
            airplane = cast["airplanes"][1]
            position = airplane.get_position()
            bullet.set_height(constants.BULLET_HEIGHT)
            bullet.set_width(constants.BULLET_WIDTH)
            x = position.get_x()
            y = position.get_y()
            position = Point(x - 100, y)
            bullet.set_position(position)
            velocity = Point(constants.RUSSIAN_BULLET_VELOCITY, 0)
            bullet.set_velocity(velocity)
            cast["bullets"].append(bullet)

        if x == 1:
            bullet = Bullet()
            airplane = cast["airplanes"][0]
            position = airplane.get_position()
            x = position.get_x()
            y = position.get_y()
            x = x + 100
            position = Point(x, y)
            bullet.set_height(constants.BULLET_HEIGHT)
            bullet.set_width(constants.BULLET_WIDTH)
            bullet.set_position(position)
            velocity = Point(constants.AMERICAN_BULLET_VELOCITY, 0)
            bullet.set_velocity(velocity)
            cast["bullets"].append(bullet)
                    
        