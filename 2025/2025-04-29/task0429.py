# 🥋【2025-04-28（月・祝）｜Python道場・第三十八問】
# 🎯 お題：
# "file1.csv" と "file2.csv" を読み込み、
# 2列目に "Python" を含み、かつ
# 3列目の数値が50以上の行だけを抽出し、
# 3列目（数値）を「降順」で並び替え、
# 同じ数値なら1列目（文字列）を「昇順」で並び替えよ！
#
# 【条件】
# - extend()で2ファイル結合OK
# - フィルタ時に数値比較する（int(row[2]) >= 50）
# - 並び替えは key=lambda row: (-int(row[2]), row[0])

import os
import csv

base_dir = os.path.dirname(__file__)
sorted_path = os.path.join(base_dir, "sorted.csv")

# 読み込み＆結合
merge_rows = []
for path in ("file1.csv", "file2.csv"):
    with open(os.path.join(base_dir, path), "r", encoding="utf-8") as f:
        merge_rows.extend(csv.reader(f))

# 抽出
filtered_rows = [row for row in merge_rows if "python" in row[1].lower() and int(row[2])>=50]

# 並び替え
filtered_rows.sort(key=lambda row: (-int(row[2]), row[0]))

# 書き出し
with open(sorted_path, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(filtered_rows)
