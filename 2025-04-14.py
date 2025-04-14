# 🥋【2025-04-14（月）｜Python道場・第十三問】
# 🎯 お題："input.txt" から数字だけの行を抽出し、"output.txt" に書き出す関数を作れ！
#
# 【条件】
# - "input.txt" には、数字の行・文字列の行・混合行が含まれている
# - 数字だけの行（例："12345"）を抽出対象とする
# - 行末の改行は適切に処理し、"output.txt" に改行付きで保存すること
# - 書き出しファイルは `"w"` モード（上書き）
#
# 【例】
# input.txt：
# Hello
# 12345
# 67890
# こんにちは
#
# → output.txt：
# 12345
# 67890

# ファイルを開く
# 行に分割する
# forで回す
#     改行消す
#     行が数字だけか判定
#         数字だけなら書き出し変数に追記
        
# 文字列長さを確認
#     0じゃなければoutput.txtに書き出す

with open("2025-14-14-input.txt", "r", encoding="utf-8") as f:
    result = []
    lines = f.readlines()
    for line in lines:
        if line.strip().isdigit():
            result.append(line.strip())
            
if len(result) > 0:
    with open("2025-04-14-output_standart.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(result))
        

with open("2025-14-14-input.txt", "r", encoding="utf-8") as f:
    result = "\n".join([line.strip() for line in f.readlines() if line.strip().isdigit()])

if len(result) > 0:
    with open("2025-04-14-output_listin.txt", "w", encoding="utf-8") as f:
        f.write(result)