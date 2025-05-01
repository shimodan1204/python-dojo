# 🥋【2025-04-21（月）｜Python道場・第二十六問】
# 🎯 お題："sample.csv" から「2列目に 'Python' を含む行」だけを抽出し、
#     - "filtered.csv" に出力せよ！
#     - 同時に抽出件数を "log.txt" に書き出せ！
#
# 【条件】
# - 抽出対象："Python" を含む行（部分一致・大文字小文字無視）
# - 抽出行は CSV形式で書き出し
# - ログには `"抽出件数：X件"` のように書き出すこと
# - 書き込みはすべて上書きでよい（モード "w"）
# - パスは `os.path.dirname(__file__)` で構成しよう！

import os
import csv

base_dir = os.path.dirname(__file__)
sample_path = os.path.join(base_dir, "sample.csv")
filtered_path = os.path.join(base_dir, "filtered.csv")
log_path = os.path.join(base_dir, "log.txt")

# 読み込み
with open(sample_path, "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))

# 抽出
filtered = [row for row in rows if "python" in row[1].lower()]

# 抽出書き込み
with open(filtered_path, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(filtered)
    
# 件数書き込み
with open(log_path, "w", encoding="utf-8") as f:
    f.write(f"抽出件数：{len(filtered)}件")
