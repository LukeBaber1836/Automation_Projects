from pathlib import Path

roo_dir = Path('Files')
file_paths = roo_dir.glob("**/*")

# Renames batch of files using pathlib
for path in file_paths:
    if path.is_file():
        # Two folder names
        year = path.parts[1]
        month = path.parts[2]

        # Rename .txt files
        new_name = f"{year}-{month}-{path.parts[3]}"
        new_filepath = path.with_name(new_name)
        path.rename(new_filepath)
        
