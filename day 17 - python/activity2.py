#function to check whether
# first and last character of word match
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 0 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("The list of words with matching first and last characters is:\n", lst)
    return ctr
count = match_words(['abc', 'xyz', 'aba', '1221'])
print(f"Number of words with matching first and last characters: {count}")