from pathlib import Path

roo_dir = Path('Files')
file_paths = roo_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[1]
        new_name = parent_folder + '-' + path.name
        new_filepath = path.with_name(new_name)
        path.rename(new_filepath)
        
