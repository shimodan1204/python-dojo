# 🥋【2025-05-07（水）｜Python道場・第四十八問（DictReader条件抽出 & 集約編）】
# 🎯 お題："users.csv" を読み込み、各 "level" ごとに所属するユーザー数をカウントし、
#     結果を "level_summary.csv" に書き出せ！
#
# 【条件】
# - 読み取り元ファイル名："users.csv"（ヘッダーは name,email,level）
# - 書き出し先ファイル名："level_summary.csv"
# - `csv.DictReader()` を使って読み込むこと
# - 集約結果は以下の形式で書き出すこと
#
# 【出力例】
# level,count
# Expert,2
# Intermediate,3
# Beginner,1
#
# 【ヒント】
# - 集約には `collections.Counter` が便利
# - カウント結果は辞書形式で保持できる
# - CSV書き出しには `csv.writer()` を使うこと

import os
import csv
from collections import Counter

base_dir = os.path.dirname(__file__)
users_path = os.path.join(base_dir, "users.csv")
level_summary_path = os.path.join(base_dir, "level_summary.csv")

with open(users_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    levels = [row["level"] for row in reader]
    level_counts = Counter(levels)

level_counts_rows = [{"level":key,"count":value} for key, value in level_counts.items()]

with open(level_summary_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=["level", "count"])
    writer.writeheader()
    writer.writerows(level_counts_rows)
