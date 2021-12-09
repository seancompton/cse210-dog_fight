from game.actor import Actor

class Bullet(Actor):

    def __init__(self):
        super().__init__()
        self._whos_bullet = None

    def set_whos_bullet(self, shot):
        self._whos_bullet = shot

    def return_whos_bullet(self):
        return self._whos_bullet

    