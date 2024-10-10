import FMEngine as fm

fm.size = (800, 600)
fm.title = "Simulation Test"
fm.init()
fm.loop.run()

cube = fm.physics.Entity("1", 10, 10, 20)
cube.actForce((3, 3), 2)