# 🥋【2025-04-13（日）｜Python道場・第十二問】
# 🎯 お題：テキストファイルの全行を読み込み、各行に「行番号」をつけて表示する関数を作れ！
#
# 【条件】
# - ファイル名は "log.txt" とする（内容は任意）
# - 各行に対して「1行目から」順に番号を付けて表示
# - 出力フォーマットは `"1: ○○○○"` のように、コロン+スペースで区切ること
#
# 【例】
# log.txt の中身：
# Hello
# World
#
# 出力：
# 1: Hello
# 2: World


with open("log.txt", "r",encoding="utf-8") as f:
    lines = f.readlines()
    for (index, line) in enumerate(lines):
        print(f"{index+1}: {line.strip()}")

with open("log.txt", "r",encoding="utf-8") as f:
    for (index, line) in enumerate(f, start=1):
        print(f"{index}: {line.strip()}")
