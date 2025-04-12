# 🥋【2025-04-12（土）｜Python道場・第十一問】
# 🎯 お題：テキストファイルから、特定のキーワードを含む行だけを抽出して表示する関数を作れ！
#
# 【条件】
# - ファイル名は "log.txt" とする（自分で用意してもOK！）
# - 引数で渡された文字列を含む行だけを抽出し、リストで返すこと
# - 大文字・小文字の違いは区別しなくてよい（＝どちらでもヒットするように）
#
# 【例】
# log.txt の中身：
# 2025-04-11: 今日のPython修行、完了！
# 2025-04-12: 今日のJS修行、完了！
#
# extract_keyword_lines("python") → ["2025-04-11: 今日のPython修行、完了！"]

def extract_keyword_lines(file_path, keyword):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if keyword in line.strip().lower()]

matchlines = extract_keyword_lines("log.txt", "python")
print(matchlines)
