import FMEngine as fm

fm.screen = fm.graphics.init(800, 600, "Simulation Test")
fm.loop = fm.graphics.GameLoop(fm.screen)

cube = fm.physics.Entity("1", 10, 10, 20)
cube.actForce((100, 100), 200)
cube.draw((300, 300, 300, 300), fm.graphics.Color.WHITE)

