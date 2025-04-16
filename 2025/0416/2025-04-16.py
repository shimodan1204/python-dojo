# 🥋【2025-04-15（火）｜Python道場・第十六問】
# 🎯 お題："sample.csv" の中から「2列目の値が 'Python'」の行だけを表示する関数を作れ！
#
# 【条件】
# - ファイル名は "sample.csv" とする（カンマ区切り）
# - 2列目（インデックス1）の値が "Python" の行だけを抽出する
# - 出力形式はリストでOK！（[['A', 'Python', 'C'], ['D', 'Python', 'F']] など）
#
# 【例】
# sample.csv の中身：
# A,Python,C
# D,Java,F
# G,Python,I
#
# 出力：
# [['A', 'Python', 'C'], ['G', 'Python', 'I']]

import csv
with open("2025-04-16-sample.csv", "r", encoding="utf-8") as f:
    print([row for row in csv.reader(f) if row[1] == "Python"])