import pygame

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