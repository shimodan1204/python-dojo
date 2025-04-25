# 🥋【2025-04-25（金）｜Python道場・第三十二問】
# 🎯 お題："file1.csv" と "file2.csv" を結合し、
#     「3列目（インデックス2）を数値として昇順にソート」して、
#     "sorted.csv" に出力せよ！
#
# 【条件】
# - ソートキーは `int(row[2])` を使う（全て整数と仮定）
# - 並び替えは昇順（小さい順）
# - 結合と同時に抽出しても、分けて処理してもOK
# - 書き出しには `csv.writer().writerows()` を使ってOK

import os
import csv

base_dir = os.path.dirname(__file__)
sorted_path = os.path.join(base_dir, "sorted.csv")

# 読み込み
rows =[]
for path in ("file1.csv", "file2.csv"):
    with open(os.path.join(base_dir, path), "r", encoding="utf-8") as f:
        rows += list(csv.reader(f))

# 並び替え
rows.sort(key=lambda r: int(r[2]))

# 書き出し
with open(sorted_path, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)