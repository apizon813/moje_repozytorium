def char_number(word):
    directory = {}
    for char in word:
        if char not in directory:
            directory[char] = 1
        else:
            directory[char] += 1
    return directory


def merge_word_list(word_list):
    text = ''
    for word in word_list:
        text.append(word + ' ')
    

def remove_words(sentence, specifics):
    sentence_split = sentence.split()
    output = []
    for word in sentence_split:
        char_dictionary = char_number(word)
        word_good = True
        for double in specifics:
            letter, count = double
            if letter in char_dictionary and char_dictionary[letter] >= count:
                word_good = False
        if word_good:
            output.append(word)
    output = ' '.join(output)
    return output


word = 'kukułka' #input("Choose a word: ")
print(char_number(word))


text = 'Alice in wonderland went into a deep coma.'
text1 = "I literally can't deal with this drama right now." 
doubles = [('a', 2), ('l', 3)]

print(remove_words(text1, doubles))