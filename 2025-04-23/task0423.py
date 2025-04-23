# 🥋【2025-04-23（水）｜Python道場・第二十九問】
# 🎯 お題："sample.csv" の中から「2列目（インデックス1）に 'Java' を含まない行」だけを抽出し、
#     "filtered.csv" に書き出せ！
#
# 【条件】
# - 判定は部分一致でOK（例："JavaScript" も含む）
# - 'Java' を含ま**ない**行のみが対象
# - 判定には `.lower()` を使ってもOK（"java" 大文字小文字は無視）
# - 読み取り元："sample.csv"
# - 書き出し先："filtered.csv"
# - 書き出しは `csv.writer().writerows()` を使ってOK！
# - パスは `os.path.dirname(__file__)` で構築してみよう！

import os
import csv

base_dir = os.path.dirname(__file__)
sample_path = os.path.join(base_dir, "sample.csv")
filtered_path = os.path.join(base_dir, "filtered.csv")

# ファイル開く
with open(sample_path, "r", encoding="utf-8") as f:
    reader = list(csv.reader(f))
    
# 抽出
tuple_rows = [tuple(row) for row in reader]
filtered_rows = [row for row in tuple_rows if not "java" in row[1].lower()]

# 書き出し
with open(filtered_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(filtered_rows)