import PhysicsComponent as physics
import GraphicsComponent as graphics


screen = None
loop = None

def init():
    screen = graphics.init(size[0], size[1], title)
    loop = graphics.GameLoop(screen)

def start():
    loop.running = True

def stop():
    loop.running = False