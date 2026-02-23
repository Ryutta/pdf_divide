# PDF Splitter Tool (PDF分割ツール)

このツールは、`original`フォルダにあるPDFファイルを、指定したページ範囲（チャプター）ごとに分割するためのスクリプトです。

## 前提条件

- Python 3.x
- 必要なライブラリ: `PyPDF2`

## インストール

以下のコマンドで必要なライブラリをインストールしてください。

```bash
pip install -r requirements.txt
```

## 使い方

1. **PDFファイルの配置**
   分割したいPDFファイルを `original` フォルダに配置してください（例: `toeic_speaking_question.pdf`, `toeic_speaking_answers.pdf`）。

2. **チャプター設定の編集**
   `split_chapters.py` をテキストエディタで開き、`CONFIG` セクションを編集して、各チャプターのページ範囲を指定してください。

   ```python
   CONFIG = {
       "original/toeic_speaking_question.pdf": [
           # ("ファイル名（チャプター名）", 開始ページ, 終了ページ)
           ("01_Chapter_1", 0, 10),   # 0ページ目から9ページ目まで
           ("02_Chapter_2", 10, 20),  # 10ページ目から19ページ目まで
           ("03_Chapter_3", 20, None), # 20ページ目から最後まで
       ],
       # ... 他のファイルの設定
   }
   ```
   *注意: ページ番号は0から始まります。終了ページはそのページを含みません（その直前まで）。*

3. **スクリプトの実行**
   以下のコマンドを実行してPDFを分割します。

   ```bash
   python split_chapters.py
   ```

4. **結果の確認**
   分割されたPDFファイルは `output_chapters` フォルダに保存されます。ファイルごとにサブフォルダが作成されます。

## ファイル構成

- `original/`: 分割元のPDFファイルを置く場所
- `output_chapters/`: 分割後のPDFが出力される場所
- `split_chapters.py`: 分割を行うスクリプト（設定もここで行います）
- `requirements.txt`: 必要なライブラリの一覧
