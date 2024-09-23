import os

file_path = "pdfs/ID383113_Файзуллаев_Мухсин_реа_мед_00_00_1995.pdf"

if not os.path.exists(file_path):
    print(f"Fayl topilmadi: {file_path}")
else:
    print("Fayl mavjud")
