import PhysicsComponent as physics
import GraphicsComponent as graphics


screen: graphics.pygame.Surface = None
loop: graphics.GameLoop = None

def start():
    loop.running = True

def stop():
    loop.running = False