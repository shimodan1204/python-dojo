# 🥋【2025-04-11（金）｜Python道場・第十問】
# 🎯 お題：テキストファイルに「日付付きのメッセージ」を追記する関数を作れ！
#
# 【条件】
# - ファイル名は "log.txt" とする
# - 追記モードで書き込むこと（既存内容を消さない）
# - メッセージの前に「今日の日付（例：2025-04-11）」を付けること
# - メッセージは引数で渡されるものとする
#
# 【出力例】
# 2025-04-11: 今日のPython修行、完了！

import datetime
with open("input.txt", "a", encoding="utf-8") as f:
    date_today = datetime.date.today().isoformat()
    f.write(f"\n{date_today}: 今日のPython修行、完了！")