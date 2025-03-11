
def get_num_words(text):

    words = text.split()

    return len(words)


def sorted(char_count):

    count_list = []

    for char, count in char_count.items():

        if char.isalpha():
            count_list.append({"character":char,"count":count})

    
    count_list.sort(key=lambda x: x["count"], reverse= True)

    return count_list




def char_count(text):

    text = text.lower()

    char_count = {}


    for char in text:

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    

    return char_count



