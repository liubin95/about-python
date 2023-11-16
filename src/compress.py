"""
该脚本将搜索给*.suffix定目录中的所有文件，使用您指定的程序压缩它们.
"""

import argparse
import shutil
import tempfile
from pathlib import Path
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument(
    "-p",
    "--path",
    help="the path of the log file",
    default="/Users/liubin/code",
)
parser.add_argument(
    "-c",
    "--compress",
    help="the compress of the log file",
    default="gzip",
    choices=["gzip", "bzip2", "zip"],
)

parser.add_argument(
    "-s",
    "--suffix",
    help="the suffix of the file",
    default="log",
)
args = parser.parse_args()
suffix = args.suffix

path = args.path
compress_name = str(Path(path) / suffix)
compress = args.compress

# 创建临时目录
with tempfile.TemporaryDirectory() as tmpdir:
    pprint(tmpdir)
    # 移动文件
    for f in Path(path).rglob(f"*.{suffix}"):
        pprint(f)
        shutil.move(f, f"{tmpdir}/{f.name}")
    # 压缩文件
    if compress == "gzip":
        shutil.make_archive(compress_name, "gztar", root_dir=tmpdir)
    elif compress == "bzip2":
        shutil.make_archive(compress_name, "bztar", root_dir=tmpdir)
    elif compress == "zip":
        shutil.make_archive(compress_name, "zip", root_dir=tmpdir)
