import FMEngine as fm
from physics import Entity, Vector
from graphics import GameLoop, GraphicsComponent as g, DrawUtility
import pygame

class Cube(Entity):
    def __init__(self, id: str, position: Vector, side: int, mass: int):
        super().__init__(id, side, side, mass, fm.screen)
        self.drawer = fm.graphics.DrawUtility(fm.screen)
    
    def actForce(self, vector, magnitude):
        print(f"Acting Force on {self.id} from {vector[0]} | {vector[1]} with a magnitude of {magnitude}.")

    def draw(self, screen: pygame.Surface):
        DrawUtility(screen).drawRect(self.position, self.width, self.height, (255, 255, 255))


screen = g.init(800, 600, "Simulation Test")
loop = GameLoop(fm.screen)

cube = Cube("1", 10, 10, 20)
cube.actForce(Vector(10, 10))


