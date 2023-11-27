"""
about pid file
"""
import atexit
import os
import signal
import time

pid_file_path: str = "your_project.pid"  # 替换为你期望的 PID 文件路径


def write_pid_file():
    pid = os.getpid()
    with open(pid_file_path, "w", encoding="utf-8") as pid_file:
        pid_file.write(str(pid))


def remove_pid_file(sig_id, frame):
    sig = {x.value: x for x in signal.valid_signals()}.get(sig_id)
    print(f"remove_pid_file {sig.name}, {sig_id=}, {frame=}")
    if os.path.exists(pid_file_path):
        os.remove(pid_file_path)
        print(f"PID file removed: {pid_file_path}")
    exit(0)


def remove_pid_file_at_exit():
    print("remove_pid_file_at_exit")
    if os.path.exists(pid_file_path):
        os.remove(pid_file_path)
        print(f"PID file removed: {pid_file_path}")


if __name__ == "__main__":
    try:
        write_pid_file()
        print(f"PID file created: {pid_file_path}")

        # 注册退出时执行的函数
        atexit.register(remove_pid_file_at_exit)

        # 注册信号处理函数
        signal.signal(signal.SIGTERM, remove_pid_file)
        signal.signal(signal.SIGINT, remove_pid_file)
        signal.signal(signal.SIGKILL, remove_pid_file)
        # 你的程序逻辑可以放在这里

        time.sleep(60)

    except Exception as e:
        print(f"Error creating PID file: {e}")
