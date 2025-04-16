# 🥋【2025-04-09（水）｜Python道場・第六問】
# 🎯 お題：文字列の中から「英数字だけ」を取り出して、ひとつの文字列として返す関数を作れ！
#
# 【条件】
# - アルファベット（a〜z、A〜Z）と数字（0〜9）だけを対象とする
# - 記号やスペースなどはすべて除外
# - `is○○()` 系メソッドを使って実装すること！
#
# 【入力例】
# "Hello, Python3.9! 2025年"
#
# 【出力例】
# "HelloPython392025"

base_string = "Hello, Python3.9! 2025年"

def extract_alpha_and_num(text):
    extract_text = ""
    for t in text:
        if t.isalnum() and t.isascii():
            extract_text += t

    return extract_text

print(extract_alpha_and_num(base_string))

def extract_alpha_and_num(text):
    return "".join([t for t in text if t.isalnum() and t.isascii()])

print(extract_alpha_and_num(base_string))