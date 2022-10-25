# 2. Каждое из слов «class», «function», «method» записать в байтовом типе.
# Сделать это необходимо в автоматическом, а не ручном режиме,
# с помощью добавления литеры b к текстовому значению,
# (т.е. ни в коем случае не используя методы encode, decode или функцию bytes)
# и определить тип, содержимое и длину соответствующих переменных.
def str_to_byte(word):
    byte_str = eval(f"b'{word}'")
    print(f"Type of '{byte_str}' - {type(byte_str)}. Length: {len(byte_str)}")


if __name__ == '__main__':
    words_list = ["class", "function", "method"]
    for word in words_list:
        str_to_byte(word)