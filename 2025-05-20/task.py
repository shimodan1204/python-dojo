# 👩‍💻【綾奈からの挑戦状・第三問】複数条件でのデータ集計とランキング表示
# 🎯 お題：
# とあるオンラインコースの受講データ (enrollments.csv) と、各コースのカテゴリ情報 (courses.csv) があります。これらのデータを使って、以下の情報を集計・分析し、結果をテキストファイル (course_report.txt) にレポート形式で出力してください。

# 【enrollments.csv のサンプルデータ形式】

# enrollment_id,user_id,course_id,enrollment_date,completion_status,grade
# E001,U100,C01,2024-01-15,completed,85
# E002,U101,C02,2024-01-20,in_progress,
# E003,U100,C03,2024-02-01,completed,92
# E004,U102,C01,2024-02-05,completed,78
# E005,U103,C04,2024-02-10,not_started,
# E006,U101,C01,2024-03-01,completed,90
# E007,U104,C02,2024-03-05,completed,
# E008,U100,C02,2024-03-10,in_progress,
# E009,U105,C03,2024-03-15,completed,88
# E010,U102,C04,2024-04-01,completed,95
# E011,U106,C01,2024-04-05,failed,45
# E012,U107,C05,2024-04-10,completed,80
# E013,U108,C01,2024-01-18,completed,A+
# E014,U109,C02,2024-02-20,completed,
# E015,U110,C03,2024-03-01,in_progress,B

# (grade列は、完了(completed)の場合に数値または文字評価、それ以外は空欄または存在しない場合があります。また、数値でない評価も混ざっています)

# 【courses.csv のサンプルデータ形式】

# course_id,course_name,category,difficulty_level
# C01,Python入門,プログラミング,初級
# C02,データ分析基礎,データサイエンス,中級
# C03,Webデザインの基本,デザイン,初級
# C04,機械学習実践,データサイエンス,上級
# C05,JavaScript集中講座,プログラミング,中級

# 【レポート (course_report.txt) の出力形式と内容】

# コース分析レポート (YYYY-MM-DD作成)  // YYYY-MM-DD はレポート生成日

# --- カテゴリ別 受講完了者数ランキング ---
# 1. プログラミング: XX人
# 2. データサイエンス: YY人
# 3. デザイン: ZZ人
#    :

# --- カテゴリ別 平均評点 (数値評価のみ対象) ---
# プログラミング: 平均 XX.X 点 (対象者数: N人)
# データサイエンス: 平均 YY.Y 点 (対象者数: M人)
# デザイン: 平均 ZZ.Z 点 (対象者数: P人)
#    :
# (評点が数値でない、または空欄の受講者は平均点計算の対象外とします。対象者数が0の場合は「該当なし」と表示)

# --- 人気コースランキング (受講者数トップ3) ---
# 1. コース名A (カテゴリA): 受講者数 X人
# 2. コース名B (カテゴリB): 受講者数 Y人
# 3. コース名C (カテゴリC): 受講者数 Z人

# --- 特別優秀者リスト (評点が95点以上、または評価が「A+」の完了者) ---
# - ユーザーID (コース名): 評価/評点
#   例: U102 (機械学習実践): 95
#   例: U108 (Python入門): A+
#    :
# (該当者がいない場合は「該当者なし」と表示)

# 【条件】

# csv.DictReader を使用して両方のCSVファイルを読み込みます。

# カテゴリ別 受講完了者数ランキング：
# enrollments.csv の completion_status が "completed" の受講者をカウントします。
# courses.csv の情報と紐付けて、カテゴリごとに集計し、受講完了者数が多い順にランキング形式で表示します。

# カテゴリ別 平均評点：
# completion_status が "completed" で、かつ grade が数値として有効な受講者のみを対象とします。
# カテゴリごとに平均評点を計算し、小数点以下1桁まで表示します。平均評点の計算対象となった受講者数も併記してください。
# grade が空欄、または数値に変換できない文字列（例: "B"）の場合は、平均点の計算から除外します。
# もし、あるカテゴリで数値評価の完了者がいない場合は、「該当なし」と表示します。

