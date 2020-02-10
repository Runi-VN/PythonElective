
# Create a Python module, which consists of a class TextContainer. The class shall implement methods for computing statistics on texts.
# Counting the amount of words used in a text.
# Counting the amount of chars used in a text.
# Counting the amount of letters, where letters are all ASCII letter characters
# Remove all punctuation

import string


class TextContainer():

    # wordcount
    def get_word_count(self, string_to_check: str):
        return len(string_to_check.split())  # split on spaces, return len

    # charcount
    def get_char_count(self, string_to_check: str):
        # get all chars, remove spaces
        return len(string_to_check.strip()) - string_to_check.count(' ')

    # ASCII count
    def get_ascii_count(self, string_to_check: str):
        counter = 0
        for char in string_to_check.strip():
            if char in string.ascii_letters:
                counter += 1
        return counter

    # Punctuation removal
    def remove_punctuation(self, string_to_check: str):
        result_string = ""
        for char in string_to_check.strip():
            if char not in string.punctuation:
                result_string += char
        return result_string


test = TextContainer()
test_wordcount = "This sentence has 5 words"  # 5
test_charcount = "1234 5678910 abc"  # 14
test_asciicount = "abc123ABCæøå"  # 6
test_punctuationremove = "Hej mit navn er ?. Sætni[ngen fort{sætter uden @navn@, #da spørgsmå<lste>gn bliver fjernet. []}@@$@$()><"
print(test.get_word_count(test_wordcount))
print(test.get_char_count(test_charcount))
print(test.get_ascii_count(test_asciicount))
print(test.remove_punctuation(test_punctuationremove))
