# 🥋【2025-04-17（水）｜Python道場・第二十問】
# 🎯 お題："sample.csv" の行数をカウントし、
#     "log.txt" に「行数：◯行」と書き出せ！
#
# 【条件】
# - ファイル名："sample.csv"（読み取り元）・"log.txt"（書き出し先）
# - 結果の書き出し形式は：「行数：3行」など
# - 書き出しは上書きモード（"w"）
# - パスは `os.path.dirname(__file__)` を使って構築してみよう！（ステップ1練習！）

import os
import csv

base_dir = os.path.dirname(__file__)
read_path = os.path.join(base_dir, "sample.csv")

with open(read_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)
    
save_path = os.path.join(base_dir, "log,txt")
with open(save_path, "w", encoding="utf-8") as f:
    f.write(f"行数：{len(rows)}行")
    f.write(f"\n行数：{sum(1 for _ in rows)}行")
