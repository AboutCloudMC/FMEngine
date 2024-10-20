import pygame

def init(width: int, height: int, title: str):
    # Initialize Pygame
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((width, height))  # Create the window
    pygame.display.set_caption(title)  # Set the window title
    
    return screen

class Draw:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def drawLine(self, start, end, color, width):
        pygame.draw.line(self.screen, color, start, end, width)

    def drawRect(self, pos, width, color):
        pygame.draw.rect(self.screen, color, pos, width)

class DrawableObject:
    def __init__(self, instructions):
        self.instructions = instructions

    def draw(self):
        for instruction in self.instructions:
            instruction()
    
class Color:

    WHITE = (255, 255, 255)

class GameLoop:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.run()
        self.objects = dict()

    def run(self):
        pygame.time.Clock()
        self.running = True
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   self.running = False  # Exit the loop if the window is closed
            #pygame.display.update()
            for object in self.objects.values():
                object.draw()
            # Update the display
            pygame.display.flip()


    