# 人気コースランキング：
# enrollments.csv の全受講記録から、コースごとの総受講者数（completion_status によらず）を集計します。
# 受講者数が多い順にトップ3のコース名、そのカテゴリ、受講者数を表示します。

# 特別優秀者リスト：
# completion_status が "completed" で、かつ以下のいずれかの条件を満たす受講者をリストアップします。
# grade が数値で95点以上。
# grade が文字列で "A+"。
# リストには、ユーザーID、受講したコース名（courses.csv から取得）、その評価/評点を表示します。
# 該当者がいない場合は「該当者なし」と表示します。
# レポートの先頭には、レポート生成日（スクリプト実行日）を「YYYY-MM-DD作成」の形式で記載してください（datetimeモジュールが使えますね！）。
# grade の数値変換エラーなど、データの不整合が処理の妨げにならないように、適切にエラーハンドリング（try-exceptなど）を行ってください。ただし、今回はエラーログファイルへの出力は必須ではありません（コンソールに警告を出す程度でOKです）。
# 【ヒント】

# まず、courses.csv の情報を course_id をキーにした辞書に格納しておくと、enrollments.csv の処理中にコース情報を参照しやすくなります。
# 各集計は、それぞれ別の関数に分けて実装すると、コードの見通しが良くなります。
# ランキング表示の際は、Pythonの sorted() 関数やリストの sort() メソッドが役立ちます。lambda 式を使ったソートキーの指定も活用しましょう。
# 平均点を計算する際は、合計点と対象者数をそれぞれ保持しておくと良いでしょう。ゼロ除算エラーに注意してください。
# テキストファイルへの書き出しは、with open(..., "w", encoding="utf-8") as f: と f.write() を使います。

# 今回の問題は、前回までのファイル操作やデータ集計に加えて、複数の条件での絞り込み、ランキング作成、そしてレポート形式での出力、と少しステップが増えています。
# 特に「カテゴリ別平均評点」の数値評価のみを対象とする部分や、「特別優秀者リスト」の複数条件の判定がポイントになるかもしれません。

# 焦らず、一つ一つの集計項目をどうやって実現できるか、ステップごとに考えてみてくださいね。

import os
import csv
from datetime import datetime
from collections import defaultdict

# 定数の設定
ENROLLMENTS_FILE = "enrollments.csv"
COURSES_FILE = "courses.csv"
REPORT_FILE = "course_report.txt"

# ファイルパスの設定
base_dir = os.path.dirname(os.path.abspath(__file__))
enrollments_file = os.path.join(base_dir, ENROLLMENTS_FILE)
courses_file = os.path.join(base_dir, COURSES_FILE)
report_file = os.path.join(base_dir, REPORT_FILE)

