from solve import \
    turn_left, turn_right, move_forward, try_exit, check_front, BlockType, main

if __name__ == "__main__":
    main()

####################### DO NOT MODIFY ABOVE THIS LINE ##########################

def operation():
    # Your code here.
    turn_left()
    while(check_front() == BlockType.WALL):
        turn_right()
    move_forward()
    try_exit()