# 🥋【2025-05-06（火）｜Python道場・第四十六問（DictWriterの応用・カラム追加編）】
# 🎯 お題："users.csv" を読み込み、全ユーザーのデータに 'is_expert' カラムを追加し、
#     "users_labeled.csv" に出力せよ！

# 【条件】
# - 読み取り元ファイル名："users.csv"（ヘッダー：name,email,level）
# - 書き出し先ファイル名："users_labeled.csv"
# - `csv.DictReader()` で読み込み
# - `csv.DictWriter()` で書き込み
# - 追加カラム：'is_expert' を各辞書に追加
#     - 'level' が 'Expert' の場合 → 'is_expert': 'yes'
#     - それ以外の場合 → 'is_expert': 'no'
# - 書き出しのフィールド順は「元の3カラム + is_expert」の順
# - ヘッダー行も含めて書き出す（`writer.writeheader()`）

import os
import csv

base_dir = os.path.dirname(__file__)
users_path = os.path.join(base_dir, "0505-3users.csv")
users_loaded_path = os.path.join(base_dir, "0505-3users_loaded.csv")

users_labeled = []
with open(users_path, "r", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if "Expert" == row["level"]:
            row["is_expert"] = "yes"
        else:
            row["is_expert"] = "no"

        users_labeled.append(row)

with open(users_loaded_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, ["name", "email", "level", "is_expert"])
    writer.writeheader()
    writer.writerows(users_labeled)
