from pathlib import Path
import shutil

source = Path(r"C:\Users\TheEp\Desktop\Python\Tarot Project")
backup = Path(r"C:\Users\TheEp\OneDrive\Desktop\Python\Tarot Project")

backup.mkdir(parents=True, exist_ok=True)

for file in source.iterdir():
    if file.is_file():
        destination = backup / file.name
        shutil.copy2(file, destination)
        print(f"Copied: {file.name}")