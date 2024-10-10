
class Entity:

    def __init__(self, id, width, height, mass):
        self.id = id
        self.width = width
        self.height = height
        self.mass = mass
    
    def actForce(self, vector, magnitude):
        print(f"Acting Force on {self.id} from {vector[0]} | {vector[1]} with a magnitude of {magnitude}.")


        