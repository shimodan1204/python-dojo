# ----------------------------------------
# 🥋 Python道場【41問目】
#
# お題：
# 次の条件をすべて満たす行だけを抽出し、
# 3列目（数値）で昇順に並び替えて、filtered.csv に書き出せ！
#
# 条件：
# - file1.csv と file2.csv を読み込む
# - 2列目に "Python" を含む（大文字・小文字は問わない）
# - 1列目が "A" で始まる行だけ抽出する
#
# 出力：
# - 抽出した行を filtered.csv に書き出すこと
# - ソートは 3列目の数値（昇順）
# ----------------------------------------

import os
import csv

base_dir = os.path.dirname(__file__)
filtered_path = os.path.join(base_dir, 'filtered.csv')

# 読み込み＆結合
merge_rows = []
for path in ("file1.csv", "file2.csv"):
    with open(os.path.join(base_dir, path), 'r', encoding='utf-8') as f:
        merge_rows.extend(csv.reader(f))

# 抽出&並び替え
filtered_rows = []
for row in merge_rows:
    if row[0].startswith("A") and "python" in row[1].lower():
        filtered_rows.append(row)

filtered_rows.sort(key=lambda row: int(row[2]))

with open(filtered_path, 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(filtered_rows)
