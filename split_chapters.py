import os
from PyPDF2 import PdfReader, PdfWriter

# ==========================================
# CONFIGURATION (設定)
# ==========================================

# Define the PDF files and their chapter ranges here.
# Format: "filename": [
#     ("Chapter Name", start_page, end_page),
# ]
# Note: start_page is inclusive (0-indexed), end_page is exclusive.
# If end_page is None, it goes to the end of the file.
# ページ番号は0から始まります。end_pageは含まれません（そのページの手前まで）。
# Noneを指定すると、ファイルの最後までになります。

# ★★★ ここを編集してください / EDIT HERE ★★★
CONFIG = {
    "original/toeic_speaking_question.pdf": [
        # 例: ("チャプター名", 開始ページ, 終了ページ)
        # 実際のページ番号に合わせて変更してください。
        ("00_Front_Matter", 0, 5),
        ("01_Chapter_1", 5, 15),
        ("02_Chapter_2", 15, 30),
        ("03_Chapter_3", 30, None), # To the end
    ],
    "original/toeic_speaking_answers.pdf": [
        # Example ranges
        ("00_Answers_Front", 0, 3),
        ("01_Answers_Ch1", 3, 10),
        ("02_Answers_Ch2", 10, None),
    ]
}

# Output directory
OUTPUT_DIR = "output_chapters"

# ==========================================
# END CONFIGURATION
# ==========================================

def split_pdf(file_path, chapters):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    print(f"Processing {file_path}...")

    try:
        reader = PdfReader(file_path)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return

    total_pages = len(reader.pages)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    file_output_dir = os.path.join(OUTPUT_DIR, base_name)

    if not os.path.exists(file_output_dir):
        os.makedirs(file_output_dir)

    for chapter_name, start, end in chapters:
        # Handle "None" for end page
        if end is None:
            end = total_pages

        # Validate ranges
        if start < 0:
            start = 0
        if end > total_pages:
            print(f"Warning: End page {end} exceeds total pages ({total_pages}). Clamping.")
            end = total_pages
        if start >= end:
            print(f"Skipping {chapter_name}: Start page {start} >= End page {end}")
            continue

        writer = PdfWriter()
        for i in range(start, end):
            writer.add_page(reader.pages[i])

        output_filename = os.path.join(file_output_dir, f"{chapter_name}.pdf")
        with open(output_filename, "wb") as f:
            writer.write(f)

        print(f"  Saved {chapter_name} (Pages {start}-{end}) to {output_filename}")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for file_path, chapters in CONFIG.items():
        split_pdf(file_path, chapters)

if __name__ == "__main__":
    main()
