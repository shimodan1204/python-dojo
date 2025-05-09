# 🥋【2025-05-03（土）｜Python道場・第四十二問（DictReader導入編）】
# 🎯 お題："data.csv" を読み込み、各行を辞書形式で表示する関数を作れ！
#
# 【条件】
# - 読み取り元ファイル名："data.csv"
# - CSVの1行目はヘッダー（列名）として扱うこと
# - `csv.DictReader()` を使って読み込むこと
# - 出力は `print()` で1行ずつ辞書を表示すればOK
#
# 【例】
# data.csv の中身：
# name,language,level
# Alice,Python,Expert
# Bob,Java,Intermediate
#
# 出力：
# {'name': 'Alice', 'language': 'Python', 'level': 'Expert'}
# {'name': 'Bob', 'language': 'Java', 'level': 'Intermediate'}

import os
import csv

base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, "data.csv")

with open(data_path, "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row)
