# 🥋【2025-04-28（月・祝）｜Python道場・第三十七問（sort最終奥義編）】
# 🎯 お題："file1.csv" と "file2.csv" を読み込み、
#     2列目に "Python" を含む行だけを抽出し、
#     3列目（数値）を「降順」で並び替え、
#     同じ数値なら1列目（文字列）も「降順」で並び替えよ！
#
# 【条件】
# - 数値は -int() を使って降順
# - 文字列は reverseテクニックを駆使して降順
# - lambda式＋複合キーを作り、sortすること
# - extend()を使ったファイル結合も引き続きOK
#
# 【ポイント】
# - 複合キーで両方降順にするロジックを自然に操れるか！

import os
import csv

base_dir = os.path.dirname(__file__)
sorted_path1 = os.path.join(base_dir, "sorted1.csv")
sorted_path2 = os.path.join(base_dir, "sorted2.csv")

# 読み込み＆結合
merge_rows = []
for path in ("file1.csv","file2.csv"):
    with open(os.path.join(base_dir, path), "r", encoding="utf-8") as f:
        merge_rows.extend(csv.reader(f))
        
# 抽出
filtered_rows = [row for row in merge_rows if "python" in row[1].lower()]

# 並び替え：すべて降順パターン
filtered_rows.sort(key=lambda row: (int(row[2]), row[1]), reverse=True)

# 書き出し：すべて降順パターン
with open(sorted_path1, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(filtered_rows)

# 並び替え：個別降順パターン
filtered_rows.sort(key=lambda row: (-int(row[2]), "".join(reversed(row[1]))))

# 書き出し：すべて降順パターン
with open(sorted_path2, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(filtered_rows)
