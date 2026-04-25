import os
import argparse
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_dir):
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        reader = PdfReader(input_path)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return

    total_pages = len(reader.pages)
    print(f"Total pages in input PDF: {total_pages}")

    # Define the splits for Genki II 3rd Edition: (start_index, end_index, filename)
    # end_index is exclusive. None means "to the end".
    # Start Index = (Book Page) // 2 + 19
    splits = [
        (0, 30, "00_Front_Matter"),
        (30, 42, "01_Lesson_13"),
        (42, 54, "02_Lesson_14"),
        (54, 65, "03_Lesson_15"),
        (65, 76, "04_Lesson_16"),
        (76, 87, "05_Lesson_17"),
        (87, 99, "06_Lesson_18"),
        (99, 109, "07_Lesson_19"),
        (109, 122, "08_Lesson_20"),
        (122, 133, "09_Lesson_21"),
        (133, 144, "10_Lesson_22"),
        (144, 156, "11_Lesson_23"),
        (156, None, "12_Reading_and_Writing"),
    ]

    for start, end, name in splits:
        writer = PdfWriter()

        actual_end = end if end is not None else total_pages

        # Verify range
        if start >= total_pages:
            print(f"Skipping {name}: start index {start} >= total pages {total_pages}")
            continue

        if actual_end > total_pages:
            print(f"Warning: {name} end index {actual_end} exceeds total pages. Clamping to {total_pages}.")
            actual_end = total_pages

        print(f"Processing {name} (Pages {start} to {actual_end-1})...")

        for i in range(start, actual_end):
            writer.add_page(reader.pages[i])

        output_filename = os.path.join(output_dir, f"{name}.pdf")
        with open(output_filename, "wb") as f:
            writer.write(f)

        print(f"Saved {output_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split Genki II textbook PDF by lesson.")
    parser.add_argument("-i", "--input", default="original/Genki_Textbook_II_3rd_Edition 2.pdf", help="Path to input PDF file.")
    parser.add_argument("-o", "--output", default="output_genki2", help="Output directory.")
    args = parser.parse_args()

    split_pdf(args.input, args.output)
