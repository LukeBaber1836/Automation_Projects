from pathlib import Path
import zipfile

root_dir = Path("Files_4")
destination_path = root_dir / Path('destination')

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, 'r') as zf:
        new_path = destination_path / Path(path.stem)
        zf.extractall(path=new_path)
