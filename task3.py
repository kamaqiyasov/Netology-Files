import os

def get_len_by_file(file):
    with open(os.path.join(os.getcwd(), file), 'r', encoding='utf-8') as f:
        text = f.read()
    return len(text.split('\n'))

files = ['1.txt', '2.txt', '3.txt']    
files.sort(key=lambda x: get_len_by_file(x))

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name in files:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            str_count = len(text.split('\n'))
            result_file.write(f'{file_name}\n')
            result_file.write(f"{str_count}\n")
            result_file.write(f'{text}\n')