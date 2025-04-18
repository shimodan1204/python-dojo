# 🥋【2025-04-17（水）｜Python道場・第十九問】
# 🎯 お題："sample.csv" の中から「2列目に 'Python' が“含まれる”」行だけを抽出せよ！
#
# 【条件】
# - ファイル名："sample.csv"
# - 2列目（インデックス1）の値が "Python" を“含む”行だけを対象とする
#   ※ 完全一致ではなく、「Python3」「I love Python」なども含める
# - 結果はリストで出力すればOK（[['A', 'I love Python', 'C'], ...] など）
import os
import csv

def generate_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

file_path = generate_file_path("sample.csv")

with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print([row for row in reader if "python" in row[1].lower()])
    