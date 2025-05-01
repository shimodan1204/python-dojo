# 🥋【2025-04-26（土）｜Python道場・第三十五問（extend実戦編）】
# 🎯 お題："file1.csv" と "file2.csv" を読み込み、
#     2列目に "Python" を含む行だけを抽出し、
#     抽出した行をすべてまとめて "filtered_python.csv" に出力せよ！
#
# 【条件】
# - "Python" を含む行だけ（大文字小文字無視OK）
# - ファイルごとにフィルタした後、リストに「まとめる」ときに`extend()`を使うこと！
# - 書き出し時は行単位でCSV形式にすること
#
# 【ポイント】
# - extend() を自然に使いこなす型を意識する！
# - フィルタとマージの順番に注意する！

import os
import csv

base_dir = os.path.dirname(__file__)
filtered_python_path = os.path.join(base_dir, "filtered_python.csv")

# 読み込み
filtered_rows = []
for path in ("file1.csv", "file2.csv"):
    with open(os.path.join(base_dir, path), "r", encoding="utf-8") as f:
        # 抽出
        extract_rows = [row for row in csv.reader(f) if "python" in row[1].lower()]

        # 結合
        filtered_rows.extend(extract_rows)

# 書き出し
with open(filtered_python_path, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(filtered_rows)