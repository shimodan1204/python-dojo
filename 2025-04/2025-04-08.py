# 🥋【2025-04-08（火）｜Python道場・第四問】
# 🎯 お題：整数のリストから、偶数だけを2倍にして返す関数を作れ！
#
# 【条件】
# - 与えられた整数リストのうち、偶数は2倍、奇数は無視する
# - 処理後の新しいリストを返す関数を定義すること
#
# 【入力例】
# [1, 2, 3, 4, 5]
#
# 【出力例】
# [4, 8]

nums = [1, 2, 3, 4, 5]

def extract_baipush (nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num * 2)
            
    return evens

print(extract_baipush(nums))


def extract_baipush (nums):
    return [num*2 for num in nums if num % 2 == 0]

print(extract_baipush(nums))