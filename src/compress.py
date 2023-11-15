"""
该脚本将搜索给*.log定目录中的所有文件，使用您指定的程序压缩它们，然后给它们加上日期标记。
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
    default="log",
)
args = parser.parse_args()
suffix = args.suffix

path = args.path
compress_name = str(Path(path) / suffix)
compress = args.compress

with tempfile.TemporaryDirectory() as tmpdir:
    pprint(tmpdir)
    for f in Path(path).rglob(f"*.{suffix}"):
        pprint(f)
        shutil.move(f, f"{tmpdir}/{f.name}")
    if compress == "gzip":
        shutil.make_archive(compress_name, "gztar", root_dir=tmpdir)
    elif compress == "bzip2":
        shutil.make_archive(compress_name, "bztar", root_dir=tmpdir)
    elif compress == "zip":
        shutil.make_archive(compress_name, "zip", root_dir=tmpdir)
