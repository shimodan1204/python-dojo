# 🥋【2025-05-05（月）｜Python道場・第四十五問（DictReader & DictWriter編）】
# 🎯 お題："users.csv" を読み込み、'level' が 'Expert' の行だけを抽出し、
#     そのユーザーの「name」と「email」だけを "experts.csv" に書き出せ！
#
# 【条件】
# - 読み取り元ファイル名："users.csv"（ヘッダーは name,email,level）
# - 書き出し先ファイル名："experts.csv"（ヘッダーは name,email）
# - 読み込みには `csv.DictReader()` を使うこと
# - 書き出しには `csv.DictWriter()` を使うこと
# - `DictWriter` を使う際は、書き出す列（フィールド名）を指定すること
# - ヘッダー行も書き出すこと (`writer.writeheader()`)
#
# 【例】
# users.csv の中身：
# name,email,level
# Alice,alice@ex.com,Expert
# Bob,bob@ex.com,Intermediate
# Charlie,charlie@ex.com,Expert
# David,dave@ex.com,Beginner
#
# → experts.csv に出力される内容：
# name,email
# Alice,alice@ex.com
# Charlie,charlie@ex.com

import os
import csv

base_dir = os.path.dirname(__file__)
users_path = os.path.join(base_dir, "users.csv")
experts_path = os.path.join(base_dir, "experts.csv")

with open(users_path, "r", newline="", encoding="utf-8") as f:
    filtered_rows = [row for row in csv.DictReader(f) if row["level"] == "Expert"]

with open(experts_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f,["name", "email"])
    writer.writeheader()
    for row in filtered_rows:
        expert_row = {"name" : row["name"], "email" : row["email"]}
        writer.writerow(expert_row)
