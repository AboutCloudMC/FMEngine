import pygame

def init(width: int, height: int, title: str):
    # Initialize Pygame
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((width, height))  # Create the window
    pygame.display.set_caption(title)  # Set the window title
    
    return screen




    