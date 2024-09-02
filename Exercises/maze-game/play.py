from maze import GameManager

manager = GameManager()

while True:
    manager.update()
    manager.draw()
    manager.clock.tick(30)