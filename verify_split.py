import os
from PyPDF2 import PdfReader

expected_counts = {
    "00_Front_Matter.pdf": 19,
    "01_Greetings.pdf": 3,
    "02_Lesson_01.pdf": 10,
    "03_Lesson_02.pdf": 13,
    "04_Lesson_03.pdf": 10,
    "05_Lesson_04.pdf": 13,
    "06_Lesson_05.pdf": 9,
    "07_Lesson_06.pdf": 10,
    "08_Lesson_07.pdf": 10,
    "09_Lesson_08.pdf": 12,
    "10_Lesson_09.pdf": 10,
    "11_Lesson_10.pdf": 12,
    "12_Lesson_11.pdf": 9,
    "13_Lesson_12.pdf": 12,
    "14_Reading_and_Writing.pdf": 43,
}

output_dir = "output"
all_passed = True

print("Verifying page counts...")
for filename, expected in expected_counts.items():
    filepath = os.path.join(output_dir, filename)
    if not os.path.exists(filepath):
        print(f"FAIL: {filename} does not exist.")
        all_passed = False
        continue

    try:
        reader = PdfReader(filepath)
        count = len(reader.pages)
        if count == expected:
            print(f"PASS: {filename} has {count} pages.")
        else:
            print(f"FAIL: {filename} has {count} pages, expected {expected}.")
            all_passed = False
    except Exception as e:
        print(f"FAIL: Could not read {filename}. Error: {e}")
        all_passed = False

if all_passed:
    print("\nAll verification checks passed.")
else:
    print("\nVerification failed.")
