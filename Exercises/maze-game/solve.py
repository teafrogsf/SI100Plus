import pygame, sys, threading, queue
from maze.manager import GameManager
from maze.statics import BlockType
import threading, time
import bdb, cmd, linecache

manager = GameManager()
command_queue = queue.Queue()
result_queue = queue.Queue()

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
    command_queue.put("TURN_LEFT")

def turn_right():
    command_queue.put("TURN_RIGHT")

def move_forward():
    command_queue.put("MOVE_FORWARD")

def try_exit():
    command_queue.put("TRY_EXIT")

def check_front():
    command_queue.put("CHECK_FRONT")
    result = result_queue.get()
    return result


def _operation():
    from logic import operation
    debugger.run('operation()', globals=globals(), locals=locals())


def main():
    from logic import operation
    # Initial Draw
    manager.draw()
    pygame.display.flip()
    thread = threading.Thread(target=_operation)
    thread.daemon = True
    thread.start()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        while not command_queue.empty():
            command = command_queue.get()
            if command == "CHECK_FRONT":
                result_queue.put(manager.check_front())
            elif command == "TURN_LEFT":
                manager.turn_left()
                manager.update()
                manager.turn_draw()
                pygame.display.flip()
            elif command == "TURN_RIGHT":
                manager.turn_right()
                manager.update()
                manager.turn_draw()
                pygame.display.flip()
            elif command == "MOVE_FORWARD":
                manager.try_move()
                manager.update()
                manager.move_draw()
                pygame.display.flip()
            elif command == "TRY_EXIT":
                if manager.try_exit():
                    print("WIN")
                    pygame.quit()
                    sys.exit()
        manager.update()
        pygame.display.flip()
        manager.clock.tick(30)
        if not thread.is_alive():
            print("Operation finished without reaching the exit.")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    print("Run this file in logic.py")