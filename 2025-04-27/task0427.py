# 🥋【2025-04-27（日）｜Python道場・第三十六問（sort応用・複合キー）】
# 🎯 お題："file1.csv" と "file2.csv" を読み込み、
#     2列目に "Python" を含む行だけを抽出し、
#     3列目（数値）を「降順」で並び替え、
#     同じ数値だった場合は1列目（文字列）で「昇順」で並び替えよ！
#
# 【条件】
# - まず3列目（インデックス2）を数値化して降順
# - 次に1列目（インデックス0）を文字列昇順
# - lambda式＋タプルのキーでsortすること
# - extend()を使ってファイル結合もOK
#
# 【ポイント】
# - ソートキーに (優先キー, サブキー) のタプルを渡すと複合キー並び替えできる！

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
filtered_rows = [row for row in merge_rows if "python" in row[1].lower()]

# 並び替え
filtered_rows.sort(key=lambda row: (-int(row[2]), row[0]))

# 書き出し
with open(sorted_path, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(filtered_rows)