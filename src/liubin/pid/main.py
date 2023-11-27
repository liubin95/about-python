"""
about pid file
"""
import atexit
import os
import time


def write_pid_file(file_path):
    pid = os.getpid()
    with open(file_path, "w", encoding="utf-8") as pid_file:
        pid_file.write(str(pid))


def remove_pid_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"PID file removed: {file_path}")


if __name__ == "__main__":
    pid_file_path = "your_project.pid"  # 替换为你期望的 PID 文件路径

    try:
        write_pid_file(pid_file_path)
        print(f"PID file created: {pid_file_path}")

        # 注册退出时执行的函数
        atexit.register(remove_pid_file, pid_file_path)

        # 你的程序逻辑可以放在这里

        time.sleep(60)

    except Exception as e:
        print(f"Error creating PID file: {e}")
