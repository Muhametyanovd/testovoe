def encryptxor(text: str, key: str) -> str:
    """
    :param text:
    :param key:
    :return:

    Функция шифрования по методу Исключающее ИЛИ(XOR).
    Для текста и ключа берется unicode-позиция каждого символа и используется XOR попарно для каждого символа в тексте и
    ключе. Для полученных чисел возвращается unicode-символ, таким образом создается зашифрованный текст.
    """
    return "".join(chr(ord(text_chr) ^ ord(key_chr)) for text_chr, key_chr in zip(text, key))


def textinput() -> str:
    """
    :return:

    Функция получения текста, который нужно зашифровать. Если введена пустая строка, возвращает ошибку.
    """
    try:
        intext: str = input("Введите текст:")
        if intext == '':
           raise ValueError("Текст не должен быть пустым!")
    except ValueError as v:
        print(v)
        exit()
    return intext


def keyinput() -> str:
    """
    :return:

    Функция получения ключа, которым нужно зашифровать текст. Если введена пустая строка, возвращает ошибку.
    """
    try:
        inkey: str = input("Введите ключ:")
        if inkey == '':
            raise ValueError("Ключ не должны быть пустым!")
    except ValueError as v:
        print(v)
        exit()
    return inkey


def equallen(k: str, t: str) -> str:
    """
    :param k:
    :param t:
    :return:
    Если длина ключа получилась больше, чем длина текста, то укорачивает ключ до длины текста.
    """
    d = len(k) - len(t)
    shortk = k[:-d]
    return shortk


if __name__ == '__main__':
    try:
        text: str = textinput()
        key: str = keyinput()
        # Если ключ короче текста, удлиняем ключ, чтобы не потерять данные
        if len(key) < len(text):
            while len(key) < len(text):
                key += "".join(key_char for key_char in key)
        # Если ключ длиннее текста, подгоняем его длину до длины текста функцией
        if len(text) < len(key):
            key = equallen(key, text)
            print('Ключ короче текста. Новый ключ:', key)
        print('Зашифрованное сообщение:', encryptxor(text, key))
    except KeyboardInterrupt:
        print("Работа программы прервана!")
    finally:
        print("Работа программы завершена!")
