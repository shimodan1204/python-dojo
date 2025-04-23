# 🥋【2025-04-23（水）｜Python道場・第三十問】
# 🎯 お題："sample.csv" の中から「3列目（インデックス2）が整数で偶数の行」だけを抽出し、
#     "filtered.csv" に書き出せ！
#
# 【条件】
# - 3列目は「文字列の数字」（例："1", "2", "10"）である想定
# - `int(row[2])` で数値化してから `num % 2 == 0` を判定！
# - ただし、数値化できない行があってもエラーにならないよう `try-except` で防ごう！
# - 出力は CSV形式、`csv.writer().writerows()` を使用！

import os
import csv

base_dir = os.path.dirname(__file__)
sample_path = os.path.join(base_dir, "sample.csv")
filtered_path = os.path.join(base_dir, "filtered.csv")

# 読み込み
with open(sample_path, "r", encoding="utf-8") as f:
    reader = list(csv.reader(f))

# 抽出
filtered_rows = []
for row in reader:
    try:
        num = int(row[2])
        if isinstance(num, int) and num % 2 == 0:
            filtered_rows.append(row)
    except Exception as e:
        print(e)
        continue

# 書き出し
with open(filtered_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(filtered_rows)