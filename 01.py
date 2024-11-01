import os
import shutil
import argparse
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("src_dir")
    parser.add_argument("dest_dir", nargs="?", default="dist")
    return parser.parse_args()

def copy_and_sort_files(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            
            # Якщо папка, робимо рекурсію
            if os.path.isdir(item_path):
                copy_and_sort_files(item_path, dest_dir)
            
            # Якщо файл, робимо копію
            elif os.path.isfile(item_path):
                # Отримуємо розширення файлу, ігноруємо регістр
                file_extension = Path(item).suffix.lower().strip('.')
                # Призначаємо назву папки для файлів без розширень
                if not file_extension:
                    file_extension = "no_extension"

                dest_subdir = os.path.join(dest_dir, file_extension)
                os.makedirs(dest_subdir, exist_ok=True)
                
                dest_path = os.path.join(dest_subdir, item)
                print(f"Копіюю {item_path} до {dest_path}")
                shutil.copy2(item_path, dest_path)

    except Exception as e:
        print(f"Error: {e}")

def main():
    args = parse_arguments()
    
    if not os.path.exists(args.src_dir):
        print(f"Директорія {args.src_dir} не знайдена.")
        return
    
    # Створюємо директорію призначення (якщо її немає)
    os.makedirs(args.dest_dir, exist_ok=True)
    
    copy_and_sort_files(args.src_dir, args.dest_dir)
    print("Програму завершено.")

if __name__ == "__main__":
    main()


#python 01.py ./TestFolder01 ./TestFolder01Dest
