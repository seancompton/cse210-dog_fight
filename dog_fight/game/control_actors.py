from game.action import Action
from game import constants

class ConstrolActorsActoin(Action):
    def __init__(self, input_service) -> None:
        super().__init__()
        self._input_service = input_service

    def execute(self, cast):
        # TODO come up with some code that will update the posistion and will
        #shoot somthinng for the airplanes.
        pass