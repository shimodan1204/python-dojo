# 🥋【2025-04-24（木）｜Python道場・第三十一問】
# 🎯 お題："file1.csv" と "file2.csv" を読み込み、
#     「2列目（インデックス1）が 'Python'」の行だけを抽出し、
#     "filtered.csv" に書き出せ！
#
# 【条件】
# - 判定は大文字小文字を無視してOK（"python" in row[1].lower()）
# - 読み取り元：file1.csv と file2.csv（どちらも同じ形式）
# - 抽出した行は順番に書き出すこと
# - 書き出しには `csv.writer().writerows()` を使ってOK！

import os
import csv

base_dir = os.path.dirname(__file__)
f1_path = os.path.join(base_dir, "file1.csv")
f2_path = os.path.join(base_dir, "file2.csv")
filtered_path = os.path.join(base_dir, "filtered.csv")

# 読み込み
rows = []
for path in (f1_path, f2_path):
    with open(path, "r", encoding="utf-8") as f:
        rows = rows + list(csv.reader(f))
        
# 抽出
filtered_rows = [row for row in rows if "python" == row[1].lower()]

# 書き出し
with open(filtered_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(filtered_rows)