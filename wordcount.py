# put your code here.

def word_count(filename):
    file = open(filename)
    dict_word_count = {}

    for line in file:
        line = line.rstrip()
        words = line.split(' ')
        # print(words)
        for word in words:
            dict_word_count[word] = dict_word_count.get(word, 0) + 1

    for word in dict_word_count:
        print(word, dict_word_count[word])

word_count('test.txt')
word_count('twain.txt')