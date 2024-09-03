import pygame, sys
from maze.manager import GameManager
from maze.statics import BlockType
import threading, time
import bdb, cmd, linecache

manager = GameManager()

class MyDebugger(bdb.Bdb):
    def user_line(self, frame):
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        line = linecache.getline(filename, lineno).strip()
        if("logic.py" not in filename):
            self.set_step()
        else:
            print(f'Paused at {filename}:{lineno} - {line}')
            pygame.display.set_caption(f"Maze Game - Paused at {line}")
            manager.highlightCode(lineno)
            self.interaction(frame)

    def interaction(self, frame):
        self.frame = frame
        # DebuggerCLI(self).cmdloop()
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.set_next(debugger.frame)
                        flag = False
                        break
                    elif event.key == pygame.K_c:
                        self.set_continue()
                        flag = False
                        break

debugger = MyDebugger()
class DebuggerCLI(cmd.Cmd):
    prompt = '(maze-debugger) '

    def __init__(self, debugger: MyDebugger):
        super().__init__()
        self.debugger = debugger

    def do_continue(self, arg):
        'Continue execution'
        self.debugger.set_continue()
        return True  # Exits the cmdloop

    def do_step(self, arg):
        'Step to the next line (Setp into)'
        self.debugger.set_step()
        return True

    def do_quit(self, arg):
        'Quit the debugger'
        self.debugger.set_quit()
        return True

    def do_next(self, arg):
        'Step to the next line (Step over)'
        self.debugger.set_next(self.debugger.frame)
        return True

    def default(self, line):
        print(f'Unknown command: {line}')

def turn_left():
    manager.turn_left()
    manager.update()
    manager.turn_draw()
    # pygame.display.flip()

def turn_right():
    manager.turn_right()
    manager.update()
    manager.turn_draw()
    # pygame.display.flip()

def move_forward():
    manager.try_move()
    manager.update()
    manager.move_draw()
    # pygame.display.flip()

def try_exit():
    if(manager.try_exit()):
        print("WIN")
        time.sleep(1)
        sys.exit()

def check_front():
    return manager.check_front()


def _operation():
    from logic import operation
    debugger.run('operation()', globals=globals(), locals=locals())

def main():
    # Initial Draw
    manager.draw()
    pygame.display.flip()
    thread = threading.Thread(target=_operation)
    thread.start()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        manager.clock.tick(60)
        if thread.is_alive():
            pygame.display.flip()
        else:
            break

if __name__ == "__main__":
    print("Run this file in logic.py")