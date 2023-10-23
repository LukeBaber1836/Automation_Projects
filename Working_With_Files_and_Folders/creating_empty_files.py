from pathlib import Path

root_dir = Path("Files_4")

for i in range(10, 21):
    file_name = str(i) + '.txt'
    filepath = root_dir / Path(file_name)
    filepath.touch()