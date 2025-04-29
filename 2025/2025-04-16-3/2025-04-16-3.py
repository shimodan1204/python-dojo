# 🥋【2025-04-15（火）｜Python道場・第十八問】
# 🎯 お題："sample.csv" の中身を読み取り、
#     1行ごとに「行番号付き」で "log.txt" に出力せよ！
#
# 【条件】
# - 読み取り元ファイル名："sample.csv"
# - 書き出し先ファイル名："log.txt"
# - 出力形式は「1: ['A', 'Python', 'C']」のようにする
# - 行番号は 1 から始めること（`enumerate(..., start=1)` を使おう）
# - 書き出しは **上書きモード（"w"）**

import os
import csv
file_path = os.path.join(os.path.dirname(__file__), "sample.csv")
with open(file_path, "r", encoding="utf-8") as f:
    rows = [row for row in csv.reader(f)]
    print(rows)
    
file_path = os.path.join(os.path.dirname(__file__), "log.txt")
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write("\n".join([f"{index}: {row}" for index, row in enumerate(rows, start=1)]))
        
print(__file__)