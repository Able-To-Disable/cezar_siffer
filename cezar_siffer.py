import re
import string

CYR_NUMBER = "0123456789"
CYR_ALPHA_LOWERCASE = "абвгдеёжзийклмнопрстуфцчшщъыьэюя"

OFFSET_INDEX = int(input("offset? "))
CHECKING_STRING = input("string? ").strip()


def is_number_character(character):
    return re.search(r'[0-9]', character)


def is_russian_character(character):
    return re.search(r'[а-яА-Я]', character)


def is_english_character(character):
    return re.search(r'[a-zA-Z]', character)


def get_modified_char(alphabet_string, checking_char):
    return alphabet_string[(alphabet_string.index(checking_char) + OFFSET_INDEX) % len(alphabet_string)]


result_string = ''
for char in CHECKING_STRING:
    if not (char.isnumeric() or char.isspace() or char in string.punctuation):
        if is_russian_character(char):
            char = get_modified_char(CYR_ALPHA_LOWERCASE
                                     if char.islower()
                                     else CYR_ALPHA_LOWERCASE.upper(),
                                     char)
        elif is_english_character(char):
            char = get_modified_char(string.ascii_lowercase
                                     if char.islower()
                                     else string.ascii_uppercase,
                                     char)
        elif is_number_character(char or int):
            char = get_modified_char(CYR_NUMBER, char)

    result_string += char
print(f"Result: {result_string}")