# 1．courses.csvの読み込み: course_id をキーにした辞書に格納
courses = {}
with open(courses_file, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        course_id = row.get("course_id")
        course_name = row.get("course_name")
        category = row.get("category")
        if course_id and course_name and category:
            courses[course_id] = row

# 2．enrollments.csvの読み込み: 配列に格納
enrollments = []
with open(enrollments_file, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        user_id = row.get("user_id")
        course_id = row.get("course_id")
        completion_status = row.get("completion_status")
        if user_id and course_id and completion_status and course_id in courses:
            enrollments.append(row)

# ルックアップテーブルのテスト
for row in enrollments:
    course_id = row["course_id"]
    if course_id in courses:
        print(courses[course_id])
    else:
        print(f"course_id {course_id} not found")

# 3．enrollments.csv と courses.csv の結合：　結合は不要、ルックアップテーブルで対応

# 4．カテゴリ別 受講完了者数ランキングの算出
def extract_completed_users(enrollments):
    """
    受講完了ユーザーを抽出
    """
    completed_users = []
    for row in enrollments:
        completion_status = row["completion_status"]
        if completion_status == "completed":
            completed_users.append(row)
    return completed_users

def add_category_to_completed_users(completed_users,courses):
    """
    受講完了ユーザーにcourses.csvのcategoryを追加
    """
    for row in completed_users:
        course_id = row["course_id"]
        if course_id in courses:
            row["category"] = courses[course_id]["category"]
    return completed_users

def get_category_completed_count(enrollments):
    """
    カテゴリ別 受講完了者数の算出
    """
    category_completed_count = defaultdict(int)
    for row in enrollments:
        category = row["category"]
        category_completed_count[category] += 1
    return category_completed_count

def sort_category_completed_count(category_completed_count):
    """
    カテゴリ別 受講完了者数のソート
    """
    return sorted(category_completed_count.items(),key=lambda x:x[1],reverse=True)

def get_category_ranking(enrollments,courses):
    """
    カテゴリ別 受講完了者数ランキングの算出
    """
    # enrollmentsからcompletion_status=completedユーザーを抽出
    completed_users = extract_completed_users(enrollments)

    # 抽出したユーザーにcoursesを結合、category列を追加
    completed_users_with_category = add_category_to_completed_users(completed_users,courses)

    # 結合したデータからcategoryで分類ししてそれぞれカウント
    category_completed_count = get_category_completed_count(completed_users_with_category)

    # category_completedをsort、人数順降順にする
    sorted_category_completed_count = sort_category_completed_count(category_completed_count)

    return sorted_category_completed_count

# 5．カテゴリ別 平均評点の算出
def is_numeric_grade(grade):
    """
    数値評点かどうかを確認
    """
    try:
        float(grade)
        return True
    except ValueError:
        return False

def create_numeric_grade_error_message(grade,user_id,course_id):
    """
    値が数値でない場合のエラーメッセージを生成
    """
    return f"grade: {grade} is not numeric (user_id: {user_id}, course_id: {course_id})"

def extract_numeric_grade_users(enrollments):
    """
    数値評点のみを抽出
    """
    numeric_grade_users = []
    for row in enrollments:
        grade = row.get("grade")
        if is_numeric_grade(grade):
            numeric_grade_users.append(row)
        else:
            user_id = row.get("user_id","N/A")
            course_id = row.get("course_id","N/A")
            error_message = create_numeric_grade_error_message(grade,user_id,course_id)
            print(error_message)

    return numeric_grade_users

def get_category_average_score(enrollments):
    """
    カテゴリ別 平均評点の算出
    """
    # enrollmentsからcompletion_status=completedユーザーを抽出
    completed_users = extract_completed_users(enrollments)

    # 抽出したユーザーにcoursesを結合、category列を追加
    completed_users_with_category = add_category_to_completed_users(completed_users,courses)

    # completed_users_with_categoryから、gradeが数値のユーザーを抽出
    #     - gradeが数値に変換できたら集計対象listに格納
    #     - gradeが数値に変換できなかったらコンソールにメッセージを出して除外
    # 数値に変換できるかどうかを確認するために、try-exceptを使う
    numeric_grade_users = extract_numeric_grade_users(completed_users_with_category)

    # 抽出結果からカテゴリごとの平均点と集計対象人数を抽出
    # 抽出結果から平均点を算出、小数点第一まで
    # 集計対象が0人なら該当なしフラグを立てる

# 6．人気コースランキングの算出
# 7．特別優秀者リストの算出
# 8．数値変換のエラー回避(+コンソール出力)

category_ranking = get_category_ranking(enrollments,courses)
for index, (category, count) in enumerate(category_ranking, start=1):
    print(f"{index}. {category}: {count}人")

category_average_score = get_category_average_score(enrollments)
print(category_average_score)
