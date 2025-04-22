# 🥋【2025-04-22（火）｜Python道場・第二十八問】
# 🎯 お題："sample.csv" の中から「3列目（インデックス2）が 5 より大きい」行だけを抽出し、
#     "filtered.csv" に書き出せ！
#
# 【条件】
# - 3列目の値は「整数の文字列」として格納されている想定（例："1", "5", "10"）
# - 判定のために int() に変換してから比較すること（例：`int(row[2]) > 5`）
# - 読み取り元："sample.csv"
# - 書き出し先："filtered.csv"
# - 書き出しには `csv.writer().writerows()` を使ってOK！
# - パスは `os.path.dirname(__file__)` で構築すること！

import os
import csv

base_dir = os.path.dirname(__file__)
sample_path = os.path.join(base_dir, "sample.csv")
filtered_path = os.path.join(base_dir, "filtered.csv")

# 読み取り
with open(sample_path, "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))
    
# 抽出
try:
    filtered_rows = [row for row in rows if int(row[2]) > 5]
except ValueError as e:
    print(e)
else:
    # 書き出し
    with open(filtered_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)
        print("filter completed！")