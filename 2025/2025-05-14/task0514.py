# 🥋【2025-05-14（水）｜Python道場・第五十五問（DictReader 応用・フィルタ＆データ加工）】
# 🎯 お題：sales_data.csv を DictReader で読み込みます。
# 'Region' が 'North' または 'South' である取引を抽出し、
# 抽出した各取引について、Product 名をすべて大文字に変換し、
# 新しい辞書のリストとして表示してください。
#
# 【条件】
# - 読み取り元ファイル名：sales_data.csv (別途用意)
# - csv.DictReader() を使用すること
# - フィルタ条件: 'Region' が 'North' または 'South'
# - 抽出した行の 'Product' の値を `.upper()` メソッドで全て大文字に変換すること
# - 結果として、変換後の 'Product' を含む辞書のリストを作成し、print() で表示すること
#   （元の行の他のキー/値は含めなくて良い）
#   例: [{'Product': 'APPLE'}, {'Product': 'MILK'}, ...]
#
# ヒント:
# ループ内で Region の条件判定を行います。
# 条件に合う行が見つかったら、その行の 'Product' の値を取り出し、.upper() で変換します。
# 変換した値を新しい辞書に格納し、リストに追加していきます。

# ここに解答コードを記述してください
import csv
import os

base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, "sales_data.csv")

matched_rows = []
with open(data_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Region"] in ("North", "South"):
            matched_rows.append({
                "Product" : row["Product"].upper()
            })

print(matched_rows)
