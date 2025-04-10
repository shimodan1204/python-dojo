# 🥋【2025-04-10（木）｜Python道場・第七問】
# 🎯 お題：文字列の中から「数字だけ」を取り出して、新しい文字列として返す関数を作れ！
#
# 【条件】
# - 0〜9の数字だけを対象とする
# - 記号・スペース・英字・漢字などは除外
# - `is○○()` 系メソッドを使って実装すること！
#
# 【入力例】
# "TEL: 03-1234-5678 / 内線: 999"
#
# 【出力例】
# "0312345678999"

base_string = "TEL: 03-1234-5678 / 内線: 999 １２３４"

# 半角のみ + 通常
def extract_digit_hannum (string):
    hankana = ""
    for t in string:
        if t.isdigit() and t.isascii():
            hankana += t
            
    return hankana

# 半角のみ + 内包表記
print(extract_digit_hannum(base_string))

def extract_digit_hannum (string):
    return "".join([t for t in string if t.isdigit() and t.isascii()])

print(extract_digit_hannum(base_string))

# 半角 + 全角 + 通常
def extract_digit_hannum_zennum (string):
    hankana_zenkana = ""
    for t in string:
        if t.isdigit():
            hankana_zenkana += t
            
    return hankana_zenkana

print(extract_digit_hannum_zennum(base_string))

# 半角 + 全角 + 内包表記
def extract_digit_hannum_zennum (string):
    return "".join([t for t in string if t.isdigit()])

print(extract_digit_hannum_zennum(base_string))