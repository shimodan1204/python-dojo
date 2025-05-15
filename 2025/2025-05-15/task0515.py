# 🥋【2025-05-15（木）｜Python道場・第五十六問（DictReader 応用・複数日付フィルタと合計）】
# 🎯 お題：sales_data.csv を DictReader で読み込みます。
# 'Date' が '2023-03-01' から '2023-04-30' までの期間に含まれる全ての取引について、
# その 'Price' の合計を計算して表示してください。
#
# 【条件】
# - 読み取り元ファイル名：sales_data.csv (別途用意)
# - csv.DictReader() を使用すること
# - フィルタ条件: 'Date' が '2023-03-01' 以上 AND '2023-04-30' 以下
# - Price の値は文字列で読み込まれるため、int() に変換が必要
# - Date の比較は文字列として行っても、datetimeオブジェクトに変換して行っても構いません。
# - Price 列が数値に変換できない行は無視してください。（try-except を使うことを推奨）
# - 条件に合う取引の Price の合計を計算し、print() で表示すること
#
# ヒント: 日付文字列の範囲比較は、Y-M-D形式であれば通常の文字列比較演算子（>=, <=など）を組み合わせて行うことができます。Price の数値変換が必要な箇所には try-except を挟むと安全です。合計用の変数を用意し、ループ内で条件に合う行の Price を加算していきます。

# ここに解答コードを記述してください
import os
import csv
from datetime import datetime
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, "sales_data.csv")

min_date = "2023-03-01"
max_date = "2023-04-30"
total_price = 0

def is_valid_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        return None

def is_valid_price(price_str):
    try:
        return int(price_str)
    except ValueError:
        return None

def print_invalid_transaction(transaction_id, field, value):
    print(f"TransactionID: {transaction_id} Invalid {field} format: {value}")

with open(file_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        current_date = is_valid_date(row.get("Date"))
        if current_date:
            if current_date and min_date <= current_date and current_date <= max_date:
                price_int = is_valid_price(row.get("Price"))
                if price_int:
                    print(price_int)
                    total_price += price_int
                else:
                    print_invalid_transaction(row.get("TransactionID", "N/A"), "Price", row.get("Price"))

        else:
            print_invalid_transaction(row.get("TransactionID", "N/A"), "Date", row.get("Date"))
            continue

print(total_price)
