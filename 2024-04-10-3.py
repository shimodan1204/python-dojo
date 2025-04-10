# 🥋【2025-04-10（木）｜Python道場・第九問】
# 🎯 お題：テキストファイルから全行を読み取り、逆順にして別ファイルに書き出す関数を作れ！
#
# 【条件】
# - 読み込むファイルは UTF-8 の通常テキストファイルとする
# - 書き出しファイルは "output.txt" という名前でOK
# - 空行もそのまま含めてOK
# - 行末の改行は維持しても消してもOK（おまかせ！）
#
# 【例】
# input.txt の中身：
# A
# B
# C
#
# → 出力：output.txt の中身
# C
# B
# A

# inputs = []
with open("input.txt", "r", encoding="utf-8") as f:
    inputs = [line.strip() for line in f.readlines()]
    inputs.reverse()
    
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(inputs))