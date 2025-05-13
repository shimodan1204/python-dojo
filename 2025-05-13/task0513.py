# 🥋【2025-05-14（水）｜Python道場・第五十四問（DictReader 応用・フィルタリングとカウント集約）】
# 🎯 お題：sales_data.csv を DictReader で読み込みます。
# 'Category' が 'Fruit' であり、かつ 'Quantity' が 5 以上の全ての取引について、
# その数をカウントして表示してください。
#
# 【条件】
# - 読み取り元ファイル名：sales_data.csv (別途用意)
# - csv.DictReader() を使用すること
# - フィルタ条件: 'Category' が 'Fruit' AND 'Quantity' が 5 以上
# - Quantity の値は文字列で読み込まれるため、数値比較には int() に変換が必要
# - Quantity 列が数値に変換できない行は無視してください。（try-except を使うことを推奨）
# - 条件に合う取引の数をカウントし、print() で表示すること
#
# ヒント:
# カウント用の変数を用意し、ループ内で条件に合う行が見つかるたびにその変数を増やします。
# Quantity の数値変換には try-except を使って安全に行いましょう。

import os
import csv

base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, "sales_data.csv")

filtered_match_count = 0
with open(data_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row_category = row.get("Category")
        try:
            row_quantity = int(row.get("Quantity", "0"))
        except ValueError:
            print(f"TransactionID : {row.get("TransactionID", "N/A")}  Quantity is ValueError {row.get("Quantity")}")
            continue

        if row_category == "Fruit" and row_quantity > 5:
            filtered_match_count += 1

print(filtered_match_count)
