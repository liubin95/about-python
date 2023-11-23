from pathlib import Path

def add(x: int, y: int) -> int: ...

"""
:param x: The first number to add.
:param y: The second number to add.
:return The sum of x and y.
"""

def get_root_dir() -> Path: ...

"""
:return The root directory of the project.
"""

def get_data_dir() -> Path: ...

"""
:return The data directory of the project.
"""
