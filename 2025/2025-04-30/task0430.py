# 🥋【2025-04-28（月）｜Python道場・第三十九問】
# 🎯 お題：
# "file1.csv" と "file2.csv" を読み込み、
# 2列目に "Python" を含む行だけを抽出し、
# かつ3列目が **数値に変換できる** 行だけを残し、
# 3列目を「昇順」、同じ数値なら1列目（文字列）を「降順」で並び替えよ！
#
# 【条件】
# - try/except を使って数値変換エラーを除外すること
# - 並び替えは key=lambda row: (int(row[2]), "".join(reversed(row[0])))

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
filtered_rows = []
for row in merge_rows:
    if "python" in row[1].lower():
        try:
            int(row[2])
            filtered_rows.append(row)
        except ValueError as e:
            print(f"{row[2]}:{e}")

# 並び替え
sorted_rows = sorted(filtered_rows, key=lambda row: (int(row[2]), "".join(reversed(row[1]))))

# 書き出し
with open(sorted_path, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(sorted_rows)
