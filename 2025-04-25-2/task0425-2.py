# 🥋【2025-04-25（金）｜Python道場・第三十三問（sort強化編）】
# 🎯 お題："file1.csv" と "file2.csv" を読み込み、
#     3列目（インデックス2）を数値として"降順"に並び替え、
#     "sorted.csv" に出力せよ！
#
# 【条件】
# - ソートキーは int(row[2])
# - 大きい値が先に来る（reverse=True を使う）
# - lambdaを使って書くこと
# - 読み込みと書き出しは自由（1ファイルにまとめてもいい）

import os
import csv

base_dir = os.path.dirname(__file__)
sorted_path = os.path.join(base_dir, "sorted.csv")

# 読み込み
merge_rows = []
for path in ("file1.csv", "file2.csv"):
    with open(os.path.join(base_dir, path), "r", encoding="utf-8") as f:
        merge_rows += list(csv.reader(f))
        
# 並び替え
merge_rows.sort(key=lambda r: int(r[2]), reverse=True)

# 書き出し
with open(sorted_path, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(merge_rows)