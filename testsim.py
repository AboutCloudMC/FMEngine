import FMEngine as fm

fm.screen = fm.graphics.init(800, 600, "Simulation Test")
fm.loop = fm.graphics.GameLoop(fm.screen)
fm.loop.run()

cube = fm.physics.Entity("1", 10, 10, 20)
cube.actForce((100, 100), 200)

cube.setInstructions([
    lambda: fm.graphics.Draw(fm.screen).drawRect((50, 50, 50, 50), 3, fm.graphics.Color.WHITE)
])
cube.registerDrawable()

fm.graphics.pygame.draw.line(fm.screen, (255, 255, 255), (200, 200), (400, 400), 2)



