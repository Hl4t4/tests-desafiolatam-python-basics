import os

os.makedirs('html/assets/img', exist_ok=True)
os.makedirs('html/assets/css', exist_ok=True)

def make_files(path, string):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(string)

