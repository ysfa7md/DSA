class HashMap:
    def __init__(self, cap=4):
        self.cap = cap
        self.size = 0
        self.backits = [[] for _ in range(cap)]

    def put(self, key, value):
        idx = self._hash(key)
        backit = self.backits[idx]

        for i, (k, _) in enumerate(backit):
            if k == key:
                backit[i] = (key, value)
                return

        self.backits[idx].append((key, value))
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        backit = self.backits[idx]

        for k, v in backit:
            if k == key:
                return v

        raise Exception("key not found")

    def remove(self, key):
        idx = self._hash(key)
        backit = self.backits[idx]
        for i, (k, v) in enumerate(backit):
            if k == key:
                del backit[i]
                self.size += 1
                return

        raise Exception("key not found")

    def contains_key(self, key):
        idx = self._hash(key)
        backit = self.backits[idx]

        for k, _ in backit:
            if k == key:
                return True
        return False

    def contains_value(self, value):
        for backit in self.backits:
            for _, v in backit:
                if v == value:
                    return True
        return False

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def keys(self):
        return [k for backit in self.backits for k, _ in backit]

    def values(self):
        return [v for backit in self.backits for _, v in backit]

    def items(self):
        return [(k, v) for backit in self.backits for k, v in backit]

    def _hash(self, key):
        return hash(key) % self.cap

    def clear(self): ...

    def resize(self, new_capacity): ...

    def load_factor(self): ...

    def _find_slot(self, key): ...

    def _rehash(self): ...

    def __repr__(self):
        return f"HashMap({self.items()})"

    def __str__(self):
        return f"{self.items()}"


def main():
    hm = HashMap(32)
    
    hm.put(4, 6)
    hm.put(5, 2)
    hm.put(3, 6)

    print(hm.get(4))
    print(hm.get(5))

    print(hm.contains_key(5))
    print(hm.contains_key(1))
    print(hm.contains_value(5))
    print(hm.contains_value(6))

    hm.remove(5)
    # hm.remove(5)

    print(hm)
    print(hm.items())
    print(hm.__repr__())


if __name__ == "__main__":
    main()
