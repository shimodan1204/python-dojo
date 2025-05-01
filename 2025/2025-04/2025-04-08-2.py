# 🥋【2025-04-08（火）｜Python道場・第五問】
# 🎯 お題：文字列の中から**小文字のアルファベットだけ**を取り出し、1つの文字列にして返す関数を作れ！
#
# 【条件】
# - 与えられた文字列には、記号や数字、大文字なども混ざっている
# - その中から **小文字の a〜z のみ** を抽出し、それらを1つの文字列として返す
#
# 【入力例】
# "Hello, World! 123 python_3.9"
#
# 【出力例】
# "elloorldpython"

import re
question = "Hello, World! 123 python_3.9"

def extract_lowerWord (text):
    pattern = r"[a-z]"
    return "".join(re.findall(pattern, text))

print(extract_lowerWord(question))