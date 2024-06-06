from pathlib import Path
p = Path(".", "spam.txt")
file_content = p.read_text()
print(file_content)