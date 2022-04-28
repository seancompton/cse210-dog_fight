from game.actor import Actor

class Score(Actor):
    def __init__(self):
        super().__init__()
        self._hit_points = 0
        
    def get_hit_points(self):
        return self._hit_points

    def set_hit_points(self, hit):
        self._hit_points = self._hit_points + hit