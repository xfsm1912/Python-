import re
from Lesson12_OOD_II.SearchEngineBase import SearchEngineBase


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []

        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)

        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False

        return True

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式取出标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白词
        word_list = filter(None, word_list)
        # 返回单词的set
        return set(word_list)


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus('./input/'+file_path)

    while True:
        query = input()
        # query = 'i have a dream'
        results = search_engine.search(query)
        print('found {} results(s):'.format(len(results)))
        for result in results:
            print(result)


BOW_search_engine = BOWEngine()
main(BOW_search_engine)


