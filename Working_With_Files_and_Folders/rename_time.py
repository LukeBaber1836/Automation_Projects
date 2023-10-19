from pathlib import Path
from datetime import datetime

roo_dir = Path('Files_2')
file_paths = roo_dir.glob("**/*")

# Renames batch of files using pathlib
for path in file_paths:
    if path.is_file():
        # Get date created
        stats = path.stat()
        time_made = datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d_%H.%M.%S")

        # Rename .txt files
        #new_name = path.name[-5] + '.txt'
        new_name = time_made + '-' + path.name
        print(new_name)
        new_filepath = path.with_name(new_name)
        path.rename(new_filepath)
        
