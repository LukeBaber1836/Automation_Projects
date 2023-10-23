from pathlib import Path

root_dir = Path('Del_Files')

# Writes over existing files, and then deletes them forever
for path in root_dir.glob('*.csv'):
    with open(path, 'wb') as file:
        file.write(b'') # Writes blank data
    path.unlink()   # Delete files