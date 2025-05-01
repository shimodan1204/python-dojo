# 🥋【2025-04-07（月）｜Python道場・第三問】
# 🎯 お題：文字列の中で「母音が出てきた位置（index）」だけを抽出する関数を作れ！
#
# 【条件】
# - 与えられた文字列の中から、母音（a, i, u, e, o）が登場する**インデックス番号のみ**を抽出し、リストで返す関数を作る
#
# 【入力例】
# "hfdhharruuriewfweurreo"
#
# 【出力例】
# [6, 7, 8, 9, 11, 14, 16, 17, 18, 20]
#
# 【ヒント】
# - enumerate() を使って index と文字のペアで取り出せ！
# - `if c in "aiueo"` で母音を判定！
# - リスト内包表記でも書ける！

arg = "hfdhharruuriewfweurreo"

def extract_aiueo (base_string):
    array = []
    for (i, t) in enumerate(base_string):
        if t in "aiueo":
            array.append(i)
            
    return array

print(extract_aiueo(arg))

def extract_aiueo (base_string):
    return [i for (i, t) in enumerate(base_string) if t in "aiueo"]

print(extract_aiueo(arg))