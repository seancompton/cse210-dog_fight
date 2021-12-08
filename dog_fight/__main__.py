import random
from game import constants
from game import control_actors
from game import move_actors_action
from game import handle_of_screen_action
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.airplane import Airplane
from game.bullet import Bullet
from game.cover import Cover
from game.display_score import DisplayScore

# TODO: Add imports similar to the following when you create these classes
# from game.airplane import Airplane
# from game.bullet import Bullet
# from game.obstacle import Obstacle
from game.control_actors import ConstrolActorsAction
from game.handle_collisions import HandleCollisions
from game.handle_of_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["airplanes"] = []
    # TODO: Creates two airplanes and saves them in a list also stores how many hits each airplane
    #gets hit with

    #Initially starting with american airplane
    airplane = Airplane()
    position = Point(constants.X_AMERICAN_LOCATION, constants.Y_AMERICAN_LOCATION)
    airplane.set_position(position)
    airplane.set_width(constants.AMERICAN_WIDTH)
    airplane.set_height(constants.AMERICAN_HEIGHT)
    airplane.set_image(constants.IMAGE_F16)
    velocity = Point(0, 0)
    airplane.set_velocity(velocity)
    score_location = Point(constants.X_AMERICAN_SCORE, constants.Y_AMERICAN_SCORE)
    airplane.set_score_position(score_location)
    cast["airplanes"].append(airplane)

    #creating the russian airplane
    airplane = Airplane()
    position = Point(constants.X_RUSSIAN_LOCATION, constants.Y_RUSSIAN_LOCATION)
    airplane.set_position(position)
    airplane.set_width(constants.RUSSIAN_WIDTH)
    airplane.set_height(constants.RUSSIAN_HEIGHT)
    airplane.set_image(constants.IMAGE_MIG)
    velocity = Point(0, 0)
    airplane.set_velocity(velocity)
    score_location = Point(constants.X_RUSSIAN_SCORE, constants.Y_RUSSIAN_SCORE)
    airplane.set_score_position(score_location)
    cast["airplanes"].append(airplane)

    cast["bullets"] = []
    # TODO: creates a place in memory to save the bullet as they get shot from the
    #airplanes


    cast["obstacles"] = []
    # TODO: Randomly generates 4 objects that have to be shot around in order to hit the other airplane

    for i in range(constants.NUMBER_OF_OBSTACLES):
        cover = Cover()
        cover.set_height(constants.OBSTACLE_HEIGHT)
        cover.set_width(constants.OBSTACLE_WIDTH)
        cover.set_image(constants.IMAGE_ASTROID)
        position = Point(random.randint(70, 700), random.randint(70, 500))
        cover.set_position(position)
        cast["obstacles"].append(cover)

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    control_actors = ConstrolActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_of_screen_action = HandleOffScreenAction()
    handle_collisions = HandleCollisions(physics_service)
    display_score = DisplayScore(output_service)

    draw_actors_action = DrawActorsAction(output_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors]
    script["update"] = [move_actors_action, handle_of_screen_action, handle_collisions]
    script["output"] = [draw_actors_action, display_score]

    # Start the game
    output_service.open_window("Dog Fight")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
