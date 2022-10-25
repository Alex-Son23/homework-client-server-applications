# 6. Создать текстовый файл test_file.txt, заполнить его тремя
# строками: «сетевое программирование», «сокет», «декоратор».
# Далее забыть о том, что мы сами только что создали этот
# файл и исходить из того, что перед нами файл в
# неизвестной кодировке.
# Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того,
# в какой кодировке он был создан.
from chardet import detect


strings_for_doc = ["сетевое программирование\n", "сокет\n", "декоратор\n"]
with open('text.txt', 'w', encoding='utf-8') as f:
    f.writelines(strings_for_doc)

with open('text.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print(f'encoding {encoding}')

with open('text.txt', encoding=encoding) as f_en:
    for el_str in f_en:
        print(el_str)
