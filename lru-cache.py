from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_value = OrderedDict()


    def get(self, key: int) -> int:
        check = self.key_value.get(key, None)
        # if check:
        if key in self.key_value:
            self.key_value.move_to_end(key)
            return check
            # return 1
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        check = self.key_value.get(key, None)
        if check:
            self.key_value.move_to_end(key)
        self.key_value[key] = value

        if len(self.key_value) > self.capacity:
            self.key_value.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
