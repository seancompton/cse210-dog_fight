from game.action import Action

class DisplayScore(Action):

    def __init__(self, output_services) -> None:
        super().__init__()
        self._output_services = output_services

    def execute(self, cast):
        airplanes = cast["airplanes"]

        for airplane in airplanes:
            position = airplane.get_text_position()
            x = position.get_x()
            y = position.get_y()
            score = str(airplane.get_hit_points())
            self._output_services.draw_text(x, y, score, False)