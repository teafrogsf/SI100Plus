import threading
import time

msg = 0

def long_running_task():
    print("Starting long-running task...")
    for i in range(20):
        global msg
        msg = i
        time.sleep(0.5)  # 模拟耗时操作
    print("Long-running task finished.")

def main_loop():
    for i in range(5):
        print(f"Main loop iteration: {i}")
        global msg
        print(msg)
        time.sleep(1)  # 模拟主循环中的其他操作

if __name__ == "__main__":
    # 创建并启动后台线程执行耗时操作
    thread = threading.Thread(target=long_running_task, daemon=True)
    thread.start()

    # 主循环继续执行，不会被耗时操作阻塞
    main_loop()

    # 主线程结束前可以选择等待后台线程完成
    thread.join()
    print("Main thread finished.")
