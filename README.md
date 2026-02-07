# pdf_divide

This tool splits the "Genki I (3rd Edition)" textbook PDF into separate files for each lesson.

## Requirements

- Python 3
- PyPDF2

You can install the dependencies with pip:

```bash
pip install PyPDF2
```

## Usage

Place your textbook PDF file (`full_textbook.pdf` or `Genki_full_textbook 2.pdf`) in the same directory as the script.

Run the script:

```bash
python split_pdf.py
```

By default, it looks for `full_textbook.pdf`. If that file is not found, it will try `Genki_full_textbook 2.pdf`. It outputs the split files into an `output/` directory.

### Custom Input/Output

You can specify a different input file or output directory using command-line arguments:

```bash
python split_pdf.py -i "your_textbook.pdf" -o "your_output_folder"
```

## Output

The script generates the following files:

- `00_Front_Matter.pdf`
- `01_Greetings.pdf`
- `02_Lesson_01.pdf` through `13_Lesson_12.pdf`
- `14_Reading_and_Writing.pdf`
