import string

# testing = input("Enter some test text: ")

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def normalize_text(text):
    """lowercases and removes punctuation from text, replaces all whitespace with normal spaces. Multiple whitespace will be compressed into single space"""
    text = text.casefold()
    valid_chars = string.ascii_letters + string.whitespace + string.digits
    new_text = ""
    for char in text:
        if char in valid_chars:
            new_text += char

    text = new_text
    text = text.replace("\n", " ")
    return text


def print_word_freq(filename):
    """Read in `file` and print out the frequency of words in that file."""
    with open(filename) as file:
        text = file.read()

    text = normalize_text(text)
    #or could use casefold
    words = []
    for word in text.split(" "):
        if word != '' and word not in STOP_WORDS:
            words.append(word)
    
    print(words)
    return words

def word_freq(text):
    """frequency of words in text"""
    text = list(text.split(" "))
    words_count = {}
    for word in text:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    
    return words_count


def adjust_value(a_dict):
    """adjust the value to include asterisks"""
    for item, count in a_dict.items():
        print(item + " | " + str(count) + " " + str(("*" * count)))

step_1 = print_word_freq()
step_2 = word_freq(step_1)
adjust_value(step_2)





if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)






#ATTEMPTS FROM BEFORE CLASS
#removes punctuation
# def remove_non_punc(text):
#     """Remove any character that isn't a letter"""
#     all_letters = "abcdefghijklmnopqrstuvwxyz "
#     all_letters += all_letters.upper()
#     all_letters += " "

#     clean_text = ""
#     for char in text:
#         if char in all_letters:
#           clean_text += char  
#     return clean_text

# #make lowercase
# def lowercase(text):
#     text = text.lower()
#     return text

# text_list = list(text)
# #remove stop words
# def remove_stops(text):
#     #making text into list
#     for word in text:
#         if word in STOP_WORDS:
#             text_list.remove(word)
#     return text_list



# #creating dictionary from words in text

# def word_counter(text_list):
#     word_count = {}
#     for word in text_list:
#         word_count = dict(zip("word"), range(len(text_list)))
#     print(word_count)

# #counting words in list, adjusting value in dictionary
# def count_adjust(text_list):
#     word_count = {}
#     for word in text_list:
#         word_count['word'] = text_list.count("word")



