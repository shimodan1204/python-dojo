# 🥋【2025-04-18（金）｜Python道場・第二十二問】
# 🎯 お題："sample.csv" の中から「2列目に 'Python' を含む行」だけを抽出し、
#     - "filtered.csv" に書き出す
#     - 同時に行数を "log.txt" に書き出す
#
# 【条件】
# - ファイル名：
#     - 読み取り："sample.csv"
#     - 書き出し："filtered.csv"（条件に合う行のみ）
#     - ログ："log.txt"（"抽出件数：X件" という形式で書く）
# - "Python" は部分一致（例："I love Python", "Pythonista" などもOK）
# - 判定には大文字小文字を無視する（`.lower()` を使おう）
# - 書き出し形式は CSV形式でOK（ `",".join(row)` または `writer.writerow(row)` ）
# - パスは `os.path.dirname(__file__)` を使って構築すること

import os, csv
base_dir = os.path.dirname(__file__)

# 読み込み
file_path = os.path.join(base_dir, "sample.csv")
with open(file_path, "r", encoding="utf-8") as f:
    reader = list(csv.reader(f))

# マッチ列の書き出し
match_rows_count = 0
file_path = os.path.join(base_dir, "filtered.csv")
with open(file_path, "w", newline="", encoding="utf-8") as f:
    for row in reader:
        if "python" in row[1].lower():
            f.write(f"{",".join(row)}\n")
            match_rows_count += 1

# マッチ行数の書き出し
file_path = os.path.join(base_dir, "log.txt")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"抽出件数：{match_rows_count}件")

# 書き出し一行にしてみた
file_path = os.path.join(base_dir, "log2.txt")
with open(file_path, "w", newline="", encoding="utf-8") as f:            
    f.write("\n".join([f"{",".join(row)}" for row in reader if "python" in row[1].lower()]))
    