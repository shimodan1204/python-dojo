# 🥋【2025-04-10（木）｜Python道場・第八問】
# 🎯 お題：テキストファイルから行を読み取り、「数字だけの行」をリストにして返す関数を作れ！
#
# 【条件】
# - ファイルは UTF-8 の通常テキストとする
# - 数字だけの行（空白や文字が混ざらない）が対象
# - `is○○()` 系メソッドが使いたければ使ってもOK（卒業済でも再利用可）
# - 応用として `with open()` の書き方に慣れよう！
#
# 【例】
# test.txt の中身：
# 12345
# abcde
# 67890
# 1a2b3
# 
# → 出力：['12345', '67890']

with open("test.txt", "r", encoding="utf-8") as f:
    extract_digit = []
    for line in f:
        line_strip = line.strip()
        if line_strip.isdigit():
            extract_digit.append(line_strip)
            
    print(extract_digit)
    
with open("test.txt", "r", encoding="utf-8") as f:
    print([line.strip() for line in f if line.strip().isdigit()])