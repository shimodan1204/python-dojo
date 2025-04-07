# 🥋【2025-04-07（月）｜Python道場・第二問】
# 🎯 お題：文字列から母音だけを取り出す関数を作れ！
#
# 【条件】
# - 英単語などの文字列が与えられる
# - 母音（a, i, u, e, o）の文字だけを取り出し、リストで返す関数を作成する
#
# 【入力例】
# "chatgpt"
#
# 【出力例】
# ['a']
#
# 【ヒント】
# - 文字列は1文字ずつ for 文で取り出せる
# - `if c in 'aiueo'` を使えば母音判定できる
# - list comprehension（リスト内包表記）でも書ける

arg = "hfdhharruuriewfweurreo"

def extract_aiueo (base_string):
    array = []
    for t in base_string:
        if t in "aiueo":
            array.append(t)

    return array

print( extract_aiueo( arg ) )

def extract_aiueo (base_string):
    return [ t for t in base_string if t in "aiueo" ]

print( extract_aiueo( arg ) )

def extract_aiueo (base_string):
    return [ (i, t) for (i, t) in enumerate(base_string) if t in "aiueo" ]

print( extract_aiueo( arg ) )
