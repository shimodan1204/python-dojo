# 🥋【2025-04-20（日）｜Python道場・第二十四問】
# 🎯 お題："sample.csv" の中から、
#     2列目に "Python" を含む行だけを "filtered.csv" に出力せよ！
#     また、ユーザーが「追記」or「上書き」を選べるようにせよ！
#
# 【条件】
# - 入力ファイル名："sample.csv"
# - 出力ファイル名："filtered.csv"
# - 書き込みモードは "w"（上書き） or "a"（追記）を選択可能にすること
# - "Python" を含むかの判定は部分一致 + 大文字小文字無視
# - `input()` を使って `"追記しますか？ (y/n)"` みたいに聞いてもよい！
# - 出力形式は CSV形式でOK（`",".join(row)` または `writer.writerow(row)`）

import os, csv

base_dir = os.path.dirname(__file__)
sample_path = os.path.join(base_dir, "sample.csv")
filtered_path = os.path.join(base_dir, "filtered.csv")

# CSV読み込み
with open(sample_path, "r", encoding="utf-8") as f:
    extract_rows = [row for row in csv.reader(f) if "python" in row[1].lower()]
    print(extract_rows)
    
# 書き込みモード選択
select = input("追記しますか？(y/n)")
if select == "y":
    write_mode = "a"
elif select == "n":
    write_mode = "w"
else:
    print("選択が正しくありません")
    
# CSV書き出し
with open(filtered_path, write_mode, newline="", encoding="utf-8") as f:
    for row in extract_rows:
        f.write(f"{",".join(row)}\n")