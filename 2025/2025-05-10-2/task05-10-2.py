# 🥋【2025-05-10（水）｜Python道場・第五十問（DictReader・条件付き合併編）】
# 🎯 お題："users1.csv" と "users2.csv" を読み込み、
#     メールアドレスが両方に存在するユーザーだけを抽出し、
#     "common_users.csv" に書き出せ！
#
# 【条件】
# - 読み取り元ファイル名："users1.csv"、"users2.csv"（ヘッダーは name,email,level）
# - 書き出し先ファイル名："common_users.csv"
# - `csv.DictReader()` を使って読み込むこと
# - `csv.DictWriter()` を使って書き出すこと
# - **両方のファイルに存在するメールアドレス** を基準に抽出する
# - 出力CSVにはヘッダー行も含めること
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
# → common_users.csv に出力される内容：
# name,email,level
# Bob,bob@example.com,Intermediate

import os
import csv

base_dir = os.path.dirname(__file__)
users1_path = os.path.join(base_dir, "users1.csv")
users2_path = os.path.join(base_dir, "users2.csv")
common_users_path = os.path.join(base_dir, "common_users.csv")

# ベースになるCSVを読み込み
with open(users1_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    users1 = list(reader)
    csv_fieldnames = reader.fieldnames

# 重複判定用のCSVを読み込んで、メールアドレスだけsetで抽出
with open(users2_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    users2_emails = {row["email"] for row in reader}

# ベース配列を回してメアド重複判定、重複したら書き出し配列に格納
duplicate_email_rows = []
for row in users1:
    if row["email"] in users2_emails:
        duplicate_email_rows.append(row)

# 書き出し処理
with open(common_users_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=csv_fieldnames)
    writer.writeheader()
    writer.writerows(duplicate_email_rows)
