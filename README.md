# Python道場（1日1問の筋トレ修行）

Pythonの文法を手に馴染ませるため、1日1問ずつ問題に取り組んでいます。

毎日の問題は ChatGPT に出題してもらい、基本的な書き方の練習と、
GitHub を使った add / commit / push の習慣化も目的としています。

---

## 🥋 修行の目的

- Pythonの基本文法を自然に書けるようにする
- 1日10〜15分で継続できる習慣を作る
- Git操作（add / commit / push）を毎日の流れにする

---

## 📅 修行ログ

- `2025-04-06.py`：リストから偶数を抽出する関数（内包表記あり）
- `2025-04-07.py`：文字列から母音だけを抽出する関数（`for`文 & `list comprehension`）
- `2025-04-07-2.py`：文字列から母音が出現する**インデックス**のみ抽出（`enumerate()` 入門＆応用）
- `2025-04-08.py`：偶数のみを2倍して返す関数（`for`文＋内包表記の使い分け）
- `2025-04-08-2.py`：文字列から小文字アルファベットのみ抽出（正規表現での処理）
- `2025-04-09.py`：英数字のみを抽出する関数（`.isalnum()`＋`.isascii()` を併用して漢字や記号を除外）
- `2025-04-10.py`：文字列から数字だけを抽出する関数（`.isdigit()`＋`.isascii()`で全角と半角を制御）
- `2025-04-10-2.py`：テキストファイルから「数字だけの行」を抽出する処理（`with open()` によるファイル読み取り・`strip()`活用）
- `2025-04-10-3.py`：テキストファイルの内容を逆順にして別ファイルに書き出す（`readlines()`＋`.reverse()`＋`write()` の基本型）
- `2025-04-11.py`：今日の日付とメッセージを "input.txt" に追記する関数（`datetime.date.today()`＋`write()`＋追記モード `"a"` を活用）
- `2025-04-12.py`：テキストファイル内から特定のキーワードを含む行だけを抽出する関数（`in` 演算子＋`.lower()`で大文字・小文字を無視した検索を実装）
- `2025-04-13.py`：テキストファイルの内容を「行番号付き」で表示する関数（`enumerate()` の `start` パラメータを活用し、表示順を1から開始）
- `2025-04-14.py`："input.txt" から数字だけの行を抽出し、"output.txt" に書き出す関数（`isdigit()` を使った条件フィルタ＋リスト操作＋ファイル出力の基本型を確認）
- `2025-04-15.py`：CSVファイルの各行を行番号付きで表示（`csv.reader()`＋`enumerate(start=1)` による基本の読み取り）
- `2025-04-15-2.py`：CSVファイルから2列目のデータだけを抽出して表示（インデックスアクセス `[1]` による列指定処理）
- `2025/0416-1/2025-04-16-1.py`：CSVファイルから2列目が "Python" の行だけを抽出し、リストとして出力
- `2025/0416-2/2025-04-16-2.py`：抽出した行を新たなCSVファイルに書き出し（`csv.writer()`＋`writerows()`）
- `2025/0416-3/2025-04-16-3.py`：CSVファイルの全行を行番号付きで `log.txt` に記録（`enumerate(..., start=1)`）
  - ※ 実行環境によるカレントディレクトリの違いにより、`__file__` を使ったパス構成方法を習得
  - ※ `os.path.dirname(__file__)` を重ねて階層をさかのぼる応用パターンも確認
- `2025/0418/2025-04-18-1.py`：
  - 2列目に "Python" を含む行のみ抽出し、`log.txt` に出力（部分一致 + 大文字小文字無視）
  - 内包表記による一行出力表現も試行
  - `",".join(row)` vs `str(row)` の出力フォーマットの違いを確認
- `2025/0418/2025-04-18-2.py`：
  - "Python" を含む行だけを `filtered.csv` に出力し、同時に件数を `log.txt` に記録
  - 処理ステップを明確に分けて記述（読み込み → 抽出 → 書き出し → ログ）
  - 行数カウント処理（`match_rows_count`）と、内包表記による `len()` 利用パターンの違いを体感
  - 書き方の構造改善（フィルタ結果のリスト化 → 使い回し可能な形）について考察
- `2025/0419/2025-04-19.py`：
  - `file1.csv` と `file2.csv` を読み込み、内容を1つのファイルに統合（`merged.csv`）
  - `csv.reader()` でリスト化した2ファイルの内容を `list_f1 + list_f2` で結合
  - `csv.writer().writerows()` による一括書き出し構成を採用
  - 複数ファイルの読み→統合→書き出しの流れを正確に整理・実装

- 🌱 修行中に遭遇した「`writerow` を `writerrow` と書いてしまう」タイプミスを自己発見・自己修正
  - この気づきから `writerow()` vs `writerows()` の違いと用途も再確認
  - 打鍵ミスに気づく観察力とリカバリー力の重要性を実感

---

## 🧗 現在の修行レベル

- **開始日**：2025年4月6日
- **現在の難易度**：★★★★（CSVファイル応用・実務構成対応中）
  - 複数ファイルの同時操作、構造的マージ処理、CSV形式の厳格な出力管理
  - `writerow()` / `writerows()` の正確な使い分け
  - タイプミスに気づく視点・エラーメッセージの読み取りスキル
  - 「コードの見通し」と「柔軟な書き方」の両立を意識した構成

- **次回の目標**：
  - ヘッダー付きCSVの扱い（`csv.DictReader()` の導入）
  - ファイル内での条件付きマージ・フィルタ付き統合処理

---

引き続き精進！
※この履歴はGPT兄さんが作成しています