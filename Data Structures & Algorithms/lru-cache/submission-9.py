class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.lru) >= self.cap:
                tbr = self.lru.pop(0)
                del self.cache[tbr]
        else:
            self.lru.remove(key)

        self.cache[key] = value
        self.lru.append(key)