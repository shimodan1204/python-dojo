# 🥋【2025-05-04（日）｜Python道場・第四十三問（DictReader活用編）】
# 🎯 お題："data.csv" を読み込み、「language」列が「Python」である行だけを辞書形式で表示せよ！
#
# 【条件】
# - 読み取り元ファイル名："data.csv"（ヘッダーは name,language,level）
# - `csv.DictReader()` を使って読み込むこと
# - `row['language']` を使って条件判定すること
# - 抽出した行（辞書）をそのまま `print()` で表示すればOK
#
# 【例】
# data.csv の中身：
# name,language,level
# Alice,Python,Expert
# Bob,Java,Intermediate
# Charlie,Python,Beginner
#
# 出力：
# {'name': 'Alice', 'language': 'Python', 'level': 'Expert'}
# {'name': 'Charlie', 'language': 'Python', 'level': 'Beginner'}

import os
import csv

base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, "data.csv")

with open(data_path, "r", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if "python" == row["language"].lower():
            print(row)
