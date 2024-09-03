from solve import \
    turn_left, turn_right, move_forward, try_exit, check_front, BlockType, main
import time

if __name__ == "__main__":
    main()

def operation():
####################### DO NOT MODIFY ABOVE THIS LINE ##########################
    # Your code here.
    while True:
        turn_left()
        while(check_front() == BlockType.WALL):
            turn_right()
        move_forward()
        try_exit()
        time.sleep(0.01)