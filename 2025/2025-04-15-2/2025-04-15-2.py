# 🥋【2025-04-15（火）｜Python道場・第十五問】
# 🎯 お題："sample.csv" から、2列目の値だけを抽出してすべて表示する関数を作れ！
#
# 【条件】
# - ファイル名は "sample.csv" とする（カンマ区切りのCSV）
# - 1列目・3列目の値は無視して、2列目だけ表示すること
# - 出力はリスト形式でOK！（["B", "E", ...] のような形式）
#
# 【例】
# sample.csv の中身：
# A,B,C
# D,E,F
#
# 出力：
# ['B', 'E']

import csv
with open("2025-04-15-2-sample.csv", "r", encoding="utf-8") as f:
    lines = csv.reader(f)
    print([row[1] for row in lines])
    
with open("2025-04-15-2-sample.csv", "r", encoding="utf-8") as f:
    print([row[1] for row in csv.reader(f)])
