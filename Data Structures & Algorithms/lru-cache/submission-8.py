class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.lru = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.lru:
            if len(self.lru) == self.capacity:
                self.cache.pop(self.lru[0])
                self.lru.pop(0)
        else:
            self.lru.remove(key)
        self.cache[key] = value
        self.lru.append(key)
