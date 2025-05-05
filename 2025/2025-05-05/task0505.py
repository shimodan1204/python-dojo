# 🥋【2025-05-05（月）｜Python道場・第四十四問（DictReaderフィルタ＆抽出編）】
# 🎯 お題："users.csv" を読み込み、'level' が 'Expert' の人の 'name' だけを表示せよ！
#
# 【条件】
# - 読み取り元ファイル名："users.csv"（ヘッダーは name,email,level）
# - `csv.DictReader()` を使って読み込むこと
# - `row['level'] == 'Expert'` の行だけを抽出する
# - 抽出した行の中から `row['name']` の値だけを `print()` で表示すること（1行に1人）
#
# 【例】
# users.csv の中身：
# name,email,level
# Alice,alice@ex.com,Expert
# Bob,bob@ex.com,Intermediate
# Charlie,charlie@ex.com,Expert
# David,dave@ex.com,Beginner
#
# 出力：
# Alice
# Charlie

import os
import csv

base_dir = os.path.dirname(__file__)
users_path = os.path.join(base_dir, "users.csv")

with open(users_path, "r", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if "Expert" == row["level"]:
            print(row["name"])
