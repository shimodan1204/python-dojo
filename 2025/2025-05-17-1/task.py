# 🎯 お題：
# ECサイトの注文履歴がJSONファイル（orders.json）に保存されています。
# このファイルから顧客ごとの合計注文金額を計算し、結果を新しいCSVファイル（customer_revenue.csv）に出力してください。

# 【orders.json のサンプルデータ形式】
# (この内容で orders.json ファイルを作成して使ってください)

# 【条件】
# 1.  `json` モジュールを使って `orders.json` を読み込みます。
# 2.  各注文について、`items` リスト内の各商品の `price` と `quantity` を掛け合わせて小計を出し、注文全体の合計金額を計算します。
# 3.  顧客ID (`customer_id`) ごとに、その顧客の全注文の合計金額を集計します。
# 4.  集計結果を `customer_revenue.csv` に書き出します。CSVのヘッダーは `customer_id,total_revenue` としてください。
# 5.  もし `price` や `quantity` が数値に変換できないような不正なデータがあった場合は、エラーログ（例えば `error_log.txt`）に注文IDとその理由を記録し、そのアイテムの計算はスキップしてください（`try-except`を活用しましょう）。

# 【出力 `customer_revenue.csv` の例】
# (ORD004 は price が不正なため、CUST300 の revenue は 0 または記録なし、エラーログに出力)
# customer_id,total_revenue
# CUST100,26000
# CUST200,8000

# 【出力 `error_log.txt` の例】
# 注文ID ORD004 のアイテム「タブレット」のpriceが不正です: 不明

# 【ヒント】
# * ネストしたデータ構造の扱いに注意してください。
# * 顧客ごとの合計金額を保持するために、辞書を使うと便利かもしれません。
# * `json.load()` または `json.loads()` でJSONデータをPythonの辞書やリストに変換できます。

import os
import csv
import json

# エラーメッセージ生成
def create_error_message(order_id, product_name, field_name, value):
    return f"エラー: 項目「{field_name}」の値「{value}」は無効です。(注文ID: {order_id}, 商品: {product_name})"

# 数値の有効性判定
def is_valid_number(value):
    try:
        value_int = int(value)
        return value_int
    except ValueError:
        return None

dirname = os.path.dirname(__file__)
orders_path = os.path.join(dirname, "orders.json")
output_path = os.path.join(dirname, "customer_revenue.csv")
error_log_path = os.path.join(dirname, "error_log.txt")

# 読み込み
with open(orders_path, "r", encoding="utf-8") as file:
    orders = json.load(file)

# jsonを回してレコードを取り出す
customer_revenue = {}
error_log = []
for order in orders:
    # レコードからitemsを取り出す
    product_revenue_total = 0
    for item in order["items"]:
        # priceの有効性チェック
        price_str = item.get("price")
        price_int = is_valid_number(price_str)
        if not price_int:
            error_message = create_error_message(order.get('order_id', 'N/A'), item.get('product_name', 'N/A'), 'price', item.get('price', 'N/A'))
            error_log.append(error_message)

        # quantityの有効性チェック
        quantity_str = item.get("quantity")
        quantity_int = is_valid_number(quantity_str)
        if not quantity_int:
            error_message = create_error_message(order.get('order_id', 'N/A'), item.get('product_name', 'N/A'), 'quantity', item.get('quantity', 'N/A'))
            error_log.append(error_message)

        # priceとquantityがどちらか無効ならcontinue
        if not price_int or not quantity_int:
            continue

        # 総額を算出
        product_revenue = price_int * quantity_int
        product_revenue_total += product_revenue

    customer_id = order.get('customer_id', 'N/A')
    customer_revenue[customer_id] = customer_revenue.get(customer_id, 0) + product_revenue_total

# 合計額を出力
with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["customer_id", "total_revenue"])
    writer.writeheader()
    for customer_id, total_revenue in customer_revenue.items():
        writer.writerow({"customer_id": customer_id, "total_revenue": total_revenue})

# エラーログを出力
if error_log:
    with open(error_log_path, "w", newline="", encoding="utf-8") as file:
        for error_message in error_log:
            file.write(error_message + "\n")

    print(f"取得エラーが {len(error_log)} 件発生しました。エラーログを参照してください。")

# jsonを回してレコードを取り出す
#     レコードからitemsを取り出す
#         itemsを回してitemを取り出す
#         item内のpriceの有効性をチェック
#         item内のquantityの有効性をチェック
#         item内のpriceとquantityを掛ける = ここではitem_totalとする
#         item_totalを合計する = item_total_sum　とする
#             集計配列にcustomer_id：item_total_sumを追加する
