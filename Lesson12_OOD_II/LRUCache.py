import pylru
from Lesson12_OOD_II.BOWInvertedindexEngine import BOWInvertedIndexEngine


class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)

    def has(self, key):
        return key in self.cache

    def get(self, key):
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value


class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        super(BOWInvertedIndexEngineWithCache, self).__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('cache hit!')
            return self.get(query)

        result = super(BOWInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)

        return result


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus('./input/'+file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} results(s):'.format(len(results)))
        for result in results:
            print(result)


BOWInvert_cache_search_engine = BOWInvertedIndexEngineWithCache()
main(BOWInvert_cache_search_engine)
