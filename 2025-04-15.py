# 🥋【2025-04-15（火）｜Python道場・第十四問】
# 🎯 お題："sample.csv" の全行を、1から始まる行番号付きで表示する関数を作れ！
#
# 【条件】
# - ファイル名は "sample.csv" とする（任意のCSV内容でOK）
# - カンマ区切りのCSVファイルを読み込み、行単位で出力
# - 出力フォーマットは「1: ['A', 'B', 'C']」のように、リスト表示でOK！
# - 行番号は 1 から始めること
#
# 【例】
# sample.csv の中身：
# A,B,C
# D,E,F
#
# 出力：
# 1: ['A', 'B', 'C']
# 2: ['D', 'E', 'F']

import csv
with open("sample.csv", "r", newline="", encoding="utf-8") as f:
    for index, line in enumerate(csv.reader(f), start=1):
        print(f"{index}: {line}")