import pygame, sys, threading, queue, ctypes
from maze.manager import GameManager
from maze.statics import BlockType, GameMode
from solve import command_queue, result_queue

# time limit (frames)
time_limit = 120 * 25

def terminate_thread(thread):
    if not thread.is_alive():
        return
    
    thread_id = ctypes.c_long(thread.ident)
    
    if hasattr(ctypes.pythonapi, 'PyThreadState_SetAsyncExc'):
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if res == 0:
            raise ValueError("Invalid thread ID")
        elif res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    else:
        res = ctypes.pythonapi.pthread_kill(thread_id, ctypes.c_int(9))
        if res != 0:
            raise ValueError("Error terminating thread")

def main():
    from logic import operation
    
    def fail(index: int):
        print(f"Test Case {index} Failed")
        print(f"Score: {score}/5")
        print(manager.maze)
        print(repr(manager.maze))
        pygame.quit()
        sys.exit()
    
    manager = GameManager(GameMode.CHECK)
    
    score = 0
    
    for i in range(1, 6):
        running_time = 0
        manager.generate_test_case()
        manager.draw()
        pygame.display.flip()
        
        command_queue.queue.clear()
        result_queue.queue.clear()
        
        solve_thread = threading.Thread(target=operation)
        solve_thread.daemon = True
        solve_thread.start()
        
        process_command_count = 0
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
                        terminate_thread(solve_thread)
                        manager.end_game(f"Test Case {i} Passed")
                        score += 1
                process_command_count += 1
                if process_command_count > 30:
                    break
            if not solve_thread.is_alive():
                if manager.ended:
                    break
                else:
                    fail(i)
            manager.clock.tick(120)
            running_time += 1
            if running_time > time_limit:
                fail(i)
                
    print(f"Score: 5/5")

if __name__ == "__main__":
    main()