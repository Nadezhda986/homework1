class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        name = 'test_file.txt'
        with open(name, 'r', encoding='utf-8') as file:
            list_ = file.read().split()
            list_0 = [',', '.', '=', '!', '?', ';', ':', ' - ']
            self.list_1 = []
            for i in list_:
                if i not in list_0:
                    self.list_1.append(i.lower())
            all_words[name] = self.list_1
            return all_words

    def find(self, word):
        word_words = {}
        word = word.lower()
        for i in self.list_1:
            if i == word:
                number_ = self.list_1.index(i) + 1
                word_words[self.file_names] = number_
        return word_words

    def count(self, word):
        word_ = []
        word_words = {}
        word = word.lower()
        for i in self.list_1:
            if i == word:
                word_.append(i)
                x = (len(word_))
                word_words[self.file_names] = x
        return word_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('text')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего