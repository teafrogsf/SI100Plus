from solve import \
    turn_left, turn_right, move_forward, try_exit, check_front, BlockType, main

if __name__ == "__main__":
    main()

####################### DO NOT MODIFY ABOVE THIS LINE ##########################

def operation():
    # Your code here.
    while True:
        turn_right()
        if check_front() == BlockType.GROUND:
            move_forward()
            try_exit()
            continue
        turn_left()
        if check_front() == BlockType.GROUND:
            move_forward()
            try_exit()
            continue
        turn_left()
    