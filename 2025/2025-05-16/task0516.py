# 🥋【2025-05-16（金）｜Python道場・第五十七問（DictReader 応用・グループ化と合計集約）】
# 🎯 お題：sales_data.csv を DictReader で読み込みます。
# 'Category' ごとに、その 'Quantity' の合計を計算し、
# 結果を辞書形式で表示してください。
#
# 【条件】
# - 読み取り元ファイル名：sales_data.csv (別途用意)
# - csv.DictReader() を使用すること
# - 'Category' をキーとしてデータをグループ化する
# - 各 'Category' に属する取引の 'Quantity' の合計を計算する
# - Quantity の値は文字列で読み込まれるため、int() に変換が必要
# - Quantity 列が数値に変換できない行は無視してください。（try-except を使うことを推奨）
# - 結果を以下の形式の辞書で表示すること:
#   例: {'Fruit': 35, 'Dairy': 8, 'Bakery': 4, 'Furniture': 2}
#
# ヒント: 結果を格納するための辞書を用意します。ループ内で各行の 'Category' をキーとして使用し、そのカテゴリの合計数量を更新していきます。Quantity の数値変換には try-except を使って安全に行いましょう。

# ここに解答コードを記述してください
import os
import csv

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, "sales_data.csv")

total_quantity = {}
with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            quantity_int = int(row["Quantity"])
        except ValueError:
            print(f"TransactionID:{row.get('TransactionID', "N/A")} is Invalid quantity: {row['Quantity']}")
            continue

        total_quantity[row["Category"]] = total_quantity.get(row["Category"], 0) + quantity_int

print(total_quantity)

# total_quantity[row["Category"]] = total_quantity.get(row["Category"], 0) + int(row["Quantity"])
# 右辺にtotal_quantity.get(row["Category"], 0)を使うことで、キーが存在しない場合は0を返すようにしている。
# そのためキーの存在確認もいらなくないし、キーがなくても0を返して確実に初期化される、素晴らしい
