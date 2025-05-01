# 🥋【2025-04-19（土）｜Python道場・第二十三問】
# 🎯 お題："file1.csv" と "file2.csv" を読み込んで、
#     すべての行を "merged.csv" に書き出せ！
#
# 【条件】
# - 各ファイルの形式は同じとする（例：3列のCSV）
# - 両ファイルにヘッダーはないものとする（単純なデータ行だけ）
# - 書き出し先ファイル名は "merged.csv"
# - ファイルの読み書きには `csv` モジュールを使うこと
# - パスは `os.path.dirname(__file__)` を使って構築しよう！

import os, csv

base_dir = os.path.dirname(__file__)
file1_path = os.path.join(base_dir, "file1.csv")
file2_path = os.path.join(base_dir, "file2.csv")
merged_path = os.path.join(base_dir, "merged.csv")

with open(file1_path, "r", encoding="utf-8") as f1:
    list_f1 = list(csv.reader(f1))
    
with open(file2_path, "r", encoding="utf-8") as f2:
    list_f2 = list(csv.reader(f2))

with open(merged_path, "w", newline="", encoding="utf-8") as f3:
    merged = csv.writer(f3)
    for row in (list_f1 + list_f2):
        merged.writerow(row)