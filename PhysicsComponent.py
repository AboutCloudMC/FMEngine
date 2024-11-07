import FMEngine as fm

class Entity:

    def __init__(self, id, width, height, mass):
        self.id = id
        self.width = width
        self.height = height
        self.mass = mass
        self.drawer = fm.graphics.Draw(fm.screen)
    
    def actForce(self, vector, magnitude):
        print(f"Acting Force on {self.id} from {vector[0]} | {vector[1]} with a magnitude of {magnitude}.")

    def draw(self, pos, color):
        self.drawer.drawRect(pos, self.width, color)

        