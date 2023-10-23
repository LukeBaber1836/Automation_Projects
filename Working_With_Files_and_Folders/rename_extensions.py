from pathlib import Path

roo_dir = Path('Files_3')

# Changes extensions from .txt to .csv
for path in roo_dir.rglob("*.txt"):
    if path.is_file():
        # Rename .txt files to .csv
        new_filepath = path.with_suffix(".csv")
        path.rename(new_filepath)
        
