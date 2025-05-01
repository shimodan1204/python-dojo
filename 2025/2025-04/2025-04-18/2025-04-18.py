# 🥋【2025-04-18（金）｜Python道場・第二十一問】
# 🎯 お題："sample.csv" の中から「3列目が 'F' の行だけ」を抽出し、
#     "log.txt" に書き出せ！
#
# 【条件】
# - ファイル名："sample.csv"（読み取り元）・"log.txt"（書き出し先）
# - 3列目（インデックス2）の値が "F" と一致する行だけを対象とする
# - 書き出しは上書きモード（"w"）
# - パスは `os.path.dirname(__file__)` を使って構築してみよう！
# - 書き出しは `str(row)` または `",".join(row)` どちらでもOK！

import os
import csv

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "sample.csv")

with open(file_path, "r", encoding="utf-8") as f:
    reader = list(csv.reader(f))
    
file_path = os.path.join(base_dir, "log.txt")
with open(file_path,"w", newline="", encoding="utf-8") as f:
    for row in reader:
        if row[2] == "F":
            f.write(f"{",".join(row)}\n") 
