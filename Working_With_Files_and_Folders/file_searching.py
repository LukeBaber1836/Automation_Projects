from pathlib import Path
import zipfile

root_dir = Path('Files_5')

file_num = input("Enter file number you are looking for: ")

for path in root_dir.rglob("*"):
    if file_num in path.stem:
        print(path.absolute())
        