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
    
class Color:

    WHITE = (255, 255, 255)

class GameLoop:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.run()

    def run(self):
        self.running = True
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   self.running = False  # Exit the loop if the window is closed

            # Update the display
            pygame.display.flip()


    