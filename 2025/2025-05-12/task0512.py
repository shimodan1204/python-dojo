# 🥋【2025-05-12（月）｜Python道場・第五十二問（DictReader 応用・複数条件フィルタ＆合計）】
# 🎯 お題：sales_data.csv を DictReader で読み込みます。
# 'Category' が 'Fruit' または 'Dairy' であり、かつ 'Price' が 100 より大きい全ての取引について、
# その 'Quantity' の合計を計算して表示してください。
#
# 【条件】
# - 読み取り元ファイル名：sales_data.csv (別途用意)
# - csv.DictReader() を使用すること
# - フィルタ条件: ('Category' が 'Fruit' OR 'Category' が 'Dairy') AND ('Price' が 100 より大きい)
# - Quantity と Price の値は文字列で読み込まれるため、int() に変換が必要
# - Price 列が数値に変換できない行は無視してください。（try-except を使うことを推奨）
# - 条件に合う取引の Quantity の合計を計算し、print() で表示すること
#
# ヒント: ループ内で複数の条件を組み合わせた if 文を使います。数値変換が必要な列のアクセスには try-except を挟むと安全です。条件に合う行の Quantity を合計用の変数に加算していきます。

# import csv
# import os # osモジュールが必要な場合はインポートしてください

# ファイルパスは sales_data.csv を参照するように適宜修正してください
# 例: file_path = 'sales_data.csv'
# 例: file_path = os.path.join(os.path.dirname(__file__), 'sales_data.csv')
# file_path = 'sales_data.csv' # 必要に応じて変更してください

# ここに解答コードを記述してください

import os
import csv

base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, "sales_data.csv")

Quantity_total = 0
with open(data_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Category"] == "Fruit" or row["Category"] == "Dairy":
            try:
                if int(row["Price"]) > 100:
                    try:
                        Quantity_total += int(row["Quantity"])
                    except ValueError as e:
                        print(f"TransactionID : {row["TransactionID"]} is ValueError Quantity : {row["Quantity"]}")
                        continue

            except ValueError as e:
                print(f"TransactionID : {row["TransactionID"]} is ValueError Price : {row["Price"]}")
                continue

print(Quantity_total)
