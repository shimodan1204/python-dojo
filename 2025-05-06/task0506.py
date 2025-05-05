# 🥋【2025-05-06（火）｜Python道場・第四十六問（Dictデータ加工＆書き出し編）】
# 🎯 お題："users.csv" を読み込み、'level' が 'Expert' の行だけを抽出し、
#     そのユーザーの「nameを大文字にしたもの」と「emailにドメイン(@company.com)を付与したもの」を
#     "processed_experts.csv" に書き出せ！
#
# 【条件】
# - 読み取り元ファイル名："users.csv"（ヘッダーは name,email,level）
# - 書き出し先ファイル名："processed_experts.csv"
# - 書き出し先のヘッダーは `NAME,full_email` とすること
# - 読み込みには `csv.DictReader()` を使うこと
# - 書き出しには `csv.DictWriter()` を使うこと
# - 処理内容：
#     - `level` が 'Expert' の行のみ対象
#     - 書き出す辞書には 'NAME' キーで `row['name'].upper()` の値を格納
#     - 書き出す辞書には 'full_email' キーで `f"{row['email']}@company.com"` の値を格納

import os
import csv

base_dir = os.path.dirname(__file__)
users_path = os.path.join(base_dir, "users.csv")
experts_path = os.path.join(base_dir, "processed_experts.csv")

expert_rows = []
with open(users_path, "r", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if "Expert" == row["level"]:
            expert_rows.append(row)

expert_rows_edited = []
for row in expert_rows:
    expert_rows_edited.append({
        "NAME" : row["name"].upper()
        ,"full_email" : row["email"] + "@company.com"
    })

with open(experts_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["NAME", "full_email"])
    writer.writeheader()
    writer.writerows(expert_rows_edited)
