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

    # Define the splits: (start_index, end_index, filename)
    # end_index is exclusive. None means "to the end".
    # Start Index = (Book Page + 8) // 2
    splits = [
        (0, 19, "00_Front_Matter"),
        (19, 22, "01_Greetings"),
        (22, 32, "02_Lesson_01"),
        (32, 45, "03_Lesson_02"),
        (45, 55, "04_Lesson_03"),
        (55, 68, "05_Lesson_04"),
        (68, 77, "06_Lesson_05"),
        (77, 87, "07_Lesson_06"),
        (87, 97, "08_Lesson_07"),
        (97, 109, "09_Lesson_08"),
        (109, 119, "10_Lesson_09"),
        (119, 131, "11_Lesson_10"),
        (131, 140, "12_Lesson_11"),
        (140, 152, "13_Lesson_12"),
        (152, None, "14_Reading_and_Writing"),
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
    parser = argparse.ArgumentParser(description="Split Genki textbook PDF by lesson.")
    parser.add_argument("-i", "--input", default="Genki_full_textbook 2.pdf", help="Path to input PDF file.")
    parser.add_argument("-o", "--output", default="output", help="Output directory.")
    args = parser.parse_args()

    split_pdf(args.input, args.output)
