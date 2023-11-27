"""
    1. 遍历指定文件夹
    2. 判断是否为git仓库
    3. 调用git log,输出格式为json
    4. 过滤掉Merge
    5. 输出到alfred
"""

import json
import os
import subprocess
import sys
from datetime import timedelta, date, datetime

date_arr = []

if len(sys.argv) > 1:
    date_arr.append(datetime.strptime(sys.argv[1], "%Y-%m-%d").date())
else:
    # 今天的日期
    today = date.today()
    # 计算过去一周的日期
    for i in range(7):
        date_arr.append(today - timedelta(days=i))

res_arr = []
# 指定要遍历的文件夹路径
code_folder_path = "/Users/liubin/code"

for date_item in date_arr:
    # 遍历文件夹
    date_res = []
    for item in os.listdir(code_folder_path):
        # 打印文件夹中的文件
        item_path = os.path.join(code_folder_path, item)
        # 判断是否为文件夹
        if not os.path.isdir(item_path):
            continue
        if ".git" not in os.listdir(item_path):
            continue

        # 调用git log,输出格式为json
        result = subprocess.run(
            ["git", "remote", "-v"],
            stdout=subprocess.PIPE,
            cwd=item_path,
            encoding="utf-8",
            check=False,
        )
        if "valueonline" not in result.stdout:
            continue
        result = subprocess.run(
            ["git", "config", "user.name"],
            stdout=subprocess.PIPE,
            cwd=item_path,
            encoding="utf-8",
            check=False,
        )
        # git log --all
        # --since="$selected_date 00:00:00"
        # --until="$selected_date 23:59:59"
        # --author="$(git config user.name)"
        # --pretty=format:"%s" | uniq | grep -v "^Merge"
        result = subprocess.run(
            [
                "git",
                "log",
                "--all",
                "--since=" + date_item.strftime("%Y-%m-%d") + " 00:00:00",
                "--until=" + date_item.strftime("%Y-%m-%d") + " 23:59:59",
                "--author=" + result.stdout.split()[0],
                "--pretty=format:%s",
            ],
            stdout=subprocess.PIPE,
            cwd=item_path,
            encoding="utf-8",
            check=False,
        )
        if result.stdout == "":
            continue
        result = result.stdout
        # 过滤掉Merge
        # 使用列表解析过滤要删除的元素

        result = [x for x in result.splitlines() if not x.startswith("Merge")]
        # 逆序
        result.reverse()
        date_res.extend(result)
    if len(date_res) == 0:
        continue
    res_arr.append(
        {
            "title": f'{date_item.strftime("%Y-%m-%d-%A")} : {len(date_res)}',
            "arg": "\n".join(date_res),
        }
    )

# res
json_obj = {"items": res_arr}
json_str = json.dumps(json_obj, ensure_ascii=False)
sys.stdout.write(json_str)
