import pygame

def init(width, height, title):
    # Initialize Pygame
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((width, height))  # Create the window
    pygame.display.set_caption(title)  # Set the window title
    
    return screen

class GameLoop:

    def __init__(self, screen):
        self.screen = screen
        self.run()

    def run(self):
        self.running = True
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   self.running = False  # Exit the loop if the window is closed

            # Fill the screen with a color
            self.screen.fill((255, 255, 255))  # Fill the screen with white color

            # Update the display
            pygame.display.flip()

    