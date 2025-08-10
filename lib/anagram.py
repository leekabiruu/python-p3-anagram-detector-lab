class Anagram:
    def __init__(self, word):
        self.word = word
        self.word_lower = word.lower()
        self.sorted_word = sorted(self.word_lower)

    def match(self, word_list):
        matches = []
        for word in word_list:
            lower_word = word.lower()
            if lower_word != self.word_lower and sorted(lower_word) == self.sorted_word:
                matches.append(word)
        return matches

print(Anagram("enlist").match(["listen", "silent", "hippopotamus"])) 