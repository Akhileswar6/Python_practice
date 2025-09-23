# pathlib module -> Object-oriented filesystem paths

# Listing Subdirectories
from pathlib import Path
# p = Path('/')
# for subdir in p.iterdir():
#     print(subdir)

# Listing Python Source Files in This Directory Tree
p = Path('/')
# files = p.rglob('*.py')
# for f in files:
#     print(f)

# Querying Path Properties
print(("Is absolute?", p.is_absolute()))
print(("Is a file?", p.is_file()))
print(("Is a directory?", p.is_dir()))
print(("File name:", p.name))
print(("File suffix:", p.suffix))
print(("File stem:", p.stem))
print(("Parent directory:", p.parent))


# Reading and writing to a file
with (p / 'sample.txt').open('r', encoding='utf-8') as file:
    content = file.read()
    print(content)

with (p / 'sample.txt').open('a',encoding='utf-8') as file:
    file.write("\nAppended line using pathlib module.")