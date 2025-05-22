# 【綾奈からの挑戦状・第二問】複数CSVファイルの関連付けと分析

# 🎯 お題：
# あなたは小規模な書店のデータを分析しています。
# `books.csv` と `sales.csv` の2つのファイルがあります。
# これらの情報を使って、カテゴリごとの総販売冊数と、最も売れた本（販売冊数基準）を特定し、`category_summary.csv` に出力してください。

# 【条件】
# 1.  `csv.DictReader` を使って両方のCSVファイルを読み込みます。
# 2.  まず、`sales.csv` から `book_id` ごとの総販売冊数を集計します。`quantity_sold` が数値に変換できないデータは無視し、ログファイル `sales_error_log.txt` に `sale_id` とエラー内容を記録してください。
# 3.  次に、`books.csv` の情報と上記集計結果を `book_id` をキーにして関連付け、各本のカテゴリと総販売冊数を把握します。
# 4.  カテゴリごとに総販売冊数を計算します。
# 5.  カテゴリごとに最も販売冊数が多かった本のタイトルとその販売冊数を特定します。（もし販売冊数が同じ場合は、どちらか一方を選んで構いません）
# 6.  結果を `category_summary.csv` に書き出します。ヘッダーは `category,total_quantity_sold,top_selling_book_title,top_book_quantity` としてください。

# 【出力 `category_summary.csv` の例】
# (S009のquantity_soldは不正。B006はsalesにはあるが、books.csvのpriceがエラーだが、この問題ではpriceは直接使わない。ここではquantity_soldのみ考慮)
# category,total_quantity_sold,top_selling_book_title,top_book_quantity
# プログラミング,10,Python入門,8
# 料理,13,お菓子作りの秘訣,6
# 小説,10,すごいSF小説,7

# 【出力 `sales_error_log.txt` の例】
# sale_id S009 の quantity_sold が不正です: ABC

# 【ヒント】
# * 本の情報を格納するために、`book_id` をキーとした辞書を作ると、販売データとの紐付けがしやすいです。
# * カテゴリごとの集計や、カテゴリ内で最も売れた本を見つけるために、ループ処理と条件分岐をうまく使いましょう。
# * デフォルト値を扱える `collections.defaultdict` も集計に便利かもしれません。

# sales.csvのエラー処理について
# `quantity_sold` が数値に変換できないデータは無視し、ログファイル `sales_error_log.txt` に `sale_id` とエラー内容を記録してください。


import os
import csv
from collections import defaultdict

BOOKS_FILE = "books.csv"
SALES_FILE = "sales.csv"
BOOKS_ERROR_LOG_FILE = "books_error_log.txt"
SALES_ERROR_LOG_FILE = "sales_error_log.txt"
CATEGORY_SUMMARY_FILE = "category_summary.csv"

dir_path = os.path.dirname(os.path.abspath(__file__))
books_csv_path = os.path.join(dir_path, BOOKS_FILE)
sales_csv_path = os.path.join(dir_path, SALES_FILE)
sales_error_log_path = os.path.join(dir_path, SALES_ERROR_LOG_FILE)
books_error_log_path = os.path.join(dir_path, BOOKS_ERROR_LOG_FILE)
category_summary_path = os.path.join(dir_path, CATEGORY_SUMMARY_FILE)

def check_quantity_sold(quantity_sold):
    try:
        return int(quantity_sold)
    except ValueError:
        return None

def create_error_message(unique_id, field_key, field_value):
    return f"{unique_id} の {field_key} が不正です: {field_value}"

def check_and_separate_sales_data(sales_data):
    valid_sales_records = []
    error_messages = []
    for sale in sales_data:
        quantity_int_or_none = check_quantity_sold(sale.get("quantity_sold"))
        if quantity_int_or_none is None:
            error_message = create_error_message(sale.get("sale_id", "N/A"), "quantity_sold", sale.get("quantity_sold"))
            error_messages.append(error_message)
        else:
            valid_sales_records.append(sale)

    return {
        "valid_sales_records": valid_sales_records,
        "error_messages": error_messages
    }

