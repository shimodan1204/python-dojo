# 🥋【2025-04-06（日）｜Python道場・第一問】
# 🎯 お題：リストから偶数だけを取り出す関数を作れ！
#
# 【条件】
# - 数字の入ったリストが与えられる
# - 偶数だけを抽出して、新しいリストとして返す関数を作成すること
#
# 【入力例】
# [1, 2, 3, 4, 5, 6]
#
# 【出力例】
# [2, 4, 6]
#
# 【ヒント】
# - if文で `num % 2 == 0` を使う
# - list comprehension でも書ける


nums = [1,2,3,4,5,6]
def extract_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append( num )

    return evens
         
print( extract_evens(nums) )

def extract_evens_list_comprehension(nums):
    return [ num for num in nums if num % 2 == 0 ]

print( extract_evens_list_comprehension(nums) )
