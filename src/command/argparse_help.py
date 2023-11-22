"""
argparse 模块可以让人轻松编写用户友好的命令行接口。
程序定义它需要的参数，然后 argparse 将弄清如何从 sys.argv 解析出那些参数。
argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。

使用click替代
"""
import argparse
import pathlib
from pprint import pprint

_parser = argparse.ArgumentParser(description="deal some files")

# nargs 参数
# N （一个整数）。命令行中的 N 个参数会被聚集到一个列表中。 多少都会报错
# * （一个星号）。所有的命令行参数都会被聚集到一个列表中。 如果没有命令行参数，会创建一个空列表。
# + （加号）。和 * 类似，但是要求至少有一个命令行参数。
_parser.add_argument(
    "-f",
    metavar="vim.pdf demo.log",
    help="name of file to deal",
    nargs="+",
    required=True,
)

_parser.add_argument("-p", type=pathlib.Path)
_subparsers = _parser.add_subparsers()

_parser_find = _subparsers.add_parser("find", help="find file")


def remove(_args):
    pprint("remove")
    pprint(_args)


_parser_rm = _subparsers.add_parser("rm", help="remove file")
# choices 参数
_parser_rm.add_argument(
    "--way",
    choices=["回收", "delete"],
    default="delete",
    help="the way to remove file",
)
_parser_rm.set_defaults(func=remove)

_parser_copy = _subparsers.add_parser("copy", help="copy file")
# type 参数
_parser_copy.add_argument("-n", "--num", type=int, help="copy times", default=2)

args = _parser.parse_args()
args_rm = _parser_rm.parse_args()
args_copy = _parser_copy.parse_args()
args.func(args)
args_rm.func(args_rm)
