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
- `2025-04-10.py`：文字列から数字だけを抽出する関数（`.isdigit()`＋`.isascii()`の組み合わせで全角・半角を制御）
- `2025-04-10-2.py`：テキストファイルから「数字だけの行」を抽出する処理（`with open()` によるファイル読み取り・`strip()`活用）

---

## 🧗 現在の修行レベル

- **開始日**：2025年4月6日
- **現在の難易度**：★☆☆（初級〜中級に移行）
  - `for`文 / `if`文 / 関数定義
  - list comprehension（内包表記）← 修行完了
  - `enumerate()` による index 操作 ← 修行完了
  - `is○○()` 系メソッド（`islower()` / `isupper()` / `isdigit()` / `isalpha()` / `isalnum()` / `isascii()`）← 修行完了
  - 📁 **ファイル操作入門 ←🆕 スタート！**
    - `with open()` の使い方と自動クローズの仕組み
    - `strip()` で改行除去
    - `.isdigit()` と組み合わせた条件フィルタリング

- **今後の目標**：
  - ファイルへの書き込み（`write()` / `a`モード）や複数ファイル処理
  - CSV・JSONなどの実用フォーマットに触れる
  - 書き出し処理や、構造的な読み取りの応用に挑戦する

  
---

## 📝 補足メモ（2025-04-09）

- `.isalnum()` だけでは「年」などの漢字もヒットするため、`.isascii()` を併用して英数字だけを抽出する方法を習得
- `.vscode/` フォルダは `.gitignore` に追加し、GitHubリポジトリから削除してスッキリ整理
- GitHubとの複数端末同期（Windows↔Mac）を達成！ `git pull` による差分取得を習得
- `git diff` の見方や `--cached` の使い分けも体感し、Gitの理解が実践レベルへ

---

引き続き精進！
※この履歴はGPT兄さんが作成しています