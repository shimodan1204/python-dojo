import re
from datetime import datetime
import os

def sort_all_python_codes_file(filepath="all_python_codes.txt"):
    """
    all_python_codes.txt ファイル内のコードブロックを、ファイルパスに含まれる日付情報を基にソートします。
    """
    separator_marker = "=================================================="

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            full_content = f.read()
    except FileNotFoundError:
        print(f"エラー: ファイル '{filepath}' が見つかりませんでした。")
        return

    if not full_content.strip():
        print(f"ファイル '{filepath}' は空です。処理をスキップします。")
        return

    # 各ブロックは "SEP\nFile:path\nSEP\ncontent..." の形式であると想定
    # re.DOTALL を使用して、content内の改行も .*? でマッチさせる
    # (?=\n{re.escape(separator_marker)}\nFile:|$) は、次のブロックの開始または文字列の終端を先読みする
    block_pattern_str = rf"({re.escape(separator_marker)}\nFile: [^\n]+\n{re.escape(separator_marker)}\n(?:.*?(?=\n{re.escape(separator_marker)}\nFile:|$)))"

    extracted_blocks = re.findall(block_pattern_str, full_content, re.DOTALL)

    if not extracted_blocks:
        # ブロックが見つからないが、ファイルに内容がある場合（セパレータのみ、または未知の形式）
        if full_content.strip() == separator_marker or not full_content.strip():
            # 元の内容が空かセパレータのみの場合は、そのまま書き戻す（変更なし）
            pass # No change needed, content is already what it should be if no blocks
        else:
            print(f"警告: ファイル '{filepath}' からソート対象のブロックを抽出できませんでした。ファイル形式が予期されたものではない可能性があります。ファイルは変更されません。")
        return


    def get_sort_key_from_block_content(block_text_content):
        # block_text_content は "SEP\nFile:path\nSEP\ncontent..." という形式
        # "File: path" の行からパスを抽出
        match_file_line = re.match(rf"{re.escape(separator_marker)}\nFile: (.*?)\n", block_text_content)
        if not match_file_line:
            # 通常発生しないはずだが、フォールバックとしてブロック全体をキーに
            return (datetime.min, 0, 0, block_text_content)

        file_path = match_file_line.group(1)

        # パス (例: "2025/2025-05-11/task.py", "2025/2025-05-11-2/task.py") から日付部分を抽出
        path_parts = file_path.split('/')
        date_str_to_parse = None

        for part in path_parts:
            # "YYYY-MM-DD" または "YYYY-MM-DD-N" の形式を探す
            m = re.match(r"(\d{4}-\d{2}-\d{2})(?:-(\d+))?", part)
            if m:
                date_str_to_parse = m.group(0) # マッチした部分全体 (例: "2025-05-11" or "2025-05-11-2")
                break

        if not date_str_to_parse:
            # ディレクトリ名に日付形式が見つからない場合、ファイル名自体から探す試み
            filename = os.path.basename(file_path)
            m_fn = re.match(r"(\d{4}-\d{2}-\d{2})(?:-(\d+))?", filename)
            if m_fn:
                date_str_to_parse = m_fn.group(0)
            else:
                print(f"警告: ソート用の日付をパス '{file_path}' から抽出できませんでした。このブロックは先頭に来る可能性があります。")
                return (datetime.min, 0, 0, file_path) # 日付が見つからない場合は、パス文字列でソート（実質的に先頭）

        # 抽出した日付文字列 (date_str_to_parse) をパース
        # date_str_to_parse は "YYYY-MM-DD" or "YYYY-MM-DD-N"
        date_ymd_part_match = re.match(r"(\d{4}-\d{2}-\d{2})(?:-(\d+))?", date_str_to_parse)
        # この上のロジックで date_str_to_parse が設定されていれば、これは常にマッチするはず
        date_ymd_str = date_ymd_part_match.group(1)  # "YYYY-MM-DD"
        number_part_str = date_ymd_part_match.group(2) # "N" or None

        try:
            date_obj = datetime.strptime(date_ymd_str, "%Y-%m-%d")
        except ValueError:
            print(f"警告: パス '{file_path}' 内の日付文字列 '{date_ymd_str}'の形式が無効です。")
            return (datetime.min, 0, 0, file_path) # 不正な日付の場合は先頭へ

        if number_part_str:
            # "YYYY-MM-DD-N" 形式の場合 (例: 2025-04-07-2)
            # (日付オブジェクト, 1, 追番, 元のファイルパス)
            return (date_obj, 1, int(number_part_str), file_path)
        else:
            # "YYYY-MM-DD" 形式の場合 (例: 2025-04-07)
            # (日付オブジェクト, 0, 0, 元のファイルパス)
            return (date_obj, 0, 0, file_path)

    extracted_blocks.sort(key=get_sort_key_from_block_content)

    sorted_full_content = "".join(extracted_blocks)

    # 元のファイルが改行で終わっていて、ソート後になくなっていたら追加する
    # ただし、findall のパターンが適切であれば、ブロック内の末尾改行は保持されるはず
    if full_content.endswith('\n') and not sorted_full_content.endswith('\n'):
        sorted_full_content += '\n'

    # 元のファイルと比較し、変更があった場合のみ書き込む
    if sorted_full_content.strip() == full_content.strip():
        print(f"ファイル '{filepath}' は既にソートされています。変更はありません。")
    else:
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(sorted_full_content)
            print(f"ファイル '{filepath}' のブロックをソートし、上書き保存しました。")
        except Exception as e:
            print(f"エラー: ファイル '{filepath}' の書き込み中に問題が発生しました: {e}")


if __name__ == "__main__":
    # スクリプト実行前に、対象ファイルが正しいか確認を促すメッセージ
    target_file = "all_python_codes.txt"
    print(f"このスクリプトは '{target_file}' の内容を直接変更します。")
    # Python 3.9+ では input() が使えますが、ここでは自動実行を前提とし、確認ステップは入れません。
    # ユーザーが手動で実行する際に注意するように促します。
    # proceed = input(f"よろしければ 'yes' を入力してください: ")
    # if proceed.lower() == 'yes':
    #     sort_all_python_codes_file(target_file)
    # else:
    #     print("処理をキャンセルしました。")
    sort_all_python_codes_file(target_file)
