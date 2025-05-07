# 🥋【2025-05-06（火）｜Python道場・第四十七問（DictReader条件抽出＆ファイル書き出し編）】
# 🎯 お題："users.csv" を読み込み、'level' が 'Intermediate' のユーザーだけを抽出し、
#     'name' と 'email' のみを "intermediate_users.csv" に書き出せ！
#
# 【条件】
# - 読み取り元ファイル名："users.csv"（ヘッダーは name,email,level）
# - 書き出し先ファイル名："intermediate_users.csv"
# - `csv.DictReader()` を使って読み込むこと
# - `csv.DictWriter()` を使って書き出すこと
# - 抽出条件は `row['level'] == 'Intermediate'`
# - 出力CSVにはヘッダー行も含めること

import os
import csv

base_dir = os.path.dirname(__file__)
users_path = os.path.join(base_dir, "users.csv")
intermediate_users_path = os.path.join(base_dir, "intermediate_users.csv")

filtered_rows = []
with open(users_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["level"] == "Intermediate":
            filtered_rows.append({
                "name" : row["name"],
                "email" : row["email"]
            })

with open(intermediate_users_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "email"])
    writer.writeheader()
    writer.writerows(filtered_rows)
