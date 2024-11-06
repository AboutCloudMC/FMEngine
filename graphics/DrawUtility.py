import pygame

class DrawUtility:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def drawLine(self, start, end, color, width):
        pygame.draw.line(self.screen, color, start, end, width)

    def drawRect(self, pos, width, color):
        pygame.draw.rect(self.screen, color, pos, width)

class ColorConstants:
    WHITE = (255, 255, 255)