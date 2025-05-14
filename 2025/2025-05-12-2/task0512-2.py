# 🥋【2025-05-12（月）｜Python道場・第五十三問（DictReader 応用・日付フィルタと集計）】
# 🎯 お題：sales_data.csv を DictReader で読み込みます。
# 'Date' が '2023-04-01' 以降の取引について、
# その 'Price' の合計を計算して表示してください。
#
# 【条件】
# - 読み取り元ファイル名：sales_data.csv (別途用意)
# - csv.DictReader() を使用すること
# - フィルタ条件: 'Date' が '2023-04-01' 以降
# - Price の値は文字列で読み込まれるため、int() に変換が必要
# - Date の比較は文字列として行っても、datetimeオブジェクトに変換して行っても構いません。
# - Price 列が数値に変換できない行は無視してください。（try-except を使うことを推奨）
# - 条件に合う取引の Price の合計を計算し、print() で表示すること
#
# ヒント:
# 日付文字列の比較は、Y-M-D形式であれば通常の文字列比較演算子（>=など）で行うことができます。
# より厳密な日付処理には datetime モジュールが使えます。
# 合計用の変数を用意し、ループ内で条件に合う行の Price を安全に（try-exceptを使って）加算していきます。

# ここに解答コードを記述してください

import os
import csv
import datetime

base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, "sales_data.csv")

price_total = 0
with open(data_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row_date_str = row.get("Date")
        if row_date_str and "2023-04-01" <= row_date_str:
            try:
                row_price = int(row.get("Price","0"))
                price_total += int(row_price)
            except ValueError:
                print(f"TransactionID : {row["TransactionID"]} is ValueError Price : {row["Price"]}")
                continue

print(price_total)