def create_books_master(books_csv_path):
    with open(books_csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        books_data = list(reader)
        books_master = {book["book_id"]:book for book in books_data if book.get("book_id")}
    return books_master

def create_sales_data(sales_csv_path):
    with open(sales_csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        sales_data = list(reader)
    return sales_data

def sum_book_quantities_sold(sales_data):
    books_quantities_sold = defaultdict(int)
    for sale in sales_data:
        book_id = sale.get("book_id", "N/A")
        quantity_sold = sale.get("quantity_sold")
        quantity_sold_int = check_quantity_sold(quantity_sold)

        # defaultdictでキーが無い場合自動的に0になるため、+=だけで処理できる
        books_quantities_sold[book_id] += quantity_sold_int
    return books_quantities_sold

def sum_category_quantities_sold(books_master, books_quantities_sold):
    category_quantities_sold = {}
    for book_id, quantity_sold in books_quantities_sold.items():
        book = books_master[book_id]
        category = book["category"]
        category_quantities_sold[category] = category_quantities_sold.get(category, 0) + quantity_sold
    return category_quantities_sold

def extract_top_selling_books(books_master, books_quantities_sold):
    top_selling_books = defaultdict(lambda: {"top_selling_book_title": "", "top_book_quantity": -1})
    for book_id, book_quantity in books_quantities_sold.items():
        book = books_master[book_id]
        book_category = book["category"]
        book_title = book["title"]
        if top_selling_books[book_category]["top_book_quantity"] < book_quantity:
            top_selling_books[book_category]["top_selling_book_title"] = book_title
            top_selling_books[book_category]["top_book_quantity"] = book_quantity
    return top_selling_books

def create_category_summary(category_quantities_sold, category_top_selling_books):
    category_summary = []
    for category, top_selling_book in category_top_selling_books.items():
        category_summary.append({
            "category": category,
            "total_quantity_sold": int(category_quantities_sold[category]),
            "top_selling_book_title": top_selling_book.get("top_selling_book_title"),
            "top_book_quantity": top_selling_book.get("top_book_quantity", 0)
        })
    return category_summary

def debug_print(dic):
    for key, value in dic.items():
        print(key, value)

# books.csvをマスターデータに変換する
books_master = create_books_master(books_csv_path)

# sales.csvをマスターデータに変換する
sales_data = create_sales_data(sales_csv_path)

# sales.csvのquantity_soldをチェックする
invalid_sales_quantity_sold = check_and_separate_sales_data(sales_data)

# sales.csvから有効なデータと無効なデータを取り出す
valid_sales_records = invalid_sales_quantity_sold.get("valid_sales_records", [])
error_messages = invalid_sales_quantity_sold.get("error_messages", [])

# sales.csvのquantity_soldnにエラーがあればログファイルに書き出す
if error_messages:
    with open(sales_error_log_path, "w") as f:
        for error_message in error_messages:
            f.write(error_message + "\n")

# 本の販売数を集計する
books_quantities_sold = sum_book_quantities_sold(valid_sales_records)

# カテゴリ単位で販売数を集計する
category_quantities_sold = sum_category_quantities_sold(books_master, books_quantities_sold)

# カテゴリ単位でトップセールス本を抽出する
category_top_selling_books = extract_top_selling_books(books_master, books_quantities_sold)

# カテゴリ単位で販売数とトップセールス本の情報を結合する
category_summary = create_category_summary(category_quantities_sold, category_top_selling_books)

# カテゴリ単位で販売数をソートする
category_summary_soted = sorted(category_summary, key=lambda x: x["total_quantity_sold"], reverse=True)

# カテゴリ単位で販売数とトップセールス本の情報を書き出す
with open(category_summary_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["category", "total_quantity_sold", "top_selling_book_title", "top_book_quantity"])
    writer.writeheader()
    writer.writerows(category_summary_soted)
