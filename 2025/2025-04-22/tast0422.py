# 🥋【2025-04-22（火）｜Python道場・第二十七問】
# 🎯 お題："sample.csv" の中から「1列目（インデックス0）に 'A' が含まれる行」だけを抽出し、
#     "filtered.csv" に書き出せ！
#
# 【条件】
# - 判定は部分一致でOK（例："AA", "Apple", "Amazing" など）
# - 大文字小文字の区別はしない（".lower()" を使ってもOK）
# - 出力は `csv.writer().writerows()` などでCSV形式に！
# - 読み取り元："sample.csv"
# - 書き出し先："filtered.csv"
# - パスは `os.path.dirname(__file__)` で構築してみよう！

import os
import csv

base_dir = os.path.dirname(__file__)
sample_path = os.path.join(base_dir, "sample.csv")
filtered_path = os.path.join(base_dir, "filtered.csv")

# 読み取り
with open(sample_path, "r", encoding="utf-8") as f:
    reader = list(csv.reader(f))

# 抽出
matches = [row for row in reader if "A" in row[0].upper()]

# 書き出し
with open(filtered_path, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(matches)