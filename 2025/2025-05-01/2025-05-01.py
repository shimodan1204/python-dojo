# 🥋【2025-04-28（月・祝）｜Python道場・第三十九問】
# 🎯 お題：
# "file1.csv" と "file2.csv" を読み込み、
# 2列目が "Python"（大文字小文字問わず）である行のみを抽出し、
# その中で **完全一致の重複行を削除**して、
# 新しいCSVファイルに出力せよ！
#
# 【条件】
# - extend()で2ファイルを結合してOK
# - 抽出条件は "python" in row[1].lower()
# - 重複判定は「行全体が一致していること」
# - 順序は元の出現順でよい（ソート不要）

import os
import csv

base_dir = os.path.dirname(__file__)
filtered_path = os.path.join(base_dir, "filtered.csv")

# 読み込み＆結合
merge_rows = []
for path in ("file1.csv", "file2.csv"):
    with open(os.path.join(base_dir, path), "r", encoding="utf-8") as f:
        merge_rows.extend(csv.reader(f))

# 抽出
filtered_rows = []
for row in merge_rows:
    if "python" in row[1].lower() and not(tuple(row) in filtered_rows):
        filtered_rows.append(tuple(row))

# 書き出し
with open(filtered_path, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(filtered_rows)
