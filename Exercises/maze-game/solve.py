import pygame, sys, threading, queue
from maze.manager import GameManager
from maze.statics import GameMode, BlockType
import threading
import bdb, linecache

command_queue = queue.Queue()
result_queue = queue.Queue()
event_list = None
event_key = None

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

def main():
    manager = GameManager(GameMode.DEBUG)

    class MyDebugger(bdb.Bdb):
        def user_line(self, frame):
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            line = linecache.getline(filename, lineno).strip()
            if("logic.py" not in filename):
                self.set_step()
            else:
                manager.highlightCode(lineno)
                print(f'Paused at {filename}:{lineno} - {line}')
                self.interaction(frame)

        def interaction(self, frame):
            self.frame = frame
            flag = True
            global event_key
            while flag:
                if event_key == pygame.K_n:
                    self.set_next(debugger.frame)
                    print("SETED NEXT")
                    flag = False
                    break
                elif event_key == pygame.K_c:
                    self.set_continue()
                    flag = False
                    break
                elif event_key == pygame.K_q:
                    self.set_quit()
                    flag = False
                    break
            event_key = None

    debugger = MyDebugger()

    def _operation():
        from logic import operation
        debugger.run('operation()', globals=globals(), locals=locals())

    # from logic import operation
    # Initial Draw
    manager.draw()
    pygame.display.flip()
    thread = threading.Thread(target=_operation)
    thread.daemon = True
    event_list = pygame.event.get()
    
    thread.start()
    
    while True:
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                global event_key
                event_key = event.key
        process_command_count = 0
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
                    manager.end_game("WIN")
            process_command_count += 1
            if process_command_count > 30:
                break
        manager.update()
        pygame.display.flip()
        manager.clock.tick(30)
        if not thread.is_alive() and not manager.ended:
            print("Operation finished without reaching the exit.")
            pygame.quit()
            sys.exit()
        event_list = pygame.event.get()

if __name__ == "__main__":
    print("Run this file in logic.py")