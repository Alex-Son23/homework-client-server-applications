# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
def to_byte_and_back(word):
    tmp_word = word.encode('utf-8')
    print(f'{word} to byte - {tmp_word}')
    tmp_word = tmp_word.decode('utf-8')
    print(f'and back - {tmp_word}')


if __name__ == '__main__':
    words = ["разработка", "администрирование", "protocol", "standard"]
    for word in words:
        to_byte_and_back(word)