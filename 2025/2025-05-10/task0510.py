# 🥋【2025-05-10（水）｜Python道場・第四十九問（DictReader & Merge編）】
# 🎯 お題："users1.csv" と "users2.csv" を読み込み、
#     メールアドレスをキーに結合した結果を "merged_users.csv" に書き出せ！
#
# 【条件】
# - 読み取り元ファイル名："users1.csv"、"users2.csv"（ヘッダーは name,email,level）
# - 書き出し先ファイル名："merged_users.csv"
# - `csv.DictReader()` を使って読み込むこと
# - `csv.DictWriter()` を使って書き出すこと
# - **メールアドレス（email）** をキーとして、`users1` のデータを優先して結合
# - 結合後は、重複しない行も含めて全て出力する
# - ヘッダー行も含めて書き出すこと
#
# 【例】
# users1.csv の中身：
# name,email,level
# Alice,alice@example.com,Expert
# Bob,bob@example.com,Intermediate
# Charlie,charlie@example.com,Beginner
#
# users2.csv の中身：
# name,email,level
# Bob,bob@example.com,Advanced
# Dave,dave@example.com,Intermediate
# Eve,eve@example.com,Expert
#
# → merged_users.csv に出力される内容：
# name,email,level
# Alice,alice@example.com,Expert
# Bob,bob@example.com,Intermediate
# Charlie,charlie@example.com,Beginner
# Dave,dave@example.com,Intermediate
# Eve,eve@example.com,Expert

import os
import csv

base_dir = os.path.dirname(__file__)
users1_path = os.path.join(base_dir, "users1.csv")
users2_path = os.path.join(base_dir, "users2.csv")
merged_users_path = os.path.join(base_dir, "merged_users.csv")

used_emails = set()
merge_rows = []
csv_fieldnames = []
for path in (users1_path, users2_path):
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        csv_fieldnames = csv_fieldnames or reader.fieldnames
        for row in reader:
            if  row["email"] not in used_emails:
                used_emails.add(row["email"])
                merge_rows.append(row)

with open(merged_users_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=csv_fieldnames)
    writer.writeheader()
    writer.writerows(merge_rows)
