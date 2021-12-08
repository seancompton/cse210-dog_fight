from game import point
from game.action import Action
from game import constants
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

        if self._input_service.is_up_pressed():
            y = -1
            direction = Point(0, y)
            airplane = cast["airplanes"][1]
            airplane.set_velocity(direction.scale(constants.AIRPLANE_SPEED_RUSSIAN))

        if self._input_service.is_down_pressed():
            y = 1
            direction = Point(0, y)
            airplane = cast["airplanes"][1]
            airplane.set_velocity(direction.scale(constants.AIRPLANE_SPEED_RUSSIAN))

        if self._input_service.is_s_pressed():
            airplane = cast["airplanes"][0]
            y = 1
            direction = Point(0, y)
            airplane.set_velocity(direction.scale(constants.AIRPLANE_SPEED_AMERICAN))  

        if self._input_service.is_w_pressed():
            airplane = cast["airplanes"][0]
            y = -1
            direction = Point(0, y)
            airplane.set_velocity(direction.scale(constants.AIRPLANE_SPEED_AMERICAN))

        elif y != -2 and y != 2 and y != -1 and y != 1: 
            for airplane in cast["airplanes"]:
                velocity = Point(0, 0)
                airplane.set_velocity(velocity)

        if self._input_service.is_d_pressed():
            bullet = Bullet()
            airplane = cast["airplanes"][0]
            position = airplane.get_position()
            x = position.get_x()
            y = position.get_y()
            x = x + 100
            position = Point(x, y)

            if len(cast["bullets"]) != 0:
                last_bullet = cast["bullets"][-1]
                last_bullet_position = last_bullet.get_position()
                last_bullet_x = last_bullet_position.get_x()
                velocity = last_bullet.get_velocity()
                dx = velocity.get_x()
                print(f"{dx}-------------------")

                if last_bullet_x > x + constants.BULLET_SHOOTING_SPEED and dx: 
                    bullet.set_height(constants.BULLET_HEIGHT)
                    bullet.set_width(constants.BULLET_WIDTH)
                    bullet.set_position(position)
                    velocity = Point(constants.AMERICAN_BULLET_VELOCITY, 0)
                    bullet.set_velocity(velocity)
                    cast["bullets"].append(bullet)
                                
            else:
                bullet.set_position(position)
                velocity = Point(constants.AMERICAN_BULLET_VELOCITY, 0)
                bullet.set_velocity(velocity)
                cast["bullets"].append(bullet)

        if self._input_service.is_left_pressed():
            bullet = Bullet()
            airplane = cast["airplanes"][1]
            position = airplane.get_position()
            bullet.set_height(constants.BULLET_HEIGHT)
            bullet.set_width(constants.BULLET_WIDTH)
            x = position.get_x()
            y = position.get_y()
            position = Point(x - 100, y)

            if len(cast["bullets"]) != 0:
               
                last_bullet = cast["bullets"][-1]
                last_bullet_position = last_bullet.get_position()
                last_bullet_x = last_bullet_position.get_x()
                velocity = last_bullet.get_velocity()
                dx = velocity.get_x()
                print(f"{dx}-------------------******************")
                
                if last_bullet_x <  x - constants.BULLET_SHOOTING_SPEED: 
                    bullet.set_position(position)
                    velocity = Point(constants.RUSSIAN_BULLET_VELOCITY, 0)
                    bullet.set_velocity(velocity)
                    cast["bullets"].append(bullet)

            else:
                bullet.set_position(position)
                velocity = Point(constants.RUSSIAN_BULLET_VELOCITY, 0)
                bullet.set_velocity(velocity)
                cast["bullets"].append(bullet)