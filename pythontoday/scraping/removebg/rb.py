from rembg import remove
from PIL import Image
from pathlib import Path

def remove_bg():
    list_of_extensions = ['*.jpg']
    all_files = []

    for ext in list_of_extensions:
        all_files.extend(Path(r'C:\Users\s.fedoruk\Desktop\amazing\pythontoday\scraping\removebg\input_img').glob(ext))

    # print(all_files)

    for index, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem

        output_path = fr"C:\Users\s.fedoruk\Desktop\amazing\pythontoday\scraping\removebg\output_img\{file_name}_output.png"

        # print(output_path)

        input_img = Image.open(input_path)
        output_img = remove(input_img)

        output_img.save(output_path)

        print(f"Completed: {index + 1}/{len(all_files)}")

def main():
    remove_bg()

if __name__ == "__main__":
    main()