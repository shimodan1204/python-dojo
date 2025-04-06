# 🥋【2025-04-06（日）｜Python道場・第一問】
# 🎯 お題：リストから偶数だけを取り出す関数を作れ！

nums = [1,2,3,4,5,6]
def extarct_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append( num )

    return evens
         
print( extarct_evens(nums) )