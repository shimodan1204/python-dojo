# 🥋【2025-05-11（日）｜Python道場・第五十一問（DictReader 条件フィルタリング＆特定の列抽出）】
# 🎯 お題：sales_data.csv を DictReader で読み込みます。
# 'Quantity' が 3 より大きく、かつ 'Region' が 'East' である全ての取引を抽出してください。
# 抽出した行から、'Product' と 'Quantity' の情報だけを含む新しい辞書のリストを作成し、表示してください。
#
# 【条件】
# - 読み取り元ファイル名：sales_data.csv (別途用意)
# - csv.DictReader() を使用すること
# - フィルタ条件: 'Quantity' が 3 より大きい AND 'Region' が 'East'
# - Quantity の値は文字列で読み込まれるため、数値比較には int() に変換が必要
# - 結果として、以下の形式のリストを作成し、print() で表示すること:
#   例: [{'Product': 'Banana', 'Quantity': 10}, {'Product': 'Orange', 'Quantity': 4}, ...]
#
# ヒント: DictReaderで読み込んだ各行（辞書）に対して if 文で条件判定を行います。
# 条件に合う行が見つかったら、その行の辞書から必要なキー ('Product', 'Quantity') だけを取り出して新しい辞書を作成し、あらかじめ用意しておいたリストに追加します。

import os
import csv

base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, "sales_data.csv")

with open(data_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    filtered_rows = [row for row in reader if int(row["Quantity"]) > 3 and row["Region"] == "East"]
    export_rows = [{"Product":row["Product"], "Quantity":row["Quantity"]} for row in filtered_rows]

print(export_rows)
