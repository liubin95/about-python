"""
Click 是一个 Python 包，用于以可组合的方式使用尽可能少的代码创建漂亮的命令行界面。
它是“命令行界面创建工具包”。它具有高度可配置性，但具有开箱即用的合理默认值。

它的目的是使编写命令行工具的过程变得快速而有趣，同时还防止因无法实现预期的 CLI API 而造成的任何挫败感。

点击三点：

命令的任意嵌套

自动生成帮助页面

支持运行时延迟加载子命令
"""
import shutil
from pathlib import Path
from pprint import pprint

import click


def validate_path(ctx, param, value):
    pprint(f"{ctx!r}")
    if not Path(value).exists():
        raise click.BadParameter("path not exists")

    if not Path(value).is_dir():
        raise click.BadParameter("path is not dir")

    return value


@click.group()
@click.option(
    "-p",
    "path",
    required=True,
    type=Path,
    help="path to deal",
    callback=validate_path,
)
@click.pass_context
def file(ctx, path):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj["path"] = path


@file.command()
@click.pass_context
@click.option("-f", "files", multiple=True, required=True, help="file name to deal")
def find(ctx, files):
    path = Path(ctx.obj["path"])

    for it in files:
        find_file = path.rglob(it)
        for f in find_file:
            click.secho(f, fg="green")


@file.command()
@click.pass_context
def ls(ctx):
    path = ctx.obj["path"]
    for it in sorted(Path(path).glob("*"), key=lambda x: x.name.lower()):
        if it.is_file():
            click.secho(it.name, fg="green")
        else:
            click.secho(it.name, fg="blue")


@file.command()
@click.pass_context
@click.option("-c", "--count", type=int, default=1, help="number of greetings")
@click.option("-f", "files", multiple=True, required=True, help="file name to deal")
def copy(ctx, count, files):
    path = Path(ctx.obj["path"])

    for it in files:
        find_file = path.rglob(it)
        for f in find_file:
            click.echo(f)
            if click.confirm("Do you want to continue?"):
                for i in range(count):
                    shutil.copy2(f, f.parent / f"{f.stem}-{i}{f.suffix}")
                click.secho("Copied", fg="green")
            else:
                click.secho("Aborted!", fg="red")


@file.command()
@click.pass_context
@click.option("-f", "files", multiple=True, required=True, help="file name to deal")
def rm(ctx, files):
    path = Path(ctx.obj["path"])
    for it in files:
        find_file = path.rglob(it)
        for f in find_file:
            click.echo(f)
            if click.confirm("Do you want to continue?"):
                f.unlink()
                click.secho("Deleted", fg="green")
            else:
                click.secho("Aborted!", fg="red")


if __name__ == "__main__":
    file(obj={})
