# 🥋【2025-04-26（土）｜Python道場・第三十四問（sort強化編②）】
# 🎯 お題："file1.csv" と "file2.csv" を読み込み、
#     2列目に "Python" を含む行だけを抽出し、
#     その中で3列目（インデックス2）を数値として"降順"に並び替え、
#     "sorted_python.csv" に出力せよ！
#
# 【条件】
# - フィルタ条件："Python"を含むかどうか（大文字小文字無視OK）
# - ソートキーは int(row[2])
# - ソートは降順（reverse=True）
# - lambdaを使ってソート
# - 読み込み、フィルタ、ソート、出力の流れをきれいに意識すること！

import os
import csv

base_dir = os.path.dirname(__file__)
sorted_python_path = os.path.join(base_dir, "sorted_python.csv")

# 読み込み
merge_rows = []
for path in ("file1.csv", "file2.csv"):
    with open(os.path.join(base_dir, path), "r", encoding="utf-8") as f:
        merge_rows += list(csv.reader(f))
        
# 抽出
filtered_rows = [row for row in merge_rows if "python" in row[1].lower()]

# 並び替え
filtered_rows.sort(key=lambda row: int(row[2]), reverse=True)

# 書き出し
with open(sorted_python_path, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(filtered_rows)
