"""
Some common functions.
"""
from pathlib import Path

import __init_root__


def add(x, y):
    return x + y


def get_root_dir():
    return Path(__init_root__.__file__).parent.absolute()


def get_data_dir() -> Path:
    """
    获取数据目录
    :return:  数据目录
    """
    return Path(get_root_dir(), "data")
