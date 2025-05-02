# 🥋【2025-05-02（金）｜Python道場・第40問】
# 🎯 お題：
# file1.csv / file2.csv を読み込み、
# 2列目が "Python"（大文字小文字問わず）である行のみを抽出し、
# その中の3列目（数値）を合計して出力せよ！
#
# 【条件】
# - extend()で2ファイル結合OK
# - 抽出条件は `"python" in row[1].lower()`
# - 合計は `sum()` を使っても、for文でもOK
# - 出力は `print()`で表示するだけでOK（ファイル書き出しは不要）

import os
import csv

base_dir = os.path.dirname(__file__)
total_path = os.path.join(base_dir, "total.csv")

merge_rows = []
for path in ("file1.csv", "file2.csv"):
    with open(os.path.join(base_dir, path), "r", encoding="utf-8") as f:
        merge_rows.extend(csv.reader(f))

filtered_nums = [int(row[2]) for row in merge_rows if "python" in row[1].lower()]
num_total = sum(filtered_nums)

print(num_total)
