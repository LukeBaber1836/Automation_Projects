from pathlib import Path

roo_dir = Path('Files')
file_paths = roo_dir.iterdir()

for path in file_paths:
    print(path)
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(new_filepath)
    path.rename(new_filepath)
