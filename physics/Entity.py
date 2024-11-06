from graphics import GameLoop, DrawUtility
from physics import Vector
import pygame

class Entity:

    def __init__(self, id: str, position: Vector, size: Vector, mass: int):
        self.id: str = id
        self.position: Vector = position
        self.size: Vector = size
        self.mass: int = mass
    
    def actForce(self, vector: Vector):
        print(f"Acting Force on {self.id} from {vector[0]} | {vector[1]} with a magnitude of {vector.magnitude()}.")

    def draw(self, screen: pygame.Surface):
        raise NotImplementedError("This method must be implemented by the subclass.")