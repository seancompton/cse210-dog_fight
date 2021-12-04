from game.actor import Actor

class Airplane(Actor):

    def __init__(self):
        super().__init__()
        self._hit_points = 0
        self._score_position = None

    def get_hit_points(self):
        return self._hit_points

    def set_hit_points(self, hit):
        self._hit_points = hit + self._hit_points

    def get_text_position(self):
        return self._score_position

    def set_score_position(self, position):
        self._score_position = position
