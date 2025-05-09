# 🥋【2025-05-06（火）｜Python道場・第四十八問（DictReader応用編・重複排除）】
# 🎯 お題："users.csv" を読み込み、'email' が重複する行を除外した結果を
#     "unique_users.csv" に書き出せ！
#
# 【条件】
# - 読み取り元ファイル名："users.csv"（ヘッダーは name,email,level）
# - 書き出し先ファイル名："unique_users.csv"
# - `csv.DictReader()` を使って読み込むこと
# - `csv.DictWriter()` を使って書き出すこと
# - 重複チェックの基準は「email」列
# - **最初に出てきた行だけ残し、それ以降の重複は無視する**
# - 出力CSVにはヘッダー行も含めること
#
# 【例】
# users.csv の中身：
# name,email,level
# Alice,alice@example.com,Expert
# Bob,bob@example.com,Intermediate
# Charlie,charlie@example.com,Beginner
# Dave,alice@example.com,Intermediate
#
# → unique_users.csv に出力される内容：
# name,email,level
# Alice,alice@example.com,Expert
# Bob,bob@example.com,Intermediate
# Charlie,charlie@example.com,Beginner

import os
import csv

base_dir = os.path.dirname(__file__)
users_path = os.path.join(base_dir, "users.csv")
unique_users_path = os.path.join(base_dir, "unique_users.csv")

unique_email = set()
unique_rows = []
with open(users_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["email"] not in unique_email:
            unique_email.add(row["email"])
            unique_rows.append(row)

with open(unique_users_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=["name","email","level"])
    writer.writeheader()
    writer.writerows(unique_rows)
