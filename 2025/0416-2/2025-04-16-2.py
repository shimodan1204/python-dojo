# 🥋【2025-04-15（火）｜Python道場・第十七問】
# 🎯 お題："sample.csv" から「2列目が 'Python' の行」だけを抽出し、
#     "python_only.csv" に書き出す関数を作れ！
#
# 【条件】
# - ファイル名："sample.csv"（読み取り元）・"python_only.csv"（書き出し先）
# - 2列目（インデックス1）が "Python" の行だけを抽出
# - 出力ファイルも **カンマ区切り形式（CSV）** にする
# - 書き出しは上書き（"w"モード）とする
#
# 【例】
# sample.csv の中身：
# A,Python,C
# D,Java,F
# G,Python,I
#
# → python_only.csv に出力される内容：
# A,Python,C
# G,Python,I

import csv
with open("2025-04-16-2-sample.csv", "r", encoding="utf-8") as f:
    matches = [row for row in csv.reader(f) if row[1] =="Python"]
    
with open("2025-04-16-python_only.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for match in matches:
        writer.writerow(match)
        
with open("2025-04-16-python_only.csv", "r", encoding="utf-8") as f:
    print(f.read())