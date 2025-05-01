# 🥋【2025-04-21（月）｜Python道場・第二十五問】
# 🎯 お題："sample.csv" を読み込み、
#     まったく同じ行が2回以上出てくるものだけを "duplicated.csv" に書き出せ！
#
# 【条件】
# - 入力ファイル："sample.csv"
# - 出力ファイル："duplicated.csv"
# - 行全体が同じであるもの（["A", "Python", "1"] など）が重複とみなされる
# - 出力には**重複していた行だけ1度だけ**書き出せばOK
# - `collections.Counter()` を使っても、辞書でカウントしてもOK！

import os, csv
from collections import Counter

base_dir = os.path.dirname(__file__)
sample_path = os.path.join(base_dir, "sample.csv")
duplicated_path = os.path.join(base_dir, "duplicated.csv")

with open(sample_path, "r", encoding="utf-8") as f:
    rows = [tuple(row) for row in csv.reader(f)]
    
with open(duplicated_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row,counter in Counter(rows).items():
        if counter > 1:
            writer.writerow(row